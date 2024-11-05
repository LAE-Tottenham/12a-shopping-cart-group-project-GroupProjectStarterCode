
from gettext import install
import math

import pip # you'll probably need this
exchange_rates = {
    'USD': 1.13, 
    'EUR': 1.15,
    'CAD': 1.80,
    'AED': 4.80,
    'CNY': 9.25,
}
def check_currency(curren):
    if "gbp" in curren or "GBP" in curren or "£" in curren or "pounds" in curren:
        return curren
    else:
        return "error"
while True:
    curren=input("Enter current currency: ")
    if curren.upper()=="GBP" or curren=="£" or curren.lower()=="pounds":
        break
    print("Can only convert from gbp")
res=check_currency(curren)
#print(res)
def currency_convert(currency, amount):
    cur=currency.upper() in exchange_rates
    res=check_currency(curren)
    while res=="error":
        if curren.upper!="GBP" or curren!="pounds" or curren!="£":
            return "Cannot convert currencies other than GBP"
    else:
        if amount>=10 and amount<=1000:
            if cur==True:
                return round(exchange_rates.get(currency.upper())*amount, 2)
            else:
                return "Incorrect code"
        else:
            return "Basket total is too large/small"
while True:
    amount=int(input("Enter basket total: "))
    if amount>=10 and amount<=1000:
        break
    elif amount>1000:
        print("Too large")
    elif amount<10:
        print("Too small")
currency=input("Enter currency, use iso currency code: ")
res1=currency_convert(currency,amount)
print(res1)

#some parts have to be added to main

##########################################################





#f = Figlet(font="slant")
#print(f.renderText("Welcome to our shop!"))

#fancy text display