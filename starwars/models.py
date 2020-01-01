from itertools import cycle
from random import choice

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q, Sum, FloatField
from django.utils.translation import gettext_lazy as _

from starwars.enums import (
    SKILL_DEPENDANCIES, SPECIES, SPECIES_ABILITIES, ITEM_TYPES, ITEM_WEAPON, ITEM_ARMOR, RANGE_BANDS, ITEM_SKILLS,
    EFFECT_ATTRIBUTE_MODIFIER, ATTRIBUTE_MAX_HEALTH, ATTRIBUTE_MAX_STRAIN, ATTRIBUTE_DEFENSE, ATTRIBUTE_SOAK_VALUE,
    DICT_STATS, DICT_SKILLS, STAT_BRAWN, STAT_WILLPOWER, EFFECT_TYPES, DICE_TYPES, ATTRIBUTES, CHARACTER_TYPES,
    STAT_PRESENCE, COOL, CHARACTER_TYPE_PC, DICE_LIGHT_FORCE, DICE_DARK_FORCE, VIGILANCE, DICE_TRIUMPH, DICE_ADVANTAGE,
    EFFECT_DURATIONS, ACTIVATION_TYPE_PASSIVE, ACTIVATION_TYPES, CHARACTER_TYPE_NEMESIS, DIFFICULTY_SIMPLE,
    DICE_TYPE_DIFFICULTY, DICE_TYPE_CHALLENGE, EFFECT_DICE_POOL_MODIFIER, EFFECT_DURATION_FIGHT,
    EFFECT_DURATION_DIRECT, EFFECT_HEALTH_MODIFIER, EFFECT_STRAIN_MODIFIER, EFFECT_DURATION_TARGET_TURN,
    EFFECT_DURATION_SOURCE_TURN)
from starwars.utils import roll_dice


class Player(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True, verbose_name=_("surnom"))

    def __str__(self):
        return self.nickname or self.first_name or self.username

    class Meta:
        verbose_name = _("joueur")
        verbose_name_plural = _("joueurs")


class NamedModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("nom"))
    description = models.TextField(blank=True, verbose_name=_("description"))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Campaign(NamedModel):
    destiny_usage_percentage = models.PositiveSmallIntegerField(
        default=10, verbose_name=_("pourcentage d'utilisation des jetons de destinée"))
    light_tokens = models.PositiveSmallIntegerField(default=0, verbose_name=_("light token"))
    dark_tokens = models.PositiveSmallIntegerField(default=0, verbose_name=_("dark token"))

    def _use_light_token(self):
        self.light_tokens -= 1
        self.dark_tokens += 1
        self.save()

    def _use_dark_token(self):
        self.dark_tokens -= 1
        self.light_tokens += 1
        self.save()

    def set_destiny_tokens(self):
        """
        Roll a force die for each playable characters, light/dark results stands for destiny tokens
        :return: None
        """
        forces_dice_result = roll_dice(force=self.characters.filter(type=CHARACTER_TYPE_PC).count())
        self.light_tokens = forces_dice_result.get(DICE_LIGHT_FORCE)
        self.dark_tokens = forces_dice_result.get(DICE_DARK_FORCE)

    def get_destiny_upgrade(self, character, opposite=False):
        """
        Rand 1-100, if the result is under the destiny_usage_percentage, return True
        :return: bool
        """
        use_ligth_token = (character.type == CHARACTER_TYPE_PC and not opposite) or (
            character.type != CHARACTER_TYPE_PC and opposite)
        if (use_ligth_token and not self.light_tokens) or (not use_ligth_token and not self.dark_tokens):
            return False
        rand = choice(range(1, 101))
        if rand <= self.destiny_usage_percentage:
            if use_ligth_token:
                self._use_light_token()
            else:
                self._use_dark_token()
            return True
        return False

    # Combat
    def set_initiative(self, characters_awareness):
        """
        Set the initiative for every characters involved in a fight
        :param characters_awareness: dict (id_character: awareness(bool)
        :return:
        """
        first_active_character = None
        for id_character, awareness in characters_awareness.items():
            character = self.characters.get(pk=id_character)
            skill_to_test = COOL if awareness else VIGILANCE
            dice_result = roll_dice(**character.get_skill_dice(skill_to_test))
            initiative = dice_result.get('remaining_success', 0) * 10 \
                + dice_result.get(DICE_TRIUMPH, 0) * 5 \
                + dice_result.get(DICE_ADVANTAGE, 0)
            character.initiative = initiative
            character.is_fighting = True
            if not first_active_character or initiative > first_active_character.initiative:
                first_active_character = character
            character.save()
        first_active_character.is_active = True
        first_active_character.save()

    def next_turn(self):
        """
        End the actual character's turn and start the next character's turn
        :return:
        """
        fighting_characters = self.characters.filter(is_fighting=True)
        active_character_turn_ended = False
        next_character = None
        for character in cycle(fighting_characters.order_by('-initiative')):
            if character.is_active:
                character.end_combat_turn()
                active_character_turn_ended = True
                continue
            if not active_character_turn_ended:
                continue
            character.refresh_from_db()
            character.start_combat_turn()
            next_character = character
            break
        return next_character

    def end_fight(self):
        for character in self.characters.filter(is_fighting=True):
            character.end_fight()
        # Remove Effect with fight duration
        CharacterEffect.objects.filter(
            Q(Q(source_character__campaign_id=self.id) | Q(target__campaign_id=self.id)),
            duration_type=EFFECT_DURATION_FIGHT).delete()

    class Meta:
        verbose_name = _("campagne")
        verbose_name_plural = _("campagnes")


