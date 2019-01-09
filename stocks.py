stock_dict = {'AAPL': 'Apple', 'AMZN': 'Amazon',
              'NFLX': 'Netflix', 'GOOG': 'Google'}

purchases = [('AAPL', 25, '04-oct-2006', 50), ('GOOG', 15, '01-dec-2016', 100), ('AMZN', 10, '20-mar-2010', 89),
             ('NFLX', 10, '30-may-2018', 100), ('NFLX', 7, '13-jun-2016', 100), ('GOOG', 5, '01-jan-2019', 150)]

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name.

for purchase in purchases:
    print('I purchased {0} stock for ${1}'.format(
        stock_dict[purchase[0]], purchase[3]))

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE.

new_dict = {}
for purchase in purchases:
  key = purchase[0]
  if key in new_dict:
    new_dict[key].append(purchase)
  else:
    new_dict[key] = [purchase]

print(new_dict)

for key, company in new_dict.items():
  price = 0
  print('----{0}----'.format(key))
  for block in company:
    price += (block[3] * block[1])
    print(block)
  print('Total value of stock in portfolio: {0}'.format(price))

