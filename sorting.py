
from logger import log


# ---------- Bubble Sort ----------
def bubble_sort(products, key, ascending=True):
    n = len(products)

    for i in range(n):
        for j in range(0, n - i - 1):
            a = getattr(products[j], key)
            b = getattr(products[j + 1], key)

            if (ascending and a > b) or (not ascending and a < b):
                products[j], products[j + 1] = products[j + 1], products[j]


# ---------- Convert Linked List to Array ----------
def linked_list_to_array(product_list):
    arr = []
    current = product_list.head
    while current:
        arr.append(current.product)
        current = current.next
    return arr


# ---------- Display ----------
# def display(products):
#     if not products:
#         print("❌ No products to display.")
#         return

#     for p in products:
#         print(
#             f"{p.id} | {p.name} | {p.price} | "
#             f"{p.category} | ⭐{p.rating} | Sales:{p.sales}"
#         )
def display(products):
    if not products:
        print("❌ No products to display.")
        return

    for p in products:
        print(f"ID: {p.id}")
        print(f"Name: {p.name}")
        print(f"Category: {p.category}")
        print(f"Price: {p.price}")
        print(f"Rating: ⭐ {p.rating}")
        print(f"Sales: {p.sales}")
        print("-----------------------------")  


# ---------- Sorting Menu ----------
def sorting_menu(product_list):
    while True:
        print("\n=== Sorting Menu ===")
        print("1. Sort by price")
        print("2. Sort by rating")
        print("3. Sort by sales")
        print("0. Back")

        choice = input("> ")

        if choice == "0":
            break

        if choice not in ["1", "2", "3"]:
            print("❌ Invalid option")
            continue

        order = input("Order (1=Ascending, 2=Descending): ")
        ascending = (order == "1")

        products = linked_list_to_array(product_list)

        if choice == "1":
            bubble_sort(products, "price", ascending)
            log("Sorted by price")
        elif choice == "2":
            bubble_sort(products, "rating", ascending)
            log("Sorted by rating")
        elif choice == "3":
            bubble_sort(products, "sales", ascending)
            log("Sorted by sales")

        display(products)