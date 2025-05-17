from customer import Customer
from coffee import Coffee
from order import Order

# Create Customers
gabriel = Customer("gabriel")
gedi = Customer("gedi")

# Create Coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create Orders
order1 = Order(gabriel, latte, 3.5)
order2 = Order(gabriel, espresso, 2.75)
order3 = Order(gedi, latte, 4.0)

# Print out data to verify correctness
print("=== Customers ===")
print(gabriel.name)  # Gabriel
print(gedi.name)     # Gedi

print("\n=== Coffees ===")
print(latte.name)      # Latte
print(espresso.name)   # Espresso

print("\n=== Orders ===")
print(f"Order1: {order1.customer.name} ordered {order1.coffee.name} for ${order1.price}")
print(f"Order2: {order2.customer.name} ordered {order2.coffee.name} for ${order2.price}")
print(f"Order3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")

# Test error cases (uncomment to test)
# invalid_customer = Order("NotACustomer", latte, 3.5)  # Should raise TypeError
# invalid_price = Order(gabriel, latte, 20.0)           # Should raise ValueError
# short_coffee = Coffee("A")                            # Should raise ValueError
