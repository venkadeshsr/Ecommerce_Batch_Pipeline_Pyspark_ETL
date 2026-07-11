import os
import random
from datetime import datetime, timedelta

import pandas as pd
from faker import Faker

fake = Faker()

# -----------------------------------------
# Create raw folder if it doesn't exist
# -----------------------------------------

RAW_FOLDER = "./data/raw"
os.makedirs(RAW_FOLDER, exist_ok=True)

# -----------------------------------------
# Master Data
# -----------------------------------------

products = [
    "Laptop",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Tablet",
    "Printer",
    "Headphones",
    "Camera",
    "Speaker",
    "Mobile"
]

categories = {
    "Laptop": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories",
    "Monitor": "Electronics",
    "Tablet": "Electronics",
    "Printer": "Office",
    "Headphones": "Accessories",
    "Camera": "Electronics",
    "Speaker": "Accessories",
    "Mobile": "Electronics"
}

regions = [
    "North",
    "South",
    "East",
    "West"
]

# -----------------------------------------
# Generate Random Sales Records
# -----------------------------------------

records = []

number_of_records = random.randint(10000, 30000)

for _ in range(number_of_records):

    product = random.choice(products)
    category = categories[product]

    quantity = random.randint(1, 10)

    sales = round(random.uniform(100, 5000), 2)

    profit = round(sales * random.uniform(0.05, 0.30), 2)

    order_date = (
        datetime.now() -
        timedelta(days=random.randint(0, 30))
    ).strftime("%Y-%m-%d")

    records.append([
        order_date,
        product,
        category,
        random.choice(regions),
        quantity,
        sales,
        profit
    ])

# -----------------------------------------
# Create DataFrame
# -----------------------------------------

df = pd.DataFrame(
    records,
    columns=[
        "Order Date",
        "Product Name",
        "Category",
        "Region",
        "Quantity",
        "Sales",
        "Profit"
    ]
)

# -----------------------------------------
# File Name
# -----------------------------------------

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

file_name = f"ecommerce_sales_data{timestamp}.csv"

file_path = os.path.join(RAW_FOLDER, file_name)

# -----------------------------------------
# Save CSV
# -----------------------------------------

df.to_csv(file_path, index=False)

print("=" * 60)
print("New Sales File Generated Successfully")
print("=" * 60)
print(f"File Name : {file_name}")
print(f"Rows      : {len(df)}")
print(f"Location  : {file_path}")
print("=" * 60)