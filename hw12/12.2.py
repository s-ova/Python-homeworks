class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}"

class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, *items):
        for item, cnt in items:
            if item in self.products:
                self.products[item] += cnt
            else:
                self.products[item] = cnt

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {cnt} pcs." for item, cnt in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}"

lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)
print(apple)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item((lemon, 2), (apple, 10))
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 2 pcs. = 10 грн
apple: 10 pcs. = 20 грн
Total: 30 грн
"""

assert isinstance(cart.user, User) is True, 'An instance of the User class'
assert cart.get_total() == 30, "Total 30"
assert cart.get_total() == 30, 'Must remain 30!'

cart.add_item((lemon, 2), (apple, 10))
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs. = 20 грн
apple: 20 pcs. = 40 грн
Total: 60 грн
"""

assert cart.get_total() == 60, 'Total must be 60'