products = [
    {"name": "Leptop", "stock": 5},
    {"name": "Mobile", "stock": 10},
    {"name": "Tablet", "stock": 0}
]

out_of_stock = [product["name"] for product in products if product["stock"] == 0]

print("Out of products: ",out_of_stock)