class Statistics(models.Model):
    # Characteristics
    brawn = models.PositiveSmallIntegerField(default=0, verbose_name=_("vigueur"))
    agility = models.PositiveSmallIntegerField(default=0, verbose_name=_("agilité"))
    intellect = models.PositiveSmallIntegerField(default=0, verbose_name=_("intelligence"))
    cunning = models.PositiveSmallIntegerField(default=0, verbose_name=_("ruse"))
    willpower = models.PositiveSmallIntegerField(default=0, verbose_name=_("volonté"))
    presence = models.PositiveSmallIntegerField(default=0, verbose_name=_("présence"))

    # Force
    force = models.PositiveSmallIntegerField(default=0, verbose_name=_("force"))
    morality = models.PositiveSmallIntegerField(default=50, verbose_name=_("moralité"))
    conflit = models.PositiveSmallIntegerField(default=0, verbose_name=_("conflit"))

    # Skills
    # General skills
    astrogation = models.PositiveSmallIntegerField(default=0, verbose_name=_("astrogation"))
    athletics = models.PositiveSmallIntegerField(default=0, verbose_name=_("athlétisme"))
    charm = models.PositiveSmallIntegerField(default=0, verbose_name=_("charme"))
    coercion = models.PositiveSmallIntegerField(default=0, verbose_name=_("coercition"))
    computers = models.PositiveSmallIntegerField(default=0, verbose_name=_("informatique"))
    cool = models.PositiveSmallIntegerField(default=0, verbose_name=_("calme"))
    coordination = models.PositiveSmallIntegerField(default=0, verbose_name=_("coordination"))
    deception = models.PositiveSmallIntegerField(default=0, verbose_name=_("tromperie"))
    discipline = models.PositiveSmallIntegerField(default=0, verbose_name=_("sang froid"))
    leadership = models.PositiveSmallIntegerField(default=0, verbose_name=_("commandement"))
    mechanics = models.PositiveSmallIntegerField(default=0, verbose_name=_("mécanique"))
    medecine = models.PositiveSmallIntegerField(default=0, verbose_name=_("médecine"))
    negociation = models.PositiveSmallIntegerField(default=0, verbose_name=_("négociation"))
    perception = models.PositiveSmallIntegerField(default=0, verbose_name=_("perception"))
    piloting = models.PositiveSmallIntegerField(default=0, verbose_name=_("pilotage"))
    resilience = models.PositiveSmallIntegerField(default=0, verbose_name=_("résistance"))
    skulduggery = models.PositiveSmallIntegerField(default=0, verbose_name=_("magouilles"))
    stealth = models.PositiveSmallIntegerField(default=0, verbose_name=_("discretion"))
    streetwise = models.PositiveSmallIntegerField(default=0, verbose_name=_("système D"))
    survival = models.PositiveSmallIntegerField(default=0, verbose_name=_("survie"))
    vigilance = models.PositiveSmallIntegerField(default=0, verbose_name=_("vigilance"))

    # Combat skills
    brawl = models.PositiveSmallIntegerField(default=0, verbose_name=_("pugilat"))
    gunnery = models.PositiveSmallIntegerField(default=0, verbose_name=_("artillerie"))
    lightsaber = models.PositiveSmallIntegerField(default=0, verbose_name=_("sabre laser"))
    melee = models.PositiveSmallIntegerField(default=0, verbose_name=_("corps à corps"))
    ranged_heavy = models.PositiveSmallIntegerField(default=0, verbose_name=_("distance (armes lourdes)"))
    ranged_light = models.PositiveSmallIntegerField(default=0, verbose_name=_("distance (armes légères)"))

    # Knowledge skills
    core_world = models.PositiveSmallIntegerField(default=0, verbose_name=_("mondes du noyau"))
    education = models.PositiveSmallIntegerField(default=0, verbose_name=_("education"))
    lore = models.PositiveSmallIntegerField(default=0, verbose_name=_("culture"))
    outer_rim = models.PositiveSmallIntegerField(default=0, verbose_name=_("bordure exterieure"))
    underworld = models.PositiveSmallIntegerField(default=0, verbose_name=_("pègre"))
    xenology = models.PositiveSmallIntegerField(default=0, verbose_name=_("xénologie"))

    class Meta:
        abstract = True


