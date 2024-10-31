from currency_exchange_tool import currency_convert
from shop_functions import start_shop
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
