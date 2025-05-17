import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_coffee_init(self):
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        
    def test_coffee_name_validation(self):
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")
        coffee = Coffee("Valid")
        with pytest.raises(AttributeError):
            coffee.name = "New Name"
    
    def test_coffee_orders(self):
        coffee = Coffee("Cappuccino")
        customer = Customer("Sarah")
        order = Order(customer, coffee, 5.0)
        assert order in coffee.orders()
    
    def test_coffee_average_price(self):
        coffee = Coffee("Americano")
        customer1 = Customer("Tom")
        customer2 = Customer("Jerry")
        Order(customer1, coffee, 5.0)
        Order(customer2, coffee, 7.0)
        assert coffee.average_price() == 6.0

    