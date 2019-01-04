import random
import operator
import previous_winners as pw
from collections import Counter


winning_numbers = []

#  get user to choose whether they want to see popularity from previous results
#  or generate their own number and compare against previous results.


def user_choice():
    print('Please choose:')
    print('1: If you want to see popular numbers from previous results')
    print('2: To generate a luckydip and compare popularity agaisnt previous winners')

    user_choice = input()

    if user_choice == '1':
        #  generate and sorts previous_winners by the second element
        #  to show most popular numbers drawn
        pop_nums = Counter(n for l in pw.previous_winners for n in l)
        ordered_pop_nums = sorted(pop_nums.items(), key=operator.itemgetter(1), reverse=True)

        print('--- most popular numbers from previous results are ---')
        print(ordered_pop_nums)

    elif user_choice == '2':
        #  creates main lotto numbers appends to winning_numbers
        for ball_numbers in range(5):
            ball_numbers = random.randint(1, 50)
            winning_numbers.append(ball_numbers)

        #  creates lucky star numbers and appends to winning_numbers
        for lucky_star_nums in range(2):
            lucky_star_nums = random.randint(1, 12)
            winning_numbers.append(lucky_star_nums)

        print('--- # ---')
        print(f'Your luckylotto numbers could be {winning_numbers}')
        print()
        print('The numbers appear in previous winning numbers this many times:')
        print()

        #  flattens winning_numbers and counts how many times each number appears win previous_winners
        counts = Counter(n for l in pw.previous_winners for n in l)
        winners_count = {n: counts.get(n, 0) for n in winning_numbers}
        ordered_winners_count = sorted(winners_count.items(), key=operator.itemgetter(1), reverse=True)
        print(ordered_winners_count)
        

user_choice()

'''
Just a list of previous winners in order so i can keep an eye on it.
(1, 16), (2, 15), (3, 20), (4, 19), (5, 9), (6, 12), (7, 10), (8, 15), (9, 12), (10, 9), (11, 14), (12, 21), (13, 4), (14, 5), (15, 7), (16, 6), (17, 7), (18, 7), (19, 2), (20, 4), (21, 5), (22, 1), (23, 7), (24, 3), (25, 5), (26, 6), (27, 4), (28, 5), (29, 4), (30, 5), (31, 7), (32, 6), (33, 2), (34, 3), (35, 3), (36, 6), (37, 6), (38, 5), (39, 3), (40, 5), (41, 2), (42, 9), (43, 9), (44, 5), (45, 9), (46, 3), (47, 2), (48, 5), (49, 3), (50, 5)
'''
