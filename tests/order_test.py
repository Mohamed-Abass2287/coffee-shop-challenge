import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_order_init(self):
        customer = Customer("Lisa")
        coffee = Coffee("Flat White")
        order = Order(customer, coffee, 5.5)
        assert order.price == 5.5
        
    def test_order_validation(self):
        with pytest.raises(TypeError):
            Order("not customer", Coffee("Latte"), 5.0)
        with pytest.raises(TypeError):
            Order(Customer("Gedi"), "not coffee", 5.0)
        with pytest.raises(TypeError):
            Order(Customer("Gedi"), Coffee("Latte"), "5")
        with pytest.raises(ValueError):
            Order(Customer("Gedi"), Coffee("Latte"), 0.5)
    
    def test_order_price_immutable(self):
        customer = Customer("Gabriel")
        coffee = Coffee("Macchiato")
        order = Order(customer, coffee, 6.0)
        with pytest.raises(AttributeError):
            order.price = 7.0
