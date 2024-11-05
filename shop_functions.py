items = {
    'apple': 1.00,
    'banana': 0.50,
    'cherry': 0.75,
    'milk': 10.00,
    'bar of gold': 0.01,
    'rolex watch': 0.05,
    'bottle of water': 100.00,
    'bread': 1.00,
    'cheese': 5.50,
    'nintendo': 5.00}

def delivery():
    postcode = input("Enter your postcode: ").upper()
    distance = {'N': 3.14,
                'S': 11.00,
                'E': 35000,
                'W': 0.90}
    if postcode[0] == "N":
        deliveryPrice = distance['N']
        return deliveryPrice
    elif postcode[0] == "S":
        deliveryPrice = distance['S']
        return deliveryPrice
    elif postcode[0] == "E":
        deliveryPrice = distance['E']
        return deliveryPrice
    elif postcode[0] == "W":
        deliveryPrice = distance['W']
        return deliveryPrice

list  = ['apple','banana','cherry','milk','bar of gold','rolex watch','bottle of water','bread','cheese','nintendo']
agree = input("Would you like to buy something? y/n: ").upper()

def start_shop():
    count = 0
    while True:
        print(items)
        num = int(input("How many items would you like to buy? "))
        for i in range(0,num):
            buy = input("what would you like to buy: ")
            for i in range(0,9):
                if buy == list[i]:
                    count = count + items[list[i]]
        agree = input("Would you to continue to buy something? y/n: ").upper()
        if agree ==  "N":
            deliveryPrice = delivery()
            p = (count+deliveryPrice) *100
            s= round(p)/100
            print(s)
        return s         
            
           


start_shop()

        #print("What you would like to buy? ")
        # display items to buy

    # blah blah blah

        
