import random

dice_rolls = [random.randint(1, 20) for number in range(500)]

roll_over_fourteen = [dice_roll for dice_roll in dice_rolls if dice_roll > 14]

odd_rolls = [dice_roll for dice_roll in dice_rolls if dice_roll % 2 == 1]

other_rolls = [dice_roll for dice_roll in dice_rolls if dice_roll not in roll_over_fourteen and dice_roll not in odd_rolls]

print(roll_over_fourteen)
print(odd_rolls)
print(other_rolls)
