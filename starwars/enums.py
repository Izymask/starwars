from django.utils.translation import gettext_lazy as _


# Activation types
ACTIVATION_TYPE_ACTIVE = 'active'
ACTIVATION_TYPE_PASSIVE = 'passive'
ACTIVATION_TYPES = (
    (ACTIVATION_TYPE_ACTIVE, _("actif")),
    (ACTIVATION_TYPE_PASSIVE, _("passif"))
)

# Character types
CHARACTER_TYPE_PC = 'pc'
CHARACTER_TYPE_NPC = 'npc'
CHARACTER_TYPE_MINION = 'minion'
CHARACTER_TYPE_RIVAL = 'rival'
CHARACTER_TYPE_NEMESIS = 'nemesis'
CHARACTER_TYPES = (
    (CHARACTER_TYPE_PC, _("personnage joueur")),
    (CHARACTER_TYPE_NPC, _("personnage non joueur")),
    (CHARACTER_TYPE_MINION, _("sbire")),
    (CHARACTER_TYPE_RIVAL, _("rival")),
    (CHARACTER_TYPE_NEMESIS, _("nemesis"))
)

# Dice
# Dice types
DICE_TYPE_FORTUNE = 'fortune'
DICE_TYPE_MISFORTUNE = 'misfortune'
DICE_TYPE_APTITUDE = 'aptitude'
DICE_TYPE_DIFFICULTY = 'difficulty'
DICE_TYPE_MASTERY = 'mastery'
DICE_TYPE_CHALLENGE = 'challenge'
DICE_TYPE_FORCE = 'force'
DICE_TYPES = (
    (DICE_TYPE_FORTUNE, _("fortune")),
    (DICE_TYPE_MISFORTUNE, _("infortune")),
    (DICE_TYPE_APTITUDE, _("aptitude")),
    (DICE_TYPE_DIFFICULTY, _("difficulté")),
    (DICE_TYPE_MASTERY, _("maitrise")),
    (DICE_TYPE_CHALLENGE, _("défi")),
    (DICE_TYPE_FORCE, _("force"))
)

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

# Test difficulty
DIFFICULTY_SIMPLE = 0
DIFFICULTY_EASY = 1
DIFFICULTY_AVERAGE = 2
DIFFICULTY_HARD = 3
DIFFICULTY_DAUNTING = 4
DIFFICULTY_FORMIDABLE = 5

# EFFECTS
# EFFECT DURATIONS
EFFECT_DURATION_PERMANENT = 'permanent'
EFFECT_DURATION_SOURCE_TURN = 'source_turn'
EFFECT_DURATION_TARGET_TURN = 'target_turn'
EFFECT_DURATION_FIGHT = 'fight'
EFFECT_DURATIONS = (
    (EFFECT_DURATION_PERMANENT, _("permanent")),
    (EFFECT_DURATION_SOURCE_TURN, _("nombre de tours - source")),
    (EFFECT_DURATION_TARGET_TURN, _("nombre de tours - cible")),
    (EFFECT_DURATION_FIGHT, _("durée du combat")),
)

# EFFECT TYPES
EFFECT_ATTRIBUTE_MODIFIER = 'attribute_modifier'
EFFECT_DICE_POOL_MODIFIER = 'dice_pool_modifier'
EFFECT_TYPES = (
    (EFFECT_ATTRIBUTE_MODIFIER, _("modificateur d'attribut")),
    (EFFECT_DICE_POOL_MODIFIER, _("modificateur de dés"))
)

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
STAT_FORCE = 'force'
STATS = (
    (STAT_AGILITY, _("agilité")),
    (STAT_CUNNING, _("ruse")),
    (STAT_BRAWN, _("vigueur")),
    (STAT_INTELLECT, _("intelligence")),
    (STAT_PRESENCE, _("présence")),
    (STAT_WILLPOWER, _("volonté")),
    (STAT_FORCE, _("force"))
)
DICT_STATS = dict(STATS)


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

ALL_SKILLS = ITEM_SKILLS + (
    (ATHLETICS, _("athlétisme")),
    (ASTROGATION, _("astrogation")),
    (CHARM, _("charme")),
    (COERCION, _("coercition")),
    (COMPUTERS, _("informatique")),
    (COOL, _("calme")),
    (COORDINATION, _("coordination")),
    (CORE_WORLD, _("mondes du noyau")),
    (DECEPTION, _("tromperie")),
    (DISCIPLINE, _("sang froid")),
    (EDUCATION, _("education")),
    (LEADERSHIP, _("commandement")),
    (LORE, _("culture")),
    (NEGOCIATION, _("negociation")),
    (OUTER_RIM, _("bordure exterieure")),
    (PERCEPTION, _("perception")),
    (PILOTING, _("pilotage")),
    (RESILIENCE, _("résistance")),
    (SKULDUGGERY, _("magouilles")),
    (STEALTH, _("discretion")),
    (STREETWISE, _("système D")),
    (SURVIVAL, _("survie")),
    (UNDERWORLD, _("pègre")),
    (VIGILANCE, _("vigilance")),
    (XENOLOGY, _("xénologie"))
)
DICT_SKILLS = dict(ALL_SKILLS)


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

# EFFECT ATTRIBUTES (STATS + SKILLS + PROPERTIES)
ATTRIBUTE_DEFENSE = 'defense'
ATTRIBUTE_MAX_HEALTH = 'max_health'
ATTRIBUTE_MAX_STRAIN = 'max_strain'
ATTRIBUTE_SOAK_VALUE = 'soak_value'
ATTRIBUTES = STATS + ALL_SKILLS + (
    (ATTRIBUTE_DEFENSE, _("défense")),
    (ATTRIBUTE_MAX_HEALTH, _("santé max")),
    (ATTRIBUTE_MAX_STRAIN, _("stress max")),
    (ATTRIBUTE_SOAK_VALUE, _("valeur d'encaissement"))
)

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
