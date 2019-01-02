from bs4 import BeautifulSoup
import requests
import csv

src = requests.get('https://www.national-lottery.co.uk/results/euromillions/draw-history').text

soup = BeautifulSoup(src, 'lxml')

ball_numbers = soup.find('li', class_='table_cell_block')
print(ball_numbers)