

import json
from logger import log
from recommendation import recommend_products, display_recommendations
from history import History

# ===================== GLOBAL HISTORY =====================
# history = History()

# ===================== PRODUCT =====================
class Product:
    def __init__(self, id, name, price, category, rating, sales):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.rating = rating
        self.sales = sales

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "rating": self.rating,
            "sales": self.sales
        }


# ===================== NODE =====================
class Node:
    def __init__(self, product):
        self.product = product
        self.next = None


# ===================== LINKED LIST =====================
class ProductLinkedList:
    def __init__(self):
        self.head = None

    # ---------- LOAD & SAVE ----------
    def load_from_json(self, filename="products.json"):
        self.head = None
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for item in json.load(f):
                    self._add_to_head(Product(**item))
            log("Products loaded")
        except Exception:
            log("Failed to load products.json – empty list used")

    def save_to_json(self, filename="products.json"):
        data = []
        current = self.head
        while current:
            data.append(current.product.to_dict())
            current = current.next
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # ---------- INTERNAL ----------
    def _add_to_head(self, product):
        node = Node(product)
        node.next = self.head
        self.head = node

    # ---------- BASIC OPS ----------
    def find_by_id(self, pid):
        current = self.head
        while current:
            if current.product.id == pid:
                return current.product
            current = current.next
        return None

    # def display_all(self):
    #     current = self.head
    #     if not current:
    #         print("No products available.")
    #         return
    #     while current:
    #         p = current.product
    #         print(f"{p.id} | {p.name} | {p.price} | {p.category}")
    #         current = current.next
    def display_all(self):
            current = self.head
            if not current:
               print("No products available.")
               return
            while current:
               p = current.product
               print(f"ID: {p.id}")
               print(f"Name: {p.name}")
               print(f"Category: {p.category}")
               print(f"Price: {p.price}")
               print(f"Rating: ⭐ {p.rating}")
               print(f"Sales: {p.sales}")
               print("-----------------------------")  # خط جداکننده
               current = current.next

    # ---------- CRUD ----------
    def add_product(self, product):
        if self.find_by_id(product.id):
            print("❌ Duplicate ID")
            return
        self._add_to_head(product)
        self.save_to_json()
        log(f"Product added: {product.id}")

    def remove_product(self, pid):
        prev, cur = None, self.head
        while cur:
            if cur.product.id == pid:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self.save_to_json()
                log(f"Product removed: {pid}")
                return
            prev, cur = cur, cur.next
        print("❌ Product not found")

    def edit_product(self, pid, **kwargs):
        p = self.find_by_id(pid)
        if not p:
            print("❌ Product not found")
            return
        for k, v in kwargs.items():
            if v is not None:
                setattr(p, k, v)
        self.save_to_json()
        log(f"Product edited: {pid}")

    # ---------- VIEW DETAILS + RECOMMEND + HISTORY ----------
    def view_product_details(self,cart=None,history=None):
        try:
            pid = int(input("Enter product ID: "))
        except ValueError:
            print("❌ Invalid ID")
            return

        product = self.find_by_id(pid)
        if not product:
            print("❌ Product not found")
            log(f"View failed: ID={pid}")
            return

        # نمایش جزئیات
        print("\n===== Product Details =====")
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Category: {product.category}")
        print(f"Price: {product.price}")
        print(f"Rating: ⭐ {product.rating}")
        print(f"Sales: {product.sales}")

        log(f"Viewed product: ID={pid}")

        # پیشنهاد کالا
        recs = recommend_products(self, product)
        display_recommendations(recs)

        # اضافه به تاریخچه
        if history is not None:
            history.add_product(product)
        # گزینه اضافه به سبد خرید
        if cart is not None:
            choice = input("Do you want to add this product to cart? (y/n): ").lower()
            if choice == 'y':
                 cart.add_product(product)
                 print("✅ Product added to cart")
                 log(f"Product added to cart from details: ID={product.id}")


# ===================== PRODUCT MANAGEMENT MENU =====================
def product_management_menu(product_list, cart=None, history=None):
    VALID_CATEGORIES = ["Digital", "Clothing", "Home", "Book"]
    while True:
        print("\n=== Product Management ===")
        print("1. Show all products")
        print("2. View product details")
        print("3. Add product")
        print("4. Remove product")
        print("5. Edit product")
        print("0. Back")

        choice = input("> ")

        if choice == "1":
            product_list.display_all()

        elif choice == "2":
            product_list.view_product_details(cart,history)

        # elif choice == "3":
        #     try:
        #         p = Product(
        #             int(input("ID: ")),
        #             input("Name: "),
        #             float(input("Price: ")),
        #             input("Category"),
        #             float(input("Rating: ")),
        #             int(input("Sales: "))
        #         )
        #         product_list.add_product(p)
        #     except ValueError:
        #         print("❌ Invalid input")
        
        elif choice == "3":  # Add product
            try:
              pid = int(input("ID: "))
              name = input("Name: ")
              price = float(input("Price: "))

              while True:
                    print("Available categories:", ", ".join(VALID_CATEGORIES))
                    category = input("Category: ")
                    if category in VALID_CATEGORIES:
                        break
                    print("❌ Invalid category, try again.")

              rating = float(input("Rating: "))
              sales = int(input("Sales: "))

              p = Product(pid, name, price, category, rating, sales)
              product_list.add_product(p)
            except ValueError:
             print("❌ Invalid input")
          
        elif choice == "4":
            try:
                product_list.remove_product(int(input("ID: ")))
            except ValueError:
                print("❌ Invalid ID")

        elif choice == "5":
            try:
                pid = int(input("ID: "))
                name = input("New name (Enter skip): ") or None
                price = input("New price: ")
                price = float(price) if price else None
                category = input("New category: ") or None
                rating = input("New rating: ")
                rating = float(rating) if rating else None
                sales = input("New sales: ")
                sales = int(sales) if sales else None

                product_list.edit_product(
                    pid,
                    name=name,
                    price=price,
                    category=category,
                    rating=rating,
                    sales=sales
                )
            except ValueError:
                print("❌ Invalid input")

        elif choice == "0":
            break
        else:
            print("❌ Invalid option")