class Character(NamedModel, Statistics):
    campaign = models.ForeignKey(
        'Campaign', blank=True, null=True, on_delete=models.SET_NULL,
        related_name='characters', verbose_name=_("campagne"))
    player = models.ForeignKey(
        'Player', blank=True, null=True, on_delete=models.SET_NULL,
        related_name='characters', verbose_name=_("joueur"))

    type = models.CharField(max_length=10, choices=CHARACTER_TYPES, verbose_name=_("type"))
    species = models.CharField(max_length=20, choices=SPECIES, verbose_name=_("espèce"))

    # Combat
    initiative = models.PositiveSmallIntegerField(default=0, verbose_name=_("initiative"))
    is_active = models.BooleanField(default=False, verbose_name=_("personnage actif ?"))
    is_fighting = models.BooleanField(default=False, verbose_name=_("en combat ?"))
    actual_health = models.PositiveSmallIntegerField(default=0, verbose_name=_("santé actuelle"))
    actual_strain = models.PositiveSmallIntegerField(default=0, verbose_name=_("stress actuel"))
    critical_wounds = models.PositiveSmallIntegerField(default=0, verbose_name=_("blessures critiques"))

    # Position State - Direct combat dice modifiers
    # Aiming => + 1 fortune dice on the character's ranged attack
    aiming = models.BooleanField(default=False, verbose_name=_("visée"))
    # Undercover => +1 misfortune dice on ranged attack targeting the character
    undercover = models.BooleanField(default=False, verbose_name=_("sous couverture"))
    # Guarded stance => +1 misfortune dice on character's attack and melee attack targeting the character
    guarded_stance = models.BooleanField(default=False, verbose_name=_("en garde"))
    # Dropped prone +1 misfortune dice on ranged attack and +1 fortune dice on melee attack targeting the character
    dropped_prone = models.BooleanField(default=False, verbose_name=_("au sol"))

    # Experience / Misc
    actual_experience = models.PositiveSmallIntegerField(default=0, verbose_name=_("experience actuelle"))
    total_experience = models.PositiveIntegerField(default=0, verbose_name=_("experience totale"))
    money = models.PositiveSmallIntegerField(default=0, verbose_name=_("crédits"))

    def _get_attribute_modifier(self, attribute_name):
        """
        Get the total value of an attribute modifiers
        :param stat_name: attribute
        :return: modifiers value
        """
        stat_modifiers = self.applied_effects.filter(effect__type=EFFECT_ATTRIBUTE_MODIFIER, effect__attribute=attribute_name)
        return stat_modifiers.aggregate(Sum('modifier_value')).get('modifier_value__sum') or 0

    @property
    def is_conscious(self):
        return self.actual_health > 0 and self.actual_strain > 0

    @property
    def defense(self):
        """
        Armor + talent
        :return: defense value
        """
        defense_value = self.inventory.filter(
            equiped=True, item__type=ITEM_ARMOR).aggregate(Sum('item__defense')).get('item__defense__sum') or 0
        defense_value += self._get_attribute_modifier(ATTRIBUTE_DEFENSE)
        return defense_value

    @property
    def max_health(self):
        """
        Brawn + species ability + talent
        :return: max_health value
        """
        max_health_value = self.stats.get(STAT_BRAWN)
        if self.type == CHARACTER_TYPE_PC:
            max_health_value += SPECIES_ABILITIES.get(self.species, {}).get('max_health', 10)
        max_health_value += self._get_attribute_modifier(ATTRIBUTE_MAX_HEALTH)
        return max_health_value

    @property
    def max_strain(self):
        """
        Willpower + species ability + talent
        :return: max_health value
        """
        max_strain_value = self.stats.get(STAT_WILLPOWER)
        if self.type == CHARACTER_TYPE_PC:
            max_strain_value += SPECIES_ABILITIES.get(self.species, {}).get('max_strain', 10)
        max_strain_value += self._get_attribute_modifier(ATTRIBUTE_MAX_STRAIN)
        return max_strain_value

    @property
    def max_charge(self):
        """
        Brawn + 5
        :return: max weigth value
        """
        return 5 + self.stats.get(STAT_BRAWN)

    @property
    def actual_charge(self):
        return self.inventory.annotate(
            total_item_weight=F('item__weight') * F('quantity')).aggregate(
            Sum('total_item_weight', output_field=FloatField())).get('total_item_weight__sum') or 0

    @property
    def is_overloaded(self):
        return self.actual_charge > self.max_charge

    @property
    def soak_value(self):
        """
        Brawn + armor + talent
        :return: soak_value
        """
        soak_value = self.stats.get(STAT_BRAWN)
        soak_value += self.inventory.filter(
            equiped=True, item__type=ITEM_ARMOR).aggregate(Sum('item__soak_value')).get('item__soak_value__sum') or 0
        soak_value += self._get_attribute_modifier(ATTRIBUTE_SOAK_VALUE)
        return soak_value

    @property
    def stats(self):
        """
        Get all the stats values with potential modifiers
        :return: dict (stat_name: final value)
        """
        stats = {}
        for stat_name in DICT_STATS.keys():
            stat_value = getattr(self, stat_name, 0)
            stat_value += self._get_attribute_modifier(stat_name)
            if self.type != CHARACTER_TYPE_NEMESIS:
                stat_value = min(stat_value, 5)
            stats[stat_name] = max(stat_value, 0)
        return stats

    @property
    def skills(self):
        """
        Get all the skills values with potential modifiers
        :return: dict (skill_name: final value)
        """
        skills = {}
        for skill_name in DICT_SKILLS.keys():
            skill_value = getattr(self, skill_name, 0)
            skill_value += self._get_attribute_modifier(skill_name)
            if self.type != CHARACTER_TYPE_NEMESIS:
                skill_value = min(skill_value, 5)
            skills[skill_name] = max(skill_value, 0)
        return skills

    def get_skill_dice(self, skill_name, dice_upgrades=0, target=None, opposite=False):
        """
        Get the aptitude/difficulty and mastery/challenge dice pool for a skill name
        :param skill_name: skill name
        :param upgrade_numbers: number of dice to upgrade
        :param opposite: opposite test ? change the aptitude/mastery dice to difficulty/challenge
        :return: dict of dice pool
        """
        skill_value = self.skills.get(skill_name, 0)
        for stat_name, skills in SKILL_DEPENDANCIES.items():
            if skill_name in skills:
                stat_value = self.stats.get(stat_name, 0)
                break
        else:
            stat_value = 0
        mastery_dice = min(skill_value, stat_value)
        aptitude_dice = max(skill_value, stat_value) - mastery_dice
        # Upgrade dice -> transform aptitude dice into mastery dice or add aptitude dice
        if dice_upgrades:
            for i in range(dice_upgrades):
                if aptitude_dice:
                    aptitude_dice -= 1
                    mastery_dice += 1
                else:
                    aptitude_dice += 1
        result = {
            'aptitude' if not opposite else 'difficulty': aptitude_dice,
            'mastery' if not opposite else 'challenge': mastery_dice
        }

        # Dice modifier effects
        dice_filter = dict(effect__type=EFFECT_DICE_POOL_MODIFIER, effect__attribute=skill_name)
        dice_effects = self.applied_effects.filter(**dice_filter, effect__opposite_test=False)

        # Opposite Modifiers - Effect affecting a test on the target character
        if target:
            target_dice_effects = CharacterEffect.objects.filter(
                **dice_filter, target=target, effect__opposite_test=True)
            dice_effects = dice_effects.union(target_dice_effects)
        for dice_type, number in dice_effects.values_list('effect__dice', 'modifier_value'):
            result[dice_type] = max(result.get(dice_type, 0) + number, 0)

        return result

    def modify_health(self, value, save=False):
        """
        Remove health
        :return:
        """
        health = self.actual_health + value
        self.actual_health = max(min(health, self.max_health), 0)
        if save:
            self.save(update_fields=["actual_health"])

    def modify_strain(self, value, save=False):
        """
        Remove strain
        :return:
        """
        strain = self.actual_strain + value
        self.actual_strain = max(min(strain, self.max_strain), 0)
        if save:
            self.save(update_fields=["actual_strain"])

    def start_combat_turn(self):
        self.is_active = True
        self.save()

    def end_combat_turn(self):
        self.is_active = False
        # Decrease turn duration or remove effects with turn duration
        queryset = CharacterEffect.objects.filter(
            Q(Q(duration_type=EFFECT_DURATION_SOURCE_TURN, source_character_id=self.id) | Q(
                duration_type=EFFECT_DURATION_TARGET_TURN, target_id=self.id)))

        # Apply health/strain modifiers effects
        for effect in queryset.filter(effect__type__in=[EFFECT_HEALTH_MODIFIER, EFFECT_STRAIN_MODIFIER]):
            effect.apply_direct_modifier(self if effect.target_id == self.id else effect.target)

        queryset.filter(nb_turn=1).delete()
        queryset.update(nb_turn=F('nb_turn') - 1)
        self.save()

    def end_fight(self):
        self.is_fighting = False
        # Recover strain
        recovered_strain = max(self.stats.get(STAT_PRESENCE), self.skills.get(COOL))
        self.modify_strain(value=recovered_strain)
        self.save()

    def rest(self):
        self.actual_strain = self.max_strain
        self.modify_health(value=1)
        self.save()

    # Tests
    def attack(self, target, equipment_id=None, upgrade=0, **bonus_dice):
        pass

    def opposite_skill_test(self, skill_name, target, opposite_skill='', check_destiny=True,
                            dice_upgrades=0, **bonus_dice):
        # Destiny upgrade ?
        if check_destiny and self.campaign.get_destiny_upgrade(self):
            dice_upgrades += 1
        dice_pool = self.get_skill_dice(skill_name, target=target, dice_upgrades=dice_upgrades)

        # Opposite test
        # Destiny upgrade ?
        target_dice_upgrades = 1 if check_destiny and self.campaign.get_destiny_upgrade(target) else 0
        opposite_skill = opposite_skill or skill_name
        dice_pool.update(target.get_skill_dice(opposite_skill, opposite=True, dice_upgrades=target_dice_upgrades))

        for dice_type, value in bonus_dice.items():
            dice_pool[dice_type] = dice_pool.get(dice_type, 0) + value

        return {
            'dice_pool': dice_pool,
            'result': roll_dice(**dice_pool)
        }

    def skill_test(self, skill_name, difficulty=DIFFICULTY_SIMPLE, challenge=0, dice_upgrades=0, **bonus_dice):
        has_difficulty = difficulty or challenge
        # Destiny upgrade ?
        if has_difficulty and self.campaign.get_destiny_upgrade(self):
            dice_upgrades += 1
        dice_pool = self.get_skill_dice(skill_name, dice_upgrades=dice_upgrades)

        # Upgrade difficulty dice into challenge dice if destiny_upgrade is True
        if has_difficulty and self.campaign.get_destiny_upgrade(self, opposite=True):
            if difficulty:
                difficulty -= 1
                challenge += 1
            else:
                difficulty += 1
        dice_pool.update({
            DICE_TYPE_DIFFICULTY: difficulty,
            DICE_TYPE_CHALLENGE: challenge
        })

        for dice_type, value in bonus_dice.items():
            dice_pool[dice_type] = dice_pool.get(dice_type, 0) + value

        return {
            'dice_pool': dice_pool,
            'result': roll_dice(**dice_pool)
        }

    def __str__(self):
        return f'{self.name} - {self.get_species_display()} - ({self.player or self.get_type_display()})'

    class Meta:
        verbose_name = _("personnage")
        verbose_name_plural = _("personnages")


