#it states that each class or object in a code should have a single responsibility of task
#let us discuss a example
class Item:
    def _init_(self,name,price):
        self.name = name
        self.price = price
        
class Order:
    def _init_(self,order_id,items):
        self.order_id = order_id
        self.items = items
        
    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

class OrderManager:
    def place_order(self,order):
        
        total = order.calculate_total()
        print(f'total is:  {total}')
order_items =[
    Item("product 1", 10),
    Item("product 2", 20),
    Item ("Product 3", 15)
]
order =Order(123,order_items)
order_manager =OrderManager()
order_manager.place_order(order)
        