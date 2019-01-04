import random
import operator
import previous_winners as pw
from collections import Counter

winning_numbers = []


def luckylotto():
    print('Please choose:')
    print('1: If you want to see popular numbers from previous results')
    print('2: To generate a LOTTO ticket and compare popularity agaisnt previous winners')

    user_choice = input()

    if user_choice == '1':
        #  comparison
        pop_nums = Counter(n for l in pw.previous_lotto_winners for n in l)
        ordered_pop_nums = sorted(pop_nums.items(), key=operator.itemgetter(1), reverse=True)

        print('--- most popular numbers from previous results are ---')
        print(ordered_pop_nums)

    elif user_choice == '2':
        #  creates main LOTTO numbers and appends to winning_numbers
        for lotto_numbers in range(6):
            lotto_numbers = random.randint(1, 50)
            winning_numbers.append(lotto_numbers)

        print('--- # ---')
        print(f'Your luckylotto numbers could be {winning_numbers}')
        print()
        print('The numbers appear in previous winning numbers this many times:')
        print()

        counts = Counter(n for l in pw.previous_lotto_winners for n in l)
        winners_count = {n: counts.get(n, 0) for n in winning_numbers}
        ordered_winners_count = sorted(winners_count.items(), key=operator.itemgetter(1), reverse=True)
        print(ordered_winners_count)

luckylotto()


