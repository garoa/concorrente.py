import glob
import os
import re
import random

BASE = 'gold/*.html'

DATE_TPL = r'[01]\d/[0-3]\d/'
PRICE_RE = re.compile(r'\$\d{2,4}\.\d\d')

round_prices = 0
total_prices = 0


for path in sorted(glob.glob(BASE)):
    _, name = os.path.split(path)
    year, _ = os.path.splitext(name)
    regex = re.compile(DATE_TPL + year[-2:])
    with open(path, encoding='utf-8') as fd:
        html = fd.read()
    dates = []
    for date in regex.findall(html):
        month, day = date.split('/')[:2]
        dates.append((year, month, day))
    prices = PRICE_RE.findall(html)
    assert len(dates) == len(prices), '%d != %d' % (len(dates), len(prices))
    for (year, month, day), price in zip(dates, prices):
        price = float(price[1:])
        fudge = random.randint(0,25) * .05
        fudge = fudge if random.randint(1,2) == 1 else -fudge
        price = price + fudge
        price = float(int(price)) if random.randint(1, 13) in (1,2) else price
        print('%s-%s-%s %0.2f' % (year, month, day, price))
        if price - int(price) == 0:
            round_prices += 1
        total_prices += 1

#print('round prices %: ',round_prices/total_prices*100)
