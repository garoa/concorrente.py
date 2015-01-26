with open('sim_gold_prices.txt', encoding='utf-8') as fp:
	for line in fp:
		print(line.split()[-1].strip())
