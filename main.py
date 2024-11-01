from shop_functions import *
from currency_exchange_tool import *
from delivery_yara import *

import pyfiglet as pf
import sys
from termcolor import colored, cprint
import pyfiglet
from colorama import Fore
styled_text=pyfiglet.figlet_format('Welcome to the cake shop',font="doom")
print(Fore.CYAN + styled_text)
print("menu:")
cprint("   1.chocolate cake----------------5.99","black")
cprint("   2.vanilla cake------------------4.49","white")
cprint("   3.red velvet cake---------------6.00","red")
cprint("   4.lemon cake--------------------4.99","yellow")
cprint("   5.funfetti cake-----------------7.99","cyan")
cprint("   6.strawberry shortcake----------7.49","light_magenta")
cprint("   7.cheesecake--------------------8.49","light_yellow")
cprint("   8.marble cake-------------------8.00","light_grey")
cprint("   9.black forest cake-------------6.49","green")
cprint("   10.carrot cake------------------5.49","light_red")

exchange_rates = {
    'USD': 1.30, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.20,
    'CAD': 1.80,
    'CNY': 9.27,
    'SAR': 4.90,
}


new_c = str(input("Choose a currency you want to convert your amount to and choose from USD EUR CAD CNY and SAR "))
amount = float(input("How much do you want to convert "))
result = currency_convert(new_c,amount)
print(result)
   
    

basket=(itemList())
total=totalPrice(basket)


postcode=input("Enter your postcode: ")
delivery_cost=delivery_cost(postcode)
print('Your delivery cost is £'+ str(delivery_cost))

Total= total + delivery_cost
print("Your total cost is £" + str(Total))

another_currency=str(input("Choose from the 5 given currencies above you want to convert the final cost to "))
delivery_price = Total
final_conversion = final_delivery_price(another_currency, delivery_price)
print(final_conversion)
















