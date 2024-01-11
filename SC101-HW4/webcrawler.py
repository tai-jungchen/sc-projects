"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        total_boy = 0
        total_girl = 0
        # ----- Write your code below this line ----- #
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", {"class": "t-stripe"})
        trs = table.select("tbody tr")[:-1]

        for name_tag in trs:
            num_boy = name_tag.find_all('td')[2].text
            num_girl = name_tag.find_all('td')[4].text

            total_boy += int(num_boy.replace(',', ''))
            total_girl += int(num_girl.replace(',', ''))

        print(f'Male Number: {total_boy}')
        print(f'Female Number: {total_girl}')


if __name__ == '__main__':
    main()
