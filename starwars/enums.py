from django.utils.translation import gettext_lazy as _


# Dice
# Dice types
DICE_TYPE_FORTUNE = 'fortune'
DICE_TYPE_MISFORTUNE = 'misfortune'
DICE_TYPE_APTITUDE = 'aptitude'
DICE_TYPE_DIFFICULTY = 'difficulty'
DICE_TYPE_MASTERY = 'mastery'
DICE_TYPE_CHALLENGE = 'challenge'
DICE_TYPE_FORCE = 'force'

# Dice values
DICE_SUCCESS = 'success'
DICE_FAILURE = 'failure'
DICE_ADVANTAGE = 'advantage'
DICE_THREAT = 'threat'
DICE_TRIUMPH = 'triumph'
DICE_DISASTER = 'disaster'
DICE_DARK_FORCE = 'dark_force'
DICE_LIGHT_FORCE = 'light_force'

DICE = {
    DICE_TYPE_FORTUNE: {
        0: None, 1: None,
        2: {DICE_SUCCESS: 1},
        3: {DICE_SUCCESS: 1, DICE_ADVANTAGE: 1},
        4: {DICE_ADVANTAGE: 2},
        5: {DICE_ADVANTAGE: 1}
    },
    DICE_TYPE_MISFORTUNE: {
        0: None, 1: None,
        2: {DICE_FAILURE: 1},
        3: {DICE_FAILURE: 1},
        4: {DICE_THREAT: 1},
        5: {DICE_THREAT: 1}
    },
    DICE_TYPE_APTITUDE: {
        0: None,
        1: {DICE_SUCCESS: 1},
        2: {DICE_SUCCESS: 1},
        3: {DICE_SUCCESS: 2},
        4: {DICE_ADVANTAGE: 1},
        5: {DICE_ADVANTAGE: 1},
        6: {DICE_SUCCESS: 1, DICE_ADVANTAGE: 1},
        7: {DICE_ADVANTAGE: 2}
    },
    DICE_TYPE_DIFFICULTY: {
        0: None,
        1: {DICE_FAILURE: 1},
        2: {DICE_FAILURE: 2},
        3: {DICE_THREAT: 1},
        4: {DICE_THREAT: 1},
        5: {DICE_THREAT: 1},
        6: {DICE_THREAT: 2},
        7: {DICE_FAILURE: 1, DICE_THREAT: 1}
    },
    DICE_TYPE_MASTERY: {
        0: None,
        1: {DICE_SUCCESS: 1},
        2: {DICE_SUCCESS: 1},
        3: {DICE_SUCCESS: 2},
        4: {DICE_SUCCESS: 2},
        5: {DICE_ADVANTAGE: 1},
        6: {DICE_SUCCESS: 1, DICE_ADVANTAGE: 1},
        7: {DICE_SUCCESS: 1, DICE_ADVANTAGE: 1},
        8: {DICE_SUCCESS: 1, DICE_ADVANTAGE: 1},
        9: {DICE_ADVANTAGE: 2},
        10: {DICE_ADVANTAGE: 2},
        11: {DICE_TRIUMPH: 1}
    },
    DICE_TYPE_CHALLENGE: {
        0: None,
        1: {DICE_FAILURE: 1},
        2: {DICE_FAILURE: 1},
        3: {DICE_FAILURE: 2},
        4: {DICE_FAILURE: 2},
        5: {DICE_THREAT: 1},
        6: {DICE_THREAT: 1},
        7: {DICE_FAILURE: 1, DICE_THREAT: 1},
        8: {DICE_FAILURE: 1, DICE_THREAT: 1},
        9: {DICE_THREAT: 2},
        10: {DICE_THREAT: 2},
        11: {DICE_DISASTER: 1}
    },
    DICE_TYPE_FORCE: {
        0: {DICE_DARK_FORCE: 1},
        1: {DICE_DARK_FORCE: 1},
        2: {DICE_DARK_FORCE: 1},
        3: {DICE_DARK_FORCE: 1},
        4: {DICE_DARK_FORCE: 1},
        5: {DICE_DARK_FORCE: 1},
        6: {DICE_DARK_FORCE: 2},
        7: {DICE_LIGHT_FORCE: 1},
        8: {DICE_LIGHT_FORCE: 1},
        9: {DICE_LIGHT_FORCE: 2},
        10: {DICE_LIGHT_FORCE: 2},
        11: {DICE_LIGHT_FORCE: 2}
    }
}

# ITEM TYPES
ITEM_WEAPON = 'weapon'
ITEM_ARMOR = 'armor'
ITEM_CONSUMABLE = 'consumable'
ITEM_MOD = 'mod'
ITEM_MISC = 'misc'
ITEM_TYPES = (
    (ITEM_WEAPON, _("arme")),
    (ITEM_ARMOR, _("armure")),
    (ITEM_CONSUMABLE, _("consommable")),
    (ITEM_MOD, _("amelioration")),
    (ITEM_MISC, _("autre")),
)


# RANGE BANDS
RANGE_ENGAGED = 'engaged'
RANGE_SHORT = 'short'
RANGE_MEDIUM = 'medium'
RANGE_LONG = 'long'
RANGE_EXTREME = 'extreme'
RANGE_BANDS = (
    (RANGE_ENGAGED, _("corps à corps")),
    (RANGE_SHORT, _("portée courte")),
    (RANGE_MEDIUM, _("portée moyenne")),
    (RANGE_LONG, _("portée longue")),
    (RANGE_EXTREME, _("portée extrème")),
)


