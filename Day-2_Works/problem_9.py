import csv

# Variables to store the highest revenue product
highest_product = ""
highest_quantity = 0
highest_price = 0
highest_revenue = 0

# Open and read the CSV file
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = float(row["price"])

        revenue = quantity * price

        # Check if this is the highest revenue so far
        if revenue > highest_revenue:
            highest_revenue = revenue
            highest_product = product
            highest_quantity = quantity
            highest_price = price

# Print the highest revenue product
print("------ Highest Revenue Product ------")
print(f"Product  : {highest_product}")
print(f"Quantity : {highest_quantity}")
print(f"Price    : ₹{highest_price}")
print(f"Revenue  : ₹{highest_revenue}")