import random

winning_numbers = []

'''generate 5 numbers from 1 to 50 and 2 Lucky Stars from 1 to 12'''
def generate_nums():

    #  creates main lotto numbers
    for num in range(5):
        ball_numbers = random.randint(1, 50)
        winning_numbers.append(ball_numbers)
    
    #  creates lucky star numbers
    for stars in range(2):
        lucky_star_nums = random.randint(1, 12)
        winning_numbers.append(lucky_star_nums)

    print(f'Your winning numbers could be {winning_numbers}')

generate_nums()