
from logger import log

MAX_HISTORY = 10

class History:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        # Remove if already exists
        self.products = [p for p in self.products if p.id != product.id]
        # Insert at beginning
        self.products.insert(0, product)
        # Keep size <= MAX_HISTORY
        if len(self.products) > MAX_HISTORY:
            self.products.pop()
        log(f"Product added to history: ID={product.id}")

    # def display_history(self):
    #     if not self.products:
    #         print("No recently viewed products.")
    #         return
    #     print("\n=== Recently Viewed Products ===")
    #     for p in self.products:
    #         print(f"{p.id} | {p.name} | {p.price} | {p.category} | ⭐{p.rating}")
    def display_history(self):
        if not self.products:
            print("No recently viewed products.")
            return
        print("\n=== Recently Viewed Products ===")
        for p in self.products:
            print(f"ID: {p.id}")
            print(f"Name: {p.name}")
            print(f"Category: {p.category}")
            print(f"Price: {p.price}")
            print(f"Rating: ⭐ {p.rating}")
            print(f"Sales: {p.sales}")
            print("-----------------------------")