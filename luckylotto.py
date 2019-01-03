import random
from collections import Counter

winning_numbers = []
previous_winners = [
    [1, 8, 11, 25, 28, 4, 6],
    [13, 16, 34, 35, 45, 10, 12],
    [4, 5, 8, 31, 43, 2, 9],
    [2, 12, 15, 34, 50, 3, 4],
    [20, 25, 34, 42, 45, 6, 11],
    [11, 17, 22, 23, 41, 6, 11],
    [2, 4, 23, 39, 40, 3, 9],
    [2, 15, 40, 43, 46, 3, 6],
    [4, 6, 27, 48, 50, 1, 11],
    [1, 4, 14, 21, 49, 2, 12],
    [3, 8, 26, 33, 45, 7, 10],
    [4, 30, 31, 38, 42, 4, 6],
    [4, 16, 32, 42, 46, 8, 12],
    [3, 14, 31, 36, 50, 1, 12]
       
]


#  creates the 7 numbers you need for a euromillions lotto ticket
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

    counts = Counter(n for l in previous_winners for n in l)
    print('---')
    print('generated number appears in previous winning numbers this many times: ')
    print('---')
    print({n: counts.get(n, 0) for n in winning_numbers})

luckylotto()