# Stats
STAT_AGILITY = 'agility'
STAT_CUNNING = 'cunning'
STAT_BRAWN = 'brawn'
STAT_INTELLECT = 'intellect'
STAT_PRESENCE = 'presence'
STAT_WILLPOWER = 'willpower'


# Skills
ATHLETICS = 'athletics'
ASTROGATION = 'astrogation'
BRAWL = 'brawl'
CHARM = 'charm'
COERCION = 'coercion'
COMPUTERS = 'computers'
COOL = 'cool'
COORDINATION = 'coordination'
CORE_WORLD = 'core_world'
DECEPTION = 'deception'
DISCIPLINE = 'discipline'
EDUCATION = 'education'
GUNNERY = 'gunnery'
LEADERSHIP = 'leadership'
LIGHTSABER = 'lightsaber'
LORE = 'lore'
MECHANICS = 'mechanics'
MEDECINE = 'medecine'
MELEE = 'melee'
NEGOCIATION = 'negociation'
OUTER_RIM = 'outer_rim'
PERCEPTION = 'perception'
PILOTING = 'piloting'
RANGED_HEAVY = 'ranged_heavy'
RANGED_LIGHT = 'ranged_light'
RESILIENCE = 'resilience'
SKULDUGGERY = 'skulduggery'
STEALTH = 'stealth'
STREETWISE = 'streetwise'
SURVIVAL = 'survival'
UNDERWORLD = 'underworld'
VIGILANCE = 'vigilance'
XENOLOGY = 'xenology'

ITEM_SKILLS = (
    (BRAWL, _("méléé")),
    (GUNNERY, _("artillerie")),
    (LIGHTSABER, _("sabre laser")),
    (MECHANICS, _("mécanique")),
    (MEDECINE, _("médecine")),
    (MELEE, _("corps à corps")),
    (RANGED_HEAVY, _("distance (armes lourdes)")),
    (RANGED_LIGHT, _("distance (armes légères)")),
)

# Skill dependancies
SKILL_DEPENDANCIES = {
    STAT_BRAWN: (ATHLETICS, BRAWL, LIGHTSABER, MELEE, RESILIENCE, ),
    STAT_AGILITY: (COORDINATION, GUNNERY, PILOTING, RANGED_HEAVY, RANGED_LIGHT, STEALTH, ),
    STAT_INTELLECT: (ASTROGATION, COMPUTERS, CORE_WORLD, EDUCATION, LORE, MECHANICS,
                     MEDECINE, OUTER_RIM, UNDERWORLD, XENOLOGY),
    STAT_CUNNING: (DECEPTION, PERCEPTION, SKULDUGGERY, STREETWISE, SURVIVAL, ),
    STAT_WILLPOWER: (COERCION, DISCIPLINE, VIGILANCE, ),
    STAT_PRESENCE: (CHARM, COOL, LEADERSHIP, NEGOCIATION, )
}

# SPECIES
SPECIES_HUMAN = 'human'
SPECIES_TWILEK = 'twilek'
SPECIES_BOTHAN = 'bothan'
SPECIES_DROID = 'droid'
SPECIES_GAND = 'gand'
SPECIES_RODIAN = 'rodian'
SPECIES_TRANDOSHAN = 'trandoshan'
SPECIES_WOOKIE = 'wookie'
SPECIES_CEREAN = 'cerean'
SPECIES_KELDOR = 'keldor'
SPECIES_MIRIALAN = 'mirialan'
SPECIES_NAUTOLAN = 'nautolan'
SPECIES_TOGRUTA = 'togruta'
SPECIES_ZABRAK = 'zabrak'
SPECIES_CREATURE = 'creature'
SPECIES = (
    # Common
    (SPECIES_HUMAN, _("humain")),
    (SPECIES_TWILEK, _("twi'lek")),
    # Edge of the Empire
    (SPECIES_BOTHAN, _("bothan")),
    (SPECIES_DROID, _("droïde")),
    (SPECIES_GAND, _("gand")),
    (SPECIES_RODIAN, _("rodien")),
    (SPECIES_TRANDOSHAN, _("trandoshan")),
    (SPECIES_WOOKIE, _("wookie")),
    # Force and Destiny
    (SPECIES_CEREAN, _("céréen")),
    (SPECIES_KELDOR, _("kel'dor")),
    (SPECIES_MIRIALAN, _("mirialan")),
    (SPECIES_NAUTOLAN, _("nautolan")),
    (SPECIES_TOGRUTA, _("togruta")),
    (SPECIES_ZABRAK, _("zabrak")),
    # Other
    (SPECIES_CREATURE, _("créature")),
)


# SPECIES_ABILITIES - default=10
SPECIES_ABILITIES = {
    SPECIES_BOTHAN: {'max_strain': 11},
    SPECIES_CEREAN: {'max_strain': 13},
    SPECIES_MIRIALAN: {'max_health': 11},
    SPECIES_NAUTOLAN: {'max_health': 11, 'max_strain': 9},
    SPECIES_TRANDOSHAN: {'max_health': 12, 'max_strain': 9},
    SPECIES_TWILEK: {'max_strain': 11},
    SPECIES_WOOKIE: {'max_health': 14, 'max_strain': 8},
}
