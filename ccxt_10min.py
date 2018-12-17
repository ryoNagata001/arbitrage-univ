import ccxt
from time import sleep 
# print (ccxt.exchanges)
amount = 0.001
exchange_list = ['bitflyer', 'quoinex', 'zaif']
ask_exchange = ''
ask_price = 99999999
bid_exchange = ''
bid_price = 0

ask_last = 0
bid_last = 0
for i in range(200):
  for exchange_id in exchange_list:
    exchange = eval('ccxt.' + exchange_id + '()')
    orderbook = exchange.fetch_order_book ('BTC/JPY')
    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
    if ask < ask_price:
      ask_exchange = exchange_id
      ask_price = ask
    if bid > bid_price:
      bid_exchange = exchange_id
      bid_price = bid

  ask_last = ask_price + ask_last
  bid_last = bid_price + bid_last
  print (ask_exchange, 'で', ask_price * amount, '円で買って')
  print (bid_exchange, 'で', bid_price * amount, '円で売れば')
  print ((bid_price - ask_price) * amount, '円の利益')  
  sleep(3)
print (ask_last, '円で買って')
print (bid_last, '円で売れば')
print ((bid_last - ask_last), '円の利益', (bid_last - ask_last)/bid_last, '%')