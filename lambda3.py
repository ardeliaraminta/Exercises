#q3

food_prices = [('Pizza', 5),('Nuggets', 10),('French Fries',3),('Lava Cake', 6),('Burger', 8)]
food_prices.sort( key = lambda x:x[1])
for item in food_prices:
  print(item)
