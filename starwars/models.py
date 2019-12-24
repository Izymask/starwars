from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from starwars.enums import SKILL_DEPENDANCIES, SPECIES, SPECIES_ABILITIES, ITEM_TYPES, ITEM_WEAPON, ITEM_ARMOR, \
    RANGE_BANDS, ITEM_SKILLS, DICT_STATS, DICT_SKILLS, STAT_BRAWN, STAT_WILLPOWER


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

    def _get_skill_modifier(self, skill_name):
        """
        Get the total value of a skill modifiers
        :param skill_name: skill_name
        :return: modifiers value
        """
        # TODO: add effects
        return 0

    def _get_stat_modifier(self, stat_name):
        """
        Get the total value of a statistic modifiers
        :param stat_name: stat_name
        :return: modifiers value
        """
        # TODO: add effects
        return 0

    @property
    def stats(self):
        """
        Get all the stats values with potential modifiers
        :return: dict (stat_name: final value)
        """
        stats = {}
        for stat_name in DICT_STATS.keys():
            stat_value = getattr(self, stat_name, 0)
            stat_value += self._get_stat_modifier(stat_name)
            stats[stat_name] = stat_value
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
            skill_value += self._get_skill_modifier(skill_name)
            skills[skill_name] = skill_value
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
    player = models.ForeignKey(
        'Player', blank=True, null=True, on_delete=models.SET_NULL,
        related_name='characters', verbose_name=_("joueur"))

    name = models.CharField(max_length=50, verbose_name=_("nom"))
    species = models.CharField(max_length=20, choices=SPECIES, verbose_name=_("espèce"))

    # Combat
    actual_health = models.PositiveSmallIntegerField(default=0, verbose_name=_("santé actuelle"))
    actual_strain = models.PositiveSmallIntegerField(default=0, verbose_name=_("stress actuel"))
    critical_wounds = models.PositiveSmallIntegerField(default=0, verbose_name=_("blessures critiques"))

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
        # TODO: add talent
        return defense_value

    @property
    def max_health(self):
        """
        Brawn + species ability + talent
        :return: max_health value
        """
        max_health_value = self.stats.get(STAT_BRAWN) + SPECIES_ABILITIES.get(self.species, {}).get('max_health', 10)
        # TODO: add talent
        return max_health_value

    @property
    def max_strain(self):
        """
        Willpower + species ability + talent
        :return: max_health value
        """
        max_strain_value = self.stats.get(STAT_WILLPOWER) + SPECIES_ABILITIES.get(self.species, {}).get('max_strain', 10)
        # TODO: add talent
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
        # TODO: add talent
        return soak_value

    class Meta:
        verbose_name = _("personnage")
        verbose_name_plural = _("personnages")


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
