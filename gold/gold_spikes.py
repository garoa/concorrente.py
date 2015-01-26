prices = []
with open('gold_prices.txt', encoding='utf-8') as fd:
    for line in fd:
        date, price = line.split()
        prices.append((date, float(price)))

max_up = 0
dt_max_up = None
max_down = 0
dt_max_down = None

_, p0 = prices[0]
for date, p1 in prices[1:]:
    change = (p1 - p0) / p0 * 100
    if change > max_up:
        max_up = change
        dt_max_up = date
    if change < max_down:
        max_down = change
        dt_max_down = date
    p0 = p1

print('max up %s: %f' % (dt_max_up, max_up))
print('max down %s: %f' % (dt_max_down, max_down))
