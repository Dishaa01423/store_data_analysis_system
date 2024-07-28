import csv
import random
from datetime import datetime, timedelta


# Function to generate a random date within a range
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


# Set up the data
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)
customers = [f"CUST{i:03d}" for i in range(1, 51)]  # 50 customers
products = [
    ("PROD001", "Laptop", 999.99),
    ("PROD002", "Smartphone", 599.99),
    ("PROD003", "Headphones", 149.99),
    ("PROD004", "Tablet", 399.99),
    ("PROD005", "Smartwatch", 249.99),
]

# Generate the data
data = []
for i in range(1, 1001):  # 1000 orders
    order_date = random_date(start_date, end_date)
    product = random.choice(products)
    quantity = random.randint(1, 5)

    data.append({
        "order_id": f"ORD{i:04d}",
        "customer_id": random.choice(customers),
        "order_date": order_date.strftime("%Y-%m-%d"),
        "product_id": product[0],
        "product_name": product[1],
        "product_price": product[2],
        "quantity": quantity
    })

# Write to CSV
with open('orders.csv', 'w', newline='') as csvfile:
    fieldnames = ["order_id", "customer_id", "order_date", "product_id", "product_name", "product_price", "quantity"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