class Effect(NamedModel):
    type = models.CharField(max_length=20, choices=EFFECT_TYPES, verbose_name=_("type"))
    # Modifier
    attribute = models.CharField(max_length=15, choices=ATTRIBUTES, blank=True, verbose_name=_("attribut modifié"))
    dice = models.CharField(max_length=10, choices=DICE_TYPES, blank=True, verbose_name=_("dé modifié"))
    opposite_test = models.BooleanField(default=False, verbose_name=_("effet sur un test en opposition ?"))

    class Meta:
        verbose_name = _("effet")
        verbose_name_plural = _("effets")


class Talent(NamedModel):
    # Activation
    activation_type = models.CharField(max_length=7, choices=ACTIVATION_TYPES, default=ACTIVATION_TYPE_PASSIVE,
                                       verbose_name=_("type d'activation"))

    class Meta:
        verbose_name = _("talent")
        verbose_name_plural = _("talents")


class EffectModifier(models.Model):
    effect = models.ForeignKey('Effect', on_delete=models.CASCADE, related_name='+', verbose_name=_("effet"))
    # Modifier
    modifier_value = models.IntegerField(default=0, verbose_name=_("valeur du modificateur"))
    # Activation
    activation_type = models.CharField(max_length=7, choices=ACTIVATION_TYPES, default=ACTIVATION_TYPE_PASSIVE,
                                       verbose_name=_("type d'activation"))
    # Duration
    duration_type = models.CharField(max_length=11, choices=EFFECT_DURATIONS, blank=True, verbose_name=_("type de durée"))
    nb_turn = models.IntegerField(default=0, verbose_name=_("nombre de tours"))

    def apply(self, targets, source_character_id=None, source_equipment_id=None, source_item_id=None, source_talent_id=None):
        """
        Apply the effect on the targets
        :param targets: targets
        :param source_character_id: id of the source character
        :param source_equipment_id: id of the source equipment
        :param source_talent_id: id of the source talent
        :return: None
        """
        for target in targets:
            if self.duration_type == EFFECT_DURATION_DIRECT:
                # Direct health/strain modifier
                self.apply_direct_modifier(target)
            else:
                CharacterEffect.objects.create(
                    target_id=target.id,
                    source_character_id=source_character_id,
                    source_equipment_id=source_equipment_id,
                    source_item_id=source_item_id,
                    source_talent_id=source_talent_id,
                    effect=self.effect,
                    modifier_value=self.modifier_value,
                    activation_type=self.activation_type,
                    duration_type=self.duration_type,
                    nb_turn=self.nb_turn
                )

    def apply_direct_modifier(self, target):
        """
        Apply a direct effect modifier on the target (health or strain)
        :param target: target
        :return: None
        """
        if self.effect.type == EFFECT_HEALTH_MODIFIER:
            target.modify_health(self.modifier_value, save=True)
        elif self.effect.type == EFFECT_STRAIN_MODIFIER:
            target.modify_strain(self.modifier_value, save=True)

    def __str__(self):
        return f'{self.effect} - valeur: {self.modifier_value} - nombres de tours: {self.nb_turn}'

    class Meta:
        abstract = True


