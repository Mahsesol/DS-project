from logger import log


def bubble_sort_by_price(products):
    n = len(products)
    for i in range(n):
        for j in range(0, n - i - 1):
            if products[j].price > products[j + 1].price:
                products[j], products[j + 1] = products[j + 1], products[j]


def display_results(results):
    if not results:
        print("❌ هیچ محصولی یافت نشد.")
        return

    for p in results:
        print(f"ID: {p.id}")
        print(f"Name: {p.name}")
        print(f"Category: {p.category}")
        print(f"Price: {p.price}")
        print(f"Rating: ⭐ {p.rating}")
        print(f"Sales: {p.sales}")
        print("-----------------------------")


# def search_by_name(product_list, keyword,cart=None,history=None):
#     results = []
#     current = product_list.head
#     while current:
#         if keyword.lower() in current.product.name.lower():
#             results.append(current.product)
#         current = current.next
#     log(f"Search by name: {keyword}")
 
#     return results
def search_by_name(product_list, keyword, history=None, cart=None):
    results = []
    current = product_list.head
    while current:
        if keyword.lower() in current.product.name.lower():
            results.append(current.product)
        current = current.next
    product = results[0]
    print("\n===== Product Details =====")
    print(f"ID: {product.id}")
    print(f"Name: {product.name}")
    print(f"Category: {product.category}")
    print(f"Price: {product.price}")
    print(f"Rating: ⭐ {product.rating}")
    print(f"Sales: {product.sales}")
    log(f"User searched by name: {keyword}, found {len(results)} products")

    if results and history is not None:
        last_product = results[0] 
        history.add_product(last_product)
        if cart is not None:
            choice = input(f"Do you want to add '{last_product.name}' to cart? (y/n): ").lower()
            if choice == 'y':
                cart.add_product(last_product)
                print("✅ Product added to cart")
                log(f"Product added to cart from search: ID={last_product.id}")

    return results



def search_by_category(product_list, category):
    results = []
    current = product_list.head
    while current:
        if current.product.category.lower() == category.lower():
            results.append(current.product)
        current = current.next
    log(f"Search by category: {category}")
    return results


def search_by_price_extreme(product_list, mode):
    products = []
    current = product_list.head
    while current:
        products.append(current.product)
        current = current.next

    if not products:
        return []

    bubble_sort_by_price(products)
    k = max(1, len(products) // 3)

    if mode == "min":
        log("Search lowest 1/3 prices")
        return products[:k]
    else:
        log("Search highest 1/3 prices")
        return products[-k:]


# def search_by_id(product_list, pid):
#     current = product_list.head
#     while current:
#         if current.product.id == pid:
#             log(f"Search by ID: {pid}")
#             return [current.product]
#         current = current.next
#     log(f"Search by ID: {pid} – not found")
#     return []

def search_by_id(product_list, pid, history=None, cart=None):
    current = product_list.head
    while current:
        if current.product.id == pid:
            product = current.product
             
            print("\n===== Product Details =====")
            print(f"ID: {product.id}")
            print(f"Name: {product.name}")
            print(f"Category: {product.category}")
            print(f"Price: {product.price}")
            print(f"Rating: ⭐ {product.rating}")
            print(f"Sales: {product.sales}")
            log(f"User searched by ID: {pid}, found product")
            if history is not None:
                history.add_product(product)
            if cart is not None:
                choice = input(f"Do you want to add '{product.name}' to cart? (y/n): ").lower()
                if choice == 'y':
                    cart.add_product(product)
                    print("✅ Product added to cart")
                    log(f"Product added to cart from search: ID={product.id}")
            return [product]
        current = current.next

    log(f"User searched by ID: {pid}, not found")
    return []


def search_menu(product_list,cart=None,history=None):
    while True:
        print("\n=== Search Menu ===")
        print("1. Search by ID")
        print("2. Search by name")
        print("3. Search by category")
        print("4. Show lowest 1/3 prices")
        print("5. Show highest 1/3 prices")
        print("0. Back")

        choice = input("> ")

        if choice == "1":
            try:
                pid = int(input("Product ID: "))
                display_results(search_by_id(product_list, pid,history,cart))
            except ValueError:
                print("❌ Invalid ID")

        elif choice == "2":
            key = input("Product name: ")
            display_results(search_by_name(product_list, key,history,cart))

        elif choice == "3":
            cat = input("Category (Digital / Clothing / Home / Book): ")
            display_results(search_by_category(product_list, cat))

        elif choice == "4":
            display_results(search_by_price_extreme(product_list, "min"))

        elif choice == "5":
            display_results(search_by_price_extreme(product_list, "max"))

        elif choice == "0":
            break
        else:
            print("❌ Invalid option")