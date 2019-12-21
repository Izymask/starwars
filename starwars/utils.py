from random import choice

from starwars.enums import DICE


def roll_dice(fortune=0, misfortune=0, aptitude=0, difficulty=0, mastery=0, challenge=0, force=0):
    dices_to_roll = locals()
    result_details = {}
    for dice_type, number in dices_to_roll.items():
        if number == 0:
            continue
        dice = DICE.get(dice_type)
        for roll in range(number):
            dice_result = dice.get(choice(range(len(dice)))) or {}
            for result_type, value in dice_result.items():
                result_details[result_type] = result_details.get(result_type, 0) + value

    # Check Advantages/Threats
    advantages = result_details.get('advantage', 0)
    threats = result_details.get('threat', 0)

    return {
        'is_success': result_details.get('success', 0) > result_details.get('failure', 0),
        'remaining_advantages': max(advantages - threats, 0),
        'remaining_threats': max(threats - advantages, 0),
        **{key: result_details.pop(key, 0) for key in ('triumph', 'disaster', 'light_force', 'dark_force')},
        'details': result_details
    }
