from bs4 import BeautifulSoup
import requests
import csv

src = requests.get('https://www.national-lottery.co.uk/results/euromillions/draw-history').text

soup = BeautifulSoup(src, 'lxml')

csv_file = open('euromill_winners.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['winning numbers'])

for results in soup.find_all('li', attrs={'class': 'table_cell_3'}):
    previous_nums = results.find('span', attrs={'class': 'table_cell_block'})
    print(previous_nums)

    csv.writer.writerow([previous_nums])

csv_file.close()