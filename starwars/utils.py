from random import choice

from starwars.enums import (DICE, DICE_SUCCESS, DICE_FAILURE, DICE_TRIUMPH, DICE_DISASTER, DICE_ADVANTAGE, DICE_THREAT,
                            DICE_LIGHT_FORCE, DICE_DARK_FORCE)


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

    # Add triumph/disaster to success/failure
    total_success = result_details.get(DICE_SUCCESS, 0) + result_details.get(DICE_TRIUMPH, 0)
    total_failures = result_details.get(DICE_FAILURE, 0) + result_details.get(DICE_DISASTER, 0)
    result_details[DICE_SUCCESS] = total_success
    result_details[DICE_FAILURE] = total_failures

    # Check Advantages/Threats
    advantages = result_details.get(DICE_ADVANTAGE, 0)
    threats = result_details.get(DICE_THREAT, 0)

    return {
        'is_success': result_details.get(DICE_SUCCESS, 0) > result_details.get(DICE_FAILURE, 0),
        'remaining_success': max(total_success - total_failures, 0),
        'remaining_advantages': max(advantages - threats, 0),
        'remaining_threats': max(threats - advantages, 0),
        **{key: result_details.pop(key, 0) for key in (DICE_TRIUMPH, DICE_DISASTER, DICE_LIGHT_FORCE, DICE_DARK_FORCE)},
        'details': result_details
    }
