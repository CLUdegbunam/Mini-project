import os
from typing import List, Dict
import csv

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Products Functions
def load_products(products: List[dict]):
    try:
        with open("products.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                products.append(row)
    except Exception as e:
        print("No file loaded")
    return products

def save_products(products: List[dict]):
    with open("products.csv", "w", newline='') as file:
        field_names = ["product_name", "price"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for product in products:
            writer.writerow(product)
    return products
       
# Couriers function
def load_couriers(couriers: List[Dict]):
    couriers = []
    try:
        with open("couriers.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                couriers.append(row)
    except Exception as e:
        print("No file loaded")
    return couriers

def save_couriers(couriers: List[dict]):
    with open("couriers.csv", "w", newline='') as file:
        field_names = ["courier_name", "phone"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        # instruct the writer to write the row
        for courier in couriers:
            writer.writerow(courier)
    return couriers

#orders function
def load_orders(orders: List[dict]) -> None:
    orders = []
    try:
        with open("orders.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                orders.append(row)
    except Exception as e:
        print("No file loaded")
    return orders

def save_orders(orders: List[dict]):
    with open("orders.csv", "w", newline='') as file:
        field_names = ["customer_name", "customer_address","customer_phone", "courier", "status"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        # instruct the writer to write the row
        for order in orders:
            writer.writerow(order)
    return orders