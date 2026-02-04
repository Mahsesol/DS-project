# DS-project
# 🛒 Online Shop System (Console-Based)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Data Structure](https://img.shields.io/badge/Data%20Structure-Linked%20List-green.svg)](#)

A project for the **Data Structures and Algorithms** course of university.  
This project implements a **console-based online shop system** in Python, focusing on the **Linked List data structure**, modular design, and data persistence using JSON files.

---

This project simulates a simple online shop where users can:
- Manage products
- Search and sort products
- Add products to a shopping cart
- View recently viewed products
- Receive similar product recommendations

All data is loaded from the `products.json` file.

---

## Main Menu
After running the program:

1. **Product Management** – View, add, remove, and edit products  
2. **Search Products** – Search by ID, name, category, and price  
3. **Sort Products** – Sort products by price  
4. **Shopping Cart** – Manage shopping cart  
5. **Recently Viewed Products** – View browsing history  
0. **Exit** – Exit the program and display logs  

---

## Project Files
- `main.py` – Main menu and program entry point  
- `product_management.py` – Linked List implementation, product CRUD, product details  
- `search_menu.py` – Product searching and price Bubble Sort  
- `sorting.py` – Sorting menu  
- `cart.py` – Shopping cart logic  
- `history.py` – Recently viewed products history  
- `recommendation.py` – Similar product recommendation system  
- `logger.py` – System activity logging  
- `products.json` – Product database  
- `system.log` – System log file  

---

## Features
- Manual implementation of **Linked List**
- Full product management (CRUD)
- Search by:
  - ID
  - Name
  - Category
  - Lowest / Highest ⅓ priced products
- Price sorting (Bubble Sort – educational purpose)
- Shopping cart system
- Recently viewed products history
- Product recommendation based on category and price range
- JSON-based data persistence
- Activity logging system

---

## Key Components

### ProductLinkedList
- `load_from_json()`
- `save_to_json()`
- `find_by_id()`
- `add_product()`
- `remove_product()`
- `edit_product()`
- `view_product_details()`

### Search Functions
- `search_by_id()`
- `search_by_name()`
- `search_by_category()`
- `search_by_price_extreme()`

### Shopping Cart
- Add and remove products
- Display cart contents

### Recommendation System
- Suggests products based on:
  - Similar category
  - Similar price range (±20%)

---

## ▶️ How to Run
```bash
python main.py
```  

## Feedback

If you have any feedback, please reach out to us. <3 
## 
- [Liliarouhi](https://www.github.com/Liliarouhi)
- [Mahsesol](https://www.github.com/Mahsesol)

