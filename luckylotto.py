import random

winning_numbers = []


def luckylotto():
    #  creates main lotto numbers
    for ball_numbers in range(5):
        ball_numbers = random.randint(1, 50)
        winning_numbers.append(ball_numbers)
    
    #  creates lucky star numbers
    for lucky_star_nums in range(2):
        lucky_star_nums = random.randint(1, 12)
        winning_numbers.append(lucky_star_nums)

    print(f'Your luckylotto numbers could be {winning_numbers}')

luckylotto()

