
from shop_functions import start_shop 
from currency_exchange_tool import currency_convert

print('Welcome to my shop')
while True:
    amount = start_shop()
    price = currency_convert()
    print('£', price)
    # blah blah 
