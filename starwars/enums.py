# Skill dependancies
SKILL_DEPENDANCIES = {
    'brawn': ('athletics', 'brawl', 'melee', 'resilience', ),
    'agility': ('coordination', 'gunnery', 'piloting', 'ranged_heavy', 'ranged_light', 'stealth', ),
    'intellect': ('astrogation', 'computers', 'core_world', 'education', 'lore', 'mechanics',
                  'medecine', 'outer_rim', 'underworld', 'xenology'),
    'cunning': ('deception', 'perception', 'skulduggery', 'streetwise', 'survival', ),
    'willpower': ('coercion', 'discipline', 'vigilance', ),
    'presence': ('charm', 'cool', 'leadership', 'negociation', )
}

# Dice
DICE = {
    'fortune': {
        0: None, 1: None,
        2: {'success': 1},
        3: {'success': 1, 'advantage': 1},
        4: {'advantage': 2},
        5: {'advantage': 1}
    },
    'misfortune': {
        0: None, 1: None,
        2: {'failure': 1},
        3: {'failure': 1},
        4: {'threat': 1},
        5: {'threat': 1}
    },
    'aptitude': {
        0: None,
        1: {'success': 1},
        2: {'success': 1},
        3: {'success': 2},
        4: {'advantage': 1},
        5: {'advantage': 1},
        6: {'success': 1, 'advantage': 1},
        7: {'advantage': 2}
    },
    'difficulty': {
        0: None,
        1: {'failure': 1},
        2: {'failure': 2},
        3: {'threat': 1},
        4: {'threat': 1},
        5: {'threat': 1},
        6: {'threat': 2},
        7: {'failure': 1, 'threat': 1}
    },
    'mastery': {
        0: None,
        1: {'success': 1},
        2: {'success': 1},
        3: {'success': 2},
        4: {'success': 2},
        5: {'advantage': 1},
        6: {'success': 1, 'advantage': 1},
        7: {'success': 1, 'advantage': 1},
        8: {'success': 1, 'advantage': 1},
        9: {'advantage': 2},
        10: {'advantage': 2},
        11: {'triumph': 1}
    },
    'challenge': {
        0: None,
        1: {'failure': 1},
        2: {'failure': 1},
        3: {'failure': 2},
        4: {'failure': 2},
        5: {'threat': 1},
        6: {'threat': 1},
        7: {'failure': 1, 'threat': 1},
        8: {'failure': 1, 'threat': 1},
        9: {'threat': 2},
        10: {'threat': 2},
        11: {'disaster': 1}
    },
    'force': {
        0: {'dark_force': 1},
        1: {'dark_force': 1},
        2: {'dark_force': 1},
        3: {'dark_force': 1},
        4: {'dark_force': 1},
        5: {'dark_force': 1},
        6: {'dark_force': 2},
        7: {'light_force': 1},
        8: {'light_force': 1},
        9: {'light_force': 2},
        10: {'light_force': 2},
        11: {'light_force': 2}
    }
}
