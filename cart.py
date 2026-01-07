
from logger import log


# ===================== CART ITEM =====================
class CartItem:
    def __init__(self, product, quantity=1):
        self.product = product
        self.quantity = quantity
        self.next = None


# ===================== CART LINKED LIST =====================
class ShoppingCart:
    def __init__(self):
        self.head = None

    # ---------- ADD ----------
    def add_product(self, product):
        current = self.head

        while current:
            if current.product.id == product.id:
                current.quantity += 1
                log(f"Cart updated: ID={product.id}, quantity={current.quantity}")
                return
            current = current.next

        new_item = CartItem(product)
        new_item.next = self.head
        self.head = new_item
        log(f"Product added to cart: ID={product.id}")

    # ---------- REMOVE ----------
    def remove_product(self, product_id):
        prev, current = None, self.head

        while current:
            if current.product.id == product_id:
                if current.quantity > 1:
                    current.quantity -= 1
                    log(f"Cart quantity decreased: ID={product_id}")
                else:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    log(f"Product removed from cart: ID={product_id}")
                return
            prev, current = current, current.next

        print("❌ Product not in cart")

    # ---------- DISPLAY ----------
    # def display_cart(self):
    #     if not self.head:
    #         print("🛒 Cart is empty.")
    #         return

    #     print("\n=== Shopping Cart ===")
    #     current = self.head
    #     total = 0

    #     while current:
    #         p = current.product
    #         subtotal = p.price * current.quantity
    #         total += subtotal
    #         print(
    #             f"{p.id} | {p.name} | "
    #             f"Qty: {current.quantity} | Subtotal: {subtotal}"
    #         )
    #         current = current.next

    #     print(f"\nTotal Price: {total}")
    def display_cart(self):
        if not self.head:
            print("🛒 Cart is empty.")
            return

        print("\n=== Shopping Cart ===")
        current = self.head
        total = 0

        while current:
            p = current.product
            subtotal = p.price * current.quantity
            total += subtotal
            print(f"ID: {p.id}")
            print(f"Name: {p.name}")
            print(f"Category: {p.category}")
            print(f"Price: {p.price}")
            print(f"Rating: ⭐ {p.rating}")
            print(f"Sales: {p.sales}")
            print(f"Quantity: {current.quantity} | Subtotal: {subtotal}")
            print("-----------------------------")
            current = current.next

        print(f"\nTotal Price: {total}")

    # ---------- TOTAL ----------
    def get_total_price(self):
        total = 0
        current = self.head
        while current:
            total += current.product.price * current.quantity
            current = current.next
        return total