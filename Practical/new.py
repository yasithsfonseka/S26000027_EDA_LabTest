products ={
    "P001": {"name": "Laptop", "price": 999.99, "category":"electronics"},
    "P002": {"name": "Smartphone", "price": 499.99, "category":"electronics"},
    "P003": {"name": "Headphones", "price": 199.99, "category":"electronics"},
    "P004": {"name": "Coffee Maker", "price": 79.99, "category":"home appliances"},
    "P005": {"name": "Blender", "price": 59.99  , "category":"home appliances"},
}
input_category = input("Enter a category to filter products: ")
threshold = float(input("Enter a price threshold: "))
total_price = 0
count = 0
for prod in products.values():
    if prod["category"] == input_category and prod["price"] > threshold:
        total_price += prod["price"]
        count += 1
if count > 0:
    average_price = total_price / count
    print(f"Average price of {input_category} products above {threshold} is {average_price:.2f}")
else:
    print(f"No {input_category} products found above {threshold}.")