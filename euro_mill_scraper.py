from bs4 import BeautifulSoup
import requests
import csv

src = requests.get('https://www.national-lottery.co.uk/results/euromillions/draw-history').text

soup = BeautifulSoup(src, 'lxml')

ball_numbers = soup.find('li', class_='table_cell_3')
lucky_stars = soup.find('li', class_='table_cell_4')

for main_nums in soup.find_all('span'):
    winning_balls = main_nums.text
    print(winning_balls)

    