class ItemEffect(EffectModifier):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='effects', verbose_name=_("objet"))

    class Meta:
        verbose_name = _("effet d'objet")
        verbose_name_plural = _("effets d'objet")


class TalentEffect(EffectModifier):
    talent = models.ForeignKey('Talent', on_delete=models.CASCADE, related_name='effects', verbose_name=_("talent"))

    class Meta:
        verbose_name = _("effet de talent")
        verbose_name_plural = _("effets de talents")


class CharacterEffect(EffectModifier):
    # Source
    source_character = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='generated_effects',
                                         verbose_name=_("personnage source"))
    source_equipment = models.ForeignKey('Equipment', on_delete=models.SET_NULL, blank=True, null=True,
                                         related_name='generated_effects',
                                         verbose_name=_("equipement source"))
    source_item = models.ForeignKey('Item', on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='generated_effects',
                                    verbose_name=_("objet source"))
    source_talent = models.ForeignKey('Talent', on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='generated_effects',
                                      verbose_name=_("talent source"))
    target = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='applied_effects',
                               verbose_name=_("personnage cible"))

    def __str__(self):
        return f'cible: {self.target} / effet: {self.effect}'

    class Meta:
        verbose_name = _("effet de personnages")
        verbose_name_plural = _("effets de personnages")


