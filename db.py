import pymysql
import os
import typing

from pymysql.cursors import Cursor
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

def execute_query(sql):
    
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database, autocommit=True)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        
        # Execute
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        # Close down
        cursor.close()
    finally:
        connection.close()
    
    return rows

def execute_with_result_row_id(sql):
    try:
        connection = pymysql.connect(host, user, password, database, autocommit=True)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        row_id = cursor.lastrowid # Get the row ID
        cursor.close()
        return row_id
    finally:
        connection.close()
    

# Products Sql   
def get_products():
    sql = "select * from products"
    products = execute_query(sql)
    return products

def add_product(name: str, price: float):
    sql = f"insert into products (name, price) values ('{name}','{price}')"
    execute_query(sql)

def update_product(name: str, price: float, id: int):
    sql = f"UPDATE products SET name = '{name}', price = '{price}' WHERE id = '{id}'"
    execute_query(sql)

def delete_product(id: int):
    sql = f"DELETE FROM products WHERE id = '{id}'"
    execute_query(sql)

# Couriers Sql
def get_couriers():
    sql = "select * from couriers"
    couriers = execute_query(sql)
    return couriers

def add_courier(name: str, phone: int):
    sql = f"insert into couriers (name, phone) values ('{name}','{phone}')"
    execute_query(sql)

def update_courier(name: str, phone: int, id: int):
    sql = f"UPDATE couriers SET name = '{name}', phone = '{phone}' WHERE id = '{id}'"
    execute_query(sql)

def delete_courier(id: int):
    sql = f"DELETE FROM couriers WHERE id = '{id}'"
    execute_query(sql)

# Orders Sql
def get_orders():
    sql = "select * from orders"
    orders = execute_query(sql)
    return orders

def get_status():
    sql = "select * from status"
    status = execute_query(sql)
    return status


def add_order(customer_name: str, customer_address: str, customer_phone: int, courier_id: int, status_id: int, items:str):
    sql = f'''insert into orders (customer_name, customer_address, customer_phone, courier_id, status_id, items) 
         values ('{customer_name}', '{customer_address}', '{customer_phone}', '{courier_id}', '{status_id}', '{items}')'''
    execute_query(sql)

def update_order_status(status_id: int, id: int):
    sql = f"UPDATE orders SET status_id = '{status_id}' WHERE id = '{id}'"
    execute_query(sql)