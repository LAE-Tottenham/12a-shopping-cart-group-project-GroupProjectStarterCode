priceList = [ ['CHOCOLATE', 'VANILLA', 'RED VELVET', 'LEMON', 'FUNFETTI', 'STRAWBERRY', 'CHEESECAKE', 'MARBLE', 'BLACK FOREST', 'CARROT'],
         [5.99, 4.90, 6.00, 4.99, 7.99, 7.49, 8.49, 8.00, 6.49, 5.49]] 

def itemList():
    basket = []
    stop = False
    num = 0
    while stop == False and num <= 10:
        item= int(input("enter the cake number you would like to buy. enter '0' to complete your order: "))
        valid = False
        while valid == False: 
            if item > 0 and item < 11:
                valid = True
                basket.append(item)
                num= num + 1
            elif item == 0:
                valid = True
                stop = True
            else: 
                while valid == False:
                    item=int(input("please enter a valid cake number: "))
                    if item > 0 and item < 11:
                        valid = True
                        basket.append(item)
                        num= num + 1
                    elif item == 0:
                        valid = True
                        stop = True
    return basket

def totalPrice(basket):
    total=0
    for i in range(len(basket)):
        item = (basket [i] -1)
        price = (priceList[1][item])
        total = total + price
    return total


        
