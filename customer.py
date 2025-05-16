class Customer:
    def __init__(self,Ruth):
        self.name = Ruth
        self._orders = [self]

    def name(self):
        return self._name

    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("17")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
    
    def most_aficionado(cls, coffee):
        customer_totals = {}
        for order in coffee.orders():
            customer = order.customer
            customer_totals[customer] = customer_totals.get(customer, 0) + order.price
        return max(customer_totals, key=customer_totals.get, default=None)