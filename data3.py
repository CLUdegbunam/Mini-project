import os
from typing import List

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#product function
def load_products(products: List[str]) ->None:
    products_list = []
    with open('products.txt', 'r') as products_file:
        contents = products_file.readlines()
        for line in contents:  
            products_list.append(line.strip())
    return products_list

def add_product(new_product):
    with open ("products.txt", "a") as products_file:
        products_file.write("\n")
        new_product = products_file.write(new_product)
        return new_product
    
def save_products( products: List[str]) -> None:
    products_list = load_products("products")
    with open('products.txt', 'w') as products_file:
        for product in products:
            products_file.write(product + '\n')
    return products_list

# couriers function
def load_couriers(couriers: List[str]) -> None:
    couriers_list = []
    with open('couriers.txt', 'r') as couriers_file:
        contents = couriers_file.readlines()
        for line in contents:  
            couriers_list.append(line.strip())
    return couriers_list

def add_courier(new_courier):
    with open ("couriers.txt", "a") as couriers_file:
        couriers_file.write("\n")
        new_courier = couriers_file.write(new_courier)
    return new_courier
         
def save_couriers(couriers: List[str]) -> None:
    couriers_list = load_couriers("couriers")
    with open('couriers.txt', 'w') as couriers_file:
        for courier in couriers:
            couriers_file.write(courier + '\n')
    return couriers_list