# luckylotto

A simple 7 number generator to help pick winning lotto numbers. As the lucky dips are never lucky.

#### luckylotto.py

Using the random module `luckylotto.py` will generate 5 numbers between 1 & 50 via a for loop, it will then go on to use another for loop to create 2 numbers between 1 & 12 for the 2 needed lucky stars using `randint()`. Which then are both appended to a list to give the result as an example:

Your luckylotto numbers could be [24, 17, 21, 35, 33, 12, 6]

---

#### euro_mill_scraper.py

The idea behind this file is to scrape the past winning euromillion numbers, store each one it it's own list. To then later compare the _luckylotto.py_ generated number to see if there are any regualr patterns.

### TODO:

- [ ] - scrape just the numbers and place in their own list
- [ ] - export the generated lists into a google sheet
- [ ] - compare luckylotto.py agaisnt the col of lists in the gsheet
- [ ] - check for patterns to see if the generated number is similar in anyway to past numbers

---

:man_shrugging: :moneybag: :man_shrugging: :moneybag: :man_shrugging: :moneybag: :man_shrugging: :moneybag:
