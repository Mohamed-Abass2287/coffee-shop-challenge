import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_init(self):
        customer = Customer("Jane")
        assert customer.name == "Jane"
        
    def test_customer_name_validation(self):
        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")
    
    def test_customer_orders(self):
        customer = Customer("John")
        coffee = Coffee("Latte")
        order = Order(customer, coffee, 5.0)
        assert order in customer.orders()
    
    def test_customer_coffees(self):
        customer = Customer("Mike")
        coffee1 = Coffee("Mocha")
        coffee2 = Coffee("Espresso")
        Order(customer, coffee1, 5.0)
        Order(customer, coffee2, 6.0)
        assert len(customer.coffees()) == 2