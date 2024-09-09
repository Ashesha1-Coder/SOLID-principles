#it states that each class or object in a code should have a single responsibility of task
#let us discuss a example
class Item:
    def _init_(self,name,price):
        self.name = name
        self.price = price
        
class Order:
    def _init_(self,order_id,item):
        self.order_id = order_id
        self.items = items
        
    def calculate_total(self):
        total = sum(items.prices for item in sekf.items)
        return total

class OrderManager:
    def place_order(self,order):
        total = order.calculate_total()