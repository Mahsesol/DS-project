from product_management import ProductLinkedList, product_management_menu
from search_menu import search_menu
from sorting import sorting_menu
from cart import ShoppingCart
from history import History
from logger import show_logs

# ===================== INITIALIZATION =====================
products = ProductLinkedList()
products.load_from_json()
history = History()
cart = ShoppingCart()

# ===================== HELPER MENUS =====================

def recently_viewed_menu():
    history.display_history()


# ===================== MAIN MENU =====================
def main_menu():
    while True:
        print("\n=== Online Shop System ===")
        print("1. Product Management")
        print("2. Search Products")
        print("3. Sort Products")
        print("4. Shopping Cart")
        print("5. Recently Viewed Products")
        print("0. Exit")

        choice = input("> ")

        if choice == "1":
            product_management_menu(products, cart,history)

        elif choice == "2":
            search_menu(products,cart,history)

        elif choice == "3":
            sorting_menu(products)

        elif choice == "4":
            while True:
                print("\n=== Shopping Cart Menu ===")
                print("1. Add product to cart")
                print("2. Remove product from cart")
                print("3. View cart")
                print("0. Back")

                c = input("> ")

                if c == "1":
                    try:
                        pid = int(input("Enter product ID to add: "))
                        p = products.find_by_id(pid)
                        if not p:
                            print("❌ Product not found")
                            continue
                        cart.add_product(p)
                        print("✅ Product added to cart")
                    except ValueError:
                        print("❌ Invalid ID")

                elif c == "2":
                    try:
                        pid = int(input("Enter product ID to remove: "))
                        cart.remove_product(pid)
                    except ValueError:
                        print("❌ Invalid ID")

                elif c == "3":
                    cart.display_cart()

                elif c == "0":
                    break
                else:
                    print("❌ Invalid option")

        elif choice == "5":
            recently_viewed_menu()

        elif choice == "0":
            print("\nExiting program...")
            show_logs()
            break

        else:
            print("❌ Invalid option")


# ===================== ENTRY POINT =====================
if __name__ == "__main__":
  main_menu()