from bs4 import BeautifulSoup
import requests

src = requests.get('https://www.national-lottery.co.uk/results/euromillions/draw-history').text

soup = BeautifulSoup(src, 'lxml')

for results in soup.find_all('li', attrs={'class': 'table_cell_3'}):
    previous_nums = results.find('span', attrs={'class': 'table_cell_block'})
    print(previous_nums)