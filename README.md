# luckylotto

A simple 7 number generator to help pick winning lotto numbers. As the lucky dips are never lucky.

#### luckylotto.py

LuckyLotto is a little program that allows you to generate a potential winning EuroMillions ticket. 

The program does two things:

1. Allows the user to generate a tuple of previously drawn numbers and sorts it by most common numbers drawn. Enabling the user to see which numbers were drawn most frequently.

2. Generate a LuckyDip using the `randint()` method from random and then compare that lucky dip to the previous winning numbers. Allowing the user to see if the generated number has numbers that are commonly drawn.

an example output:

```bash
--- # ---
Your luckylotto numbers could be [29, 11, 23, 2, 39, 7, 8]

The numbers appear in previous winning numbers this many times:

[(2, 15), (8, 15), (11, 14), (7, 10), (23, 7), (29, 4), (39, 3)]
```

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
