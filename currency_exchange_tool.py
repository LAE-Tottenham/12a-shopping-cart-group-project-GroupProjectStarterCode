import math # you'll probably need this




exchange_rates = {
    'USD': 1.30, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.20,
    'CAD': 1.80,
    'CNY': 9.27,
    'SAR': 4.90,
}


def check_currency_exists(currency):
    currencies = {
        'USD': 'United States Dollar',
        'EUR': 'Euro',
        'CAD': 'Canadian Dollar',
        'CNY': 'Chinese Yuan',
        'SAR': 'Saudi Riyal'
    }
    return currency in currencies

def validate_amount(amount):
    return 10 <= amount <= 1000

def currency_convert(original_c, new_c,amount):
    if original_c != 'GBP':
        return "Original currency must be GBP"
    if not check_currency_exists(new_c):
        return "Please choose a different currency "
    if not validate_amount(amount): 
        return "Amount must be between £10 and £1000"

    exchange_rates = {
    'USD': 1.30, #I.E. 1 Pound is 1.13 Dollars
    'EUR': 1.20,
    'CAD': 1.80,
    'CNY': 9.27,
    'SAR': 4.90,
    }

    converted_amount = amount*exchange_rates[new_c]
    return f"£{amount} is equal to {converted_amount: .2f}{new_c}"

result = currency_convert()
print(result)
   


   
def final_delivery_price(another_currency,delivery_price):
    if another_currency not in exchange_rates:
        return "Please choose a different currency"
    new_price = delivery_price*exchange_rates[another_currency]
    return f"£{delivery_price} is equal to {new_price: .2f}{another_currency}"

    

     




    
    
