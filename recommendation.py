

from logger import log


def recommend_products(product_list, target_product, max_results=5):
    recommendations = []

    current = product_list.head
    price_range = target_product.price * 0.2  # ±20%

    while current:
        p = current.product

        if p.id != target_product.id:
            same_category = (p.category == target_product.category)
            close_price = abs(p.price - target_product.price) <= price_range

            if same_category and close_price:
                recommendations.append(p)

        current = current.next

    log(f"Recommendations generated for product ID={target_product.id}")
    return recommendations[:max_results]


# def display_recommendations(products):
#     if not products:
#         print("No recommendations available.")
#         return

#     print("\n--- Recommended Products ---")
#     for p in products:
#         print(
#             f"{p.id} | {p.name} | {p.price} | "
#             f"{p.category} | ⭐{p.rating}"
#         )
def display_recommendations(products):
    if not products:
        print("No recommendations available.")
        return

    print("\n--- Recommended Products ---")
    for p in products:
        print(f"ID: {p.id}")
        print(f"Name: {p.name}")
        print(f"Category: {p.category}")
        print(f"Price: {p.price}")
        print(f"Rating: ⭐ {p.rating}")
        print(f"Sales: {p.sales}")
        print("-----------------------------")