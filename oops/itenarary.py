import pandas as pd
import string
import random


class Cart:
    def __init__(self):
        self.total = 0
        self.items = []
        self.price_list = []
        self.item_qty = []
        self.discount_percentage = Store.discount()

    


    def coupon_discount(self ,store, coupon_code):
        if coupon_code in store.coupons:
            print(f'Store coupon , "{coupon_code}" redeemed\n${self.total * .2} saved')
            self.total -= self.total * .2
            self.show_cart()      
        else:
            print(f"Coupon '{coupon_code}' is invalid")  
        
    def add_to_cart(self, item, qty=1):
        if item.name not in self.items:
            self.total += item.price * qty
            self.items.append(item.name)
            self.price_list.append(item.price)
            self.item_qty.append(qty)
        elif item.name in self.items:
            self.item_qty[self.items.index(item.name)] += 1
            self.total += item.price * qty



    def remove_from_cart(self, item, qty=1):
        if item.name in self.items:
            index = self.items.index(item.name)
            self.total -= item.price * qty
            self.items.pop(index) #woahhh
            self.price_list.pop(index) 
            self.item_qty.pop(index)
        else:
            print(f"{item.name} is not in the cart.")



    def show_cart(self):
        if self.total >= 5000:
            print(f'You have recieved a ${self.total * (self.discount_percentage / 100)} discount')
            self.total -= self.total * (self.discount_percentage / 100)
            return self.total
        else:
            pass
        headings = ['Item', 'Price', 'Quantity']
        df = pd.DataFrame(columns=headings)
        sum_price = 0
        sum_qty = 0
        for i in range(len(self.items)):
            df.loc[i] = [self.items[i], self.price_list[i], self.item_qty[i]]
            sum_price += self.price_list[i]
            sum_qty += self.item_qty[i]
        df.loc[len(self.items)] = ['---' , '---' , '---']
        df.loc[len(self.items) + 1] = ['Total' , f'${self.total}' , sum_qty]
        print(df)


class Item:
    def __init__(self, price, name , qty=1):
        self.price = price
        self.name = name
        self.qty = qty


class Store():
    def __init__(self , name):
        self.name = name
        self.coupons = []
        self.item_list = []
        columns = ['Items' , 'Price' , "Qty in Stock"]
        self.df = pd.DataFrame(columns=columns)
        
    
    def show_store(self):
        print(f'{self.name.center(30 , '-')}\n{'-' * 30}')
        for item in self.item_list:
            self.df.loc[self.item_list.index(item)] = item

        print(self.df)

    def discount():
        return 10
           
    def create(self ,name , price, qty ):
        item = Item(price,name , qty)
        self.item_list.append([item.name , item.price , qty])


    def checkout(self, cart):
        for i in range(0 , (len(cart) -1)) :
            pass
            
            



    def create_coupon(self):
        coupon = []
        code = ''
        for i in range(5):
            coupon.append(random.choice(string.ascii_letters))
        for i in range(3):
            coupon.append(random.choice(string.digits))
            

        random.shuffle(coupon)
        for i in coupon:
            code += i
        self.coupons.append(code)
        return code
    
    
item1= Item(220, 'hh')
item2= Item(200, 'DJD')
item3= Item(300, 'DJDD')
item4= Item(300, 'hh22')
cart1= Cart()
cart1.add_to_cart(item1)
cart1.add_to_cart(item3)
cart1.add_to_cart(item4)
cart1.add_to_cart(item2)
cart1.add_to_cart(item2)


cart1.show_cart()

print(cart1.items)
print(cart1.item_qty)
print(cart1.price_list)


amazon = Store("Amazon")
amazon.create('DJD' , 200 , 1)
amazon.create('DJD' , 500 , 3)
amazon.create('D2D' , 400 , 2)
print(amazon.item_list)





        