class Item(NamedModel):
    type = models.CharField(max_length=10, choices=ITEM_TYPES, verbose_name=_("type"))
    weight = models.FloatField(default=0.0, verbose_name=_("encombrement"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("prix"))
    hard_point = models.PositiveIntegerField(default=0, verbose_name=_("emplacement d'améliorations"))
    skill = models.CharField(max_length=10, choices=ITEM_SKILLS, blank=True, null=True, verbose_name=_("compétence associée"))

    # Weapon Specific
    range = models.CharField(max_length=10, choices=RANGE_BANDS, blank=True, verbose_name=_("portée"))
    damage = models.PositiveSmallIntegerField(default=0, verbose_name=_("dégats"))
    critique = models.PositiveSmallIntegerField(default=0, verbose_name=_("critique"))

    # Armor Specific
    soak_value = models.PositiveSmallIntegerField(default=0, verbose_name=_("valeur d'encaissement"))
    defense = models.PositiveSmallIntegerField(default=0, verbose_name=_("défense"))

    @property
    def is_equipable(self):
        """
        Objet équipable ?
        """
        return self.type in (ITEM_WEAPON, ITEM_ARMOR)

    def add_to_inventory(self, character_id, quantity=1):
        """
        Add the item in the character's inventory
        :param character_id: character's id
        :param quantity: quantity of the item to add in the character's inventory
        :return: None
        """
        # Add quantity if the same item is already in the character's inventory, else create the equipment
        if not Equipment.objects.filter(
                character_id=character_id, item_id=self.id).update(quantity=F('quantity') + quantity):
            Equipment.objects.create(character_id=character_id, item_id=self.id, quantity=quantity)

    class Meta:
        verbose_name = _("objet")
        verbose_name_plural = _("objets")


class Equipment(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='inventory', verbose_name=_("personnage"))
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='+', verbose_name=_("objet"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("quantité"))
    equiped = models.BooleanField(default=False, verbose_name=_("équipé ?"))

    def equip(self):
        self.equiped = True
        # Passive effects activation
        for effect in self.item.effects.filter(activation_type=ACTIVATION_TYPE_PASSIVE).all():
            effect.apply(targets=[self.character], source_equipment_id=self.id, source_character_id=self.character_id)
        self.save()

    def unequip(self):
        self.equiped = False
        CharacterEffect.objects.filter(activation_type=ACTIVATION_TYPE_PASSIVE, source_equipment__id=self.id).delete()
        self.save()

    def use_consumable(self, targets_ids):
        """
        Use consumable (medipack/grenade/..)
        :param targets_ids: ids of the targets
        :return: None
        """
        targets = Character.objects.filter(id__in=targets_ids)
        for effect in self.item.effects.all():
            effect.apply(targets, source_character_id=self.character_id, source_item_id=self.item_id)
        # Remove consumable from inventory
        if self.quantity == 1:
            self.delete()
        else:
            self.quantity -= 1
            self.save()

    def __str__(self):
        return f'objet: {self.item} / personnage: {self.character} / quantité: {self.quantity} / Equipé: {self.equiped}'

    class Meta:
        verbose_name = _("équipement")
        verbose_name_plural = _("équipements")


ALL_MODELS = (
    Player,
    Campaign,
    Character,
    CharacterEffect,
    Effect,
    Item,
    ItemEffect,
    Equipment,
    Talent,
    TalentEffect
)
