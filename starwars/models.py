from itertools import cycle

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from starwars.enums import (
    SKILL_DEPENDANCIES, SPECIES, SPECIES_ABILITIES, ITEM_TYPES, ITEM_WEAPON, ITEM_ARMOR, RANGE_BANDS, ITEM_SKILLS,
    EFFECT_ATTRIBUTE_MODIFIER, ATTRIBUTE_MAX_HEALTH, ATTRIBUTE_MAX_STRAIN, ATTRIBUTE_DEFENSE, ATTRIBUTE_SOAK_VALUE,
    DICT_STATS, DICT_SKILLS, STAT_BRAWN, STAT_WILLPOWER, EFFECT_TYPES, DICE_TYPES, ATTRIBUTES, CHARACTER_TYPES,
    STAT_PRESENCE, COOL, CHARACTER_TYPE_PC, DICE_LIGHT_FORCE, DICE_DARK_FORCE, VIGILANCE, DICE_TRIUMPH, DICE_ADVANTAGE)
from starwars.utils import roll_dice


class Player(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True, verbose_name=_("surnom"))

    def __str__(self):
        return self.nickname or self.first_name or self.username

    class Meta:
        verbose_name = _("joueur")
        verbose_name_plural = _("joueurs")


class Campaign(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("nom"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    light_tokens = models.PositiveSmallIntegerField(default=0, verbose_name=_("light token"))
    dark_tokens = models.PositiveSmallIntegerField(default=0, verbose_name=_("dark token"))

    def set_destiny_tokens(self):
        """
        Roll a force die for each playable characters, light/dark results stands for destiny tokens
        :return: None
        """
        forces_dice_result = roll_dice(force=self.characters.filter(type=CHARACTER_TYPE_PC).count())
        self.light_tokens = forces_dice_result.get(DICE_LIGHT_FORCE)
        self.dark_tokens = forces_dice_result.get(DICE_DARK_FORCE)

    def use_light_token(self):
        self.light_tokens -= 1
        self.dark_tokens += 1
        self.save()

    def use_dark_token(self):
        self.dark_tokens -= 1
        self.light_tokens += 1
        self.save()

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
        fighting_characters = self.characters.filter(is_fighting=True, actual_health__gt=0, actual_strain__gt=0)
        active_character_turn_ended = False
        next_character = None
        for character in cycle(fighting_characters.order_by('-initiative')):
            if character.is_active:
                character.end_combat_turn()
                active_character_turn_ended = True
                continue
            if not active_character_turn_ended:
                continue
            character.start_combat_turn()
            next_character = character
            break
        return next_character

    def end_fight(self):
        for character in self.characters.filter(is_fighting=True):
            character.end_fight()

    def __str__(self):
        return self.name

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

    def _get_attribute_modifier(self, attribute_name):
        """
        Get the total value of an attribute modifiers
        :param stat_name: attribute
        :return: modifiers value
        """
        stat_modifiers = self.effects.filter(type=EFFECT_ATTRIBUTE_MODIFIER, attribute=attribute_name)
        return sum(stat_modifiers.values_list('modifier_value', flat=True))

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
            skills[skill_name] = max(skill_value, 0)
        return skills

    def get_skill_dice(self, skill_name, dice_upgrades=0, opposite=False):
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
        return {
            'aptitude' if not opposite else 'difficulty': aptitude_dice,
            'mastery' if not opposite else 'challenge': mastery_dice
        }

    class Meta:
        abstract = True


class Character(Statistics):
    campaign = models.ForeignKey(
        'Campaign', blank=True, null=True, on_delete=models.SET_NULL,
        related_name='characters', verbose_name=_("campagne"))
    player = models.ForeignKey(
        'Player', blank=True, null=True, on_delete=models.SET_NULL,
        related_name='characters', verbose_name=_("joueur"))

    name = models.CharField(max_length=50, verbose_name=_("nom"))
    description = models.TextField(blank=True, verbose_name=_("description"))
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
    # Stunned - if 0: the character is active, else, decrease the "stunned" value each combat turn
    stunned = models.PositiveSmallIntegerField(default=0, verbose_name=_("étourdi(e) (nombres de tours)"))

    # Experience
    actual_experience = models.PositiveSmallIntegerField(default=0)
    total_experience = models.PositiveIntegerField(default=0)

    @property
    def defense(self):
        """
        Armor + talent
        :return: defense value
        """
        defense_value = sum(self.equipments.filter(equiped=True, item__type=ITEM_ARMOR).values_list('item__defense', flat=True))
        defense_value += self._get_attribute_modifier(ATTRIBUTE_DEFENSE)
        return defense_value

    @property
    def max_health(self):
        """
        Brawn + species ability + talent
        :return: max_health value
        """
        max_health_value = self.stats.get(STAT_BRAWN) + SPECIES_ABILITIES.get(self.species, {}).get('max_health', 10)
        max_health_value += self._get_attribute_modifier(ATTRIBUTE_MAX_HEALTH)
        return max_health_value

    @property
    def max_strain(self):
        """
        Willpower + species ability + talent
        :return: max_health value
        """
        max_strain_value = self.stats.get(STAT_WILLPOWER) + SPECIES_ABILITIES.get(self.species, {}).get('max_strain', 10)
        max_strain_value += self._get_attribute_modifier(ATTRIBUTE_MAX_STRAIN)
        return max_strain_value

    @property
    def max_weight(self):
        """
        Brawn + 5
        :return: max weigth value
        """
        return 5 + self.stats.get(STAT_BRAWN)

    @property
    def soak_value(self):
        """
        Brawn + armor + talent
        :return: soak_value
        """
        soak_value = self.stats.get(STAT_BRAWN)
        soak_value += sum(self.equipments.filter(equiped=True, item__type=ITEM_ARMOR).values_list('item__soak_value', flat=True))
        soak_value += self._get_attribute_modifier(ATTRIBUTE_SOAK_VALUE)
        return soak_value

    def modify_health(self, value, save=False):
        """
        Remove health
        :return:
        """
        health = self.actual_health + value
        self.actual_health = max(min(health, self.max_health), 0)
        if save:
            self.save()

    def modify_strain(self, value, save=False):
        """
        Remove strain
        :return:
        """
        strain = self.actual_strain + value
        self.actual_strain = max(min(strain, self.max_strain), 0)
        if save:
            self.save()

    def start_combat_turn(self):
        self.is_active = True
        self.save()

    def end_combat_turn(self):
        if self.stunned:
            self.stunned -= 1
        self.is_active = False
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

    def __str__(self):
        return f'{self.name} ({self.player or self.get_type_display()})'

    class Meta:
        verbose_name = _("personnage")
        verbose_name_plural = _("personnages")


class Effect(models.Model):
    source_character = models.ForeignKey('Character', on_delete=models.CASCADE, blank=True, null=True, related_name='+', verbose_name=_("personnage source"))
    target = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='effects', verbose_name=_("personnage cible"))
    type = models.CharField(max_length=20, choices=EFFECT_TYPES, verbose_name=_("type"))
    attribute = models.CharField(max_length=15, choices=ATTRIBUTES, blank=True, verbose_name=_("attribut modifié"))
    dice = models.CharField(max_length=10, choices=DICE_TYPES, blank=True, verbose_name=_("dé modifié"))
    modifier_value = models.IntegerField(default=0, verbose_name=_("valeur du modificateur"))

    class Meta:
        verbose_name = _("effet")
        verbose_name_plural = _("effets")


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("nom"))
    description = models.TextField(blank=True, verbose_name=_("description"))
    type = models.CharField(max_length=10, choices=ITEM_TYPES, verbose_name=_("type"))
    weigth = models.FloatField(default=0.0, verbose_name=_("encombrement"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("prix"))
    hard_point = models.PositiveIntegerField(default=0, verbose_name=_("emplacement d'améliorations"))
    skill = models.CharField(max_length=10, choices=ITEM_SKILLS, verbose_name=_("compétence associée"))

    # Weapon Specific
    range = models.CharField(max_length=10, choices=RANGE_BANDS, blank=True, verbose_name=_("portée"))
    damage = models.PositiveSmallIntegerField(default=0, verbose_name=_("dégats"))
    critique = models.PositiveSmallIntegerField(default=0, verbose_name=_("critique"))
    # TODO: specials (Effect ?)

    # Armor Specific
    soak_value = models.PositiveSmallIntegerField(default=0, verbose_name=_("valeur d'encaissement"))
    defense = models.PositiveSmallIntegerField(default=0, verbose_name=_("défense"))

    @property
    def is_equipable(self):
        """
        Objet équipable ?
        """
        return self.type in (ITEM_WEAPON, ITEM_ARMOR)

    class Meta:
        verbose_name = _("objet")
        verbose_name_plural = _("objets")


class Equipment(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='equipments', verbose_name=_("personnage"))
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='+', verbose_name=_("objet"))
    # TODO: Améliorations (Items ?)
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("quantité"))
    equiped = models.BooleanField(default=False, verbose_name=_("équipé ?"))


ALL_MODELS = (
    Player,
    Campaign,
    Character,
    Effect,
    Item,
    Equipment
)
