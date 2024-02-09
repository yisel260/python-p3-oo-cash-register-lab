#!/usr/bin/env python3

class CashRegister:
     
     def __init__(self,discount = 0):
        self.discount  = discount 
        self.total = 0
        self.items= []
        self.prices= []
        self.quantities=[]

     @property
     def discount(self):
        return self._discount 
     @discount.setter
     def discount (self, value):
        if isinstance(value, int):
            self._discount = value
        else:
             print("The value must be an interger")


     def add_item (self,title, price, quantity=1) :
         self.total+= price * quantity

         for _ in range(quantity):
          self.items.append(title)
          self.prices.append(price)
          self.quantities.append(quantity)

     def apply_discount(self):
         if self.discount >1 and self.discount<100:
            new_amount = ( 1 - self.discount/100)*self.total
            self.total = round(new_amount,2)
            print(f"After the discount, the total comes to ${new_amount:.0f}.")
         else:
           print("There is no discount to apply.")

    
     def void_last_transaction(self):
           last_price = self.prices.pop()
           last_quantity = self.quantities.pop()
           self.total -= last_price * last_quantity
           self.total = round(self.total, 2)