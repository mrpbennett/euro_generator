import random

'''generate 5 numbers from 1 to 50 and 2 Lucky Stars from 1 to 12'''
num_1 = random.randint(1, 50)
num_2 = random.randint(1, 50)
num_3 = random.randint(1, 50)
num_4 = random.randint(1, 50)
num_5 = random.randint(1, 50)
lucky_star_1 = random.randint(1, 12)
lucky_star_2 = random.randint(1, 12)


'''empty list to store nums in'''
winning_nums = []


'''euro num generator'''
def euro_generator():
    winning_nums.append(num_1)
    winning_nums.append(num_2)
    winning_nums.append(num_3)
    winning_nums.append(num_4)
    winning_nums.append(num_5)
    winning_nums.append(lucky_star_1)
    winning_nums.append(lucky_star_2)

    print(f'Your winning numbers could be {winning_nums}')


euro_generator()

