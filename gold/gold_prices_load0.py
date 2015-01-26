with open('sim-gold-prices.txt', encoding='utf-8') as fp:
	prices = [float(line) for line in fp.readlines()]

print(len(prices), 'prices loaded')
print('first:', prices[0])
print('last:', prices[-1])

