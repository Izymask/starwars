from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from starwars.enums import SKILL_DEPENDANCIES, SPECIES, SPECIES_ABILITIES


class Player(AbstractUser):
    nickname = models.CharField(max_length=100, blank=True, verbose_name=_("surnom"))

    def __str__(self):
        return self.nickname or self.first_name or self.username

    class Meta:
        verbose_name = _("joueur")
        verbose_name_plural = _("joueurs")


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

    def get_skill_dice(self, skill_name, dice_upgrades=0, opposite=False):
        """
        Get the aptitude/difficulty and mastery/challenge dice pool for a skill name
        :param skill_name: skill name
        :param upgrade_numbers: number of dice to upgrade
        :param opposite: opposite test ? change the aptitude/mastery dice to difficulty/challenge
        :return: dict of dice pool
        """
        skill_value = getattr(self, skill_name, 0)
        for stat_name, skills in SKILL_DEPENDANCIES.items():
            if skill_name in skills:
                stat_value = getattr(self, stat_name, 0)
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
    total_experience = models.PositiveIntegerField(default=0)
    actual_experience = models.PositiveSmallIntegerField(default=0)

    @property
    def max_health(self):
        """
        Brawn + species ability + talent
        :return: max_health value
        """
        max_health_value = self.brawn + SPECIES_ABILITIES.get(self.species, {}).get('max_health', 10)
        # TODO: add talent
        return max_health_value

    @property
    def max_strain(self):
        """
        Willpower + species ability + talent
        :return: max_health value
        """
        max_strain_value = self.willpower + SPECIES_ABILITIES.get(self.species, {}).get('max_strain', 10)
        # TODO: add talent
        return max_strain_value

    @property
    def soak_value(self):
        """
        Brawn + armor + talent
        :return: soak_value
        """
        soak_value = self.brawn
        # TODO: add armor/talent
        return soak_value

    class Meta:
        verbose_name = _("personnage")
        verbose_name_plural = _("personnages")
