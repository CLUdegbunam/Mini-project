from menus import main_menu, products_menu, couriers_menu, orders_menu
import db
from final_data import clear_screen

print("WELCOME TO CAFE COFFEE")

#main menu options
while(True):
    print(main_menu)
    main_menu_options = int(input("Enter option: "))
    if (main_menu_options == 0):
        print("Exit\nGoodBye")
        break
        
    elif main_menu_options == 1:
    # product menu
        while(True):
            print(products_menu)
            products_menu_options = int(input("Enter option: "))
            if products_menu_options == 0:
                print("Returned to main menu")
                break

            elif products_menu_options == 1:
                clear_screen()
                products = db.get_products()
                for product in products:
                    print(f"{product['id']}. {product['name']} : £{product['price']}")

            elif products_menu_options == 2: 
                clear_screen()
                db.get_products()
                #Add new product
                name = input("Please add new product: ")
                price = float(input("Enter Price: "))
                db.add_product(name, price)
                
            elif products_menu_options == 3:
                clear_screen()
                products = db.get_products()
                # Update Product
                for product in products:
                    print(f"{product['id']}. {product['name']}")
                id = int(input("Enter product id: "))
                name = input("Enter New product: ")
                price = float(input("Enter Price: "))

                if input == None:
                    print("Returned to Products Menu")
                    break
                else:
                    db.update_product(name, price, id)
                               
            elif products_menu_options == 4:
                clear_screen()
                #Delete product
                products = db.get_products()
                for product in products:
                    print(f"{product['id']}. {product['name']}")
                try:           
                    id = int(input("Enter product id: "))
                    db.delete_product(id)
                except:
                    print("Invalid Entry")
                
               
    elif main_menu_options == 2:
        # couriers menu            
        while(True):
            print(couriers_menu)
            couriers_menu_options = int(input("Enter option: "))
            if couriers_menu_options == 0:
                print("Return to main menu")
                break
            
            elif couriers_menu_options == 1:
                clear_screen() 
                couriers = db.get_couriers()
                for courier in couriers:
                    print(f"{courier['id']}. {courier['name']}, {courier['phone']}")
            
            elif couriers_menu_options == 2:
                clear_screen()
                db.get_couriers()
                #Add New Courier
                name = input("Please add new courier: ")
                phone = int(input("Enter Phone: "))
                db.add_courier(name, phone)

            elif couriers_menu_options == 3:
                clear_screen() 
                # Update Courier
                couriers = db.get_couriers()
                for courier in couriers:
                    print(f"{courier['id']}. {courier['name']}")
                id = int(input("Enter Courier id: "))
                name = input("Enter New courier: ")
                phone = int(input("Enter Phone: "))

                if input == None:
                    print("Returned to Couriers Menu")
                    break
                else:
                    db.update_courier(name, phone, id)
                               
            elif products_menu_options == 4:
                clear_screen()
                #Delete product
                couriers = db.get_couriers()
                for courier in couriers:
                    print(f"{courier['id']}. {courier['name']}")
                try:           
                    id = int(input("Enter Courier id: "))
                    db.delete_courier(id)
                except:
                    print("Invalid Entry")
                
            
    elif main_menu_options == 3:
        #Orders Menu
         while(True):
            print(orders_menu)
            orders_menu_options = int(input("Enter option: "))
            if orders_menu_options == 0:
                print("Return to main menu")
                break
            elif orders_menu_options == 1:
                clear_screen()
                orders = db.get_orders()
                for order in orders:
                    print(f"{order['id']}, {order['customer_name']}, {order['customer_address']}, {order['customer_phone']}, {order['courier_id']}, {order['status_id']}, {order['items']}")
    
            elif(orders_menu_options == 2): # Create order
                clear_screen()
                # Collect some data
                customer_name = input("Enter Name: ")
                customer_address = input("Enter Address: ")
                customer_phone = int(input("Enter Phone Number: "))
                couriers = db.get_couriers()
                for courier in couriers:
                    print(f"{courier['id']}. {courier['name']}")
                courier_id = int(input("Enter Courier id: "))
                status = db.get_status()
                for s in status:
                    print(f"{s['status_id']}. {s['status_name']}")
                status_id = int(input("Enter Status id: "))
                items = input("Enter items: ")
                db.add_order(customer_name, customer_address, customer_phone, courier_id, status_id, items)
                        
            elif(orders_menu_options == 3): # update order status
                clear_screen()
                orders = db.get_orders()
                for order in orders:
                    print(f"{order['id']}, {order['customer_name']}, {order['customer_address']}, {order['customer_phone']}, {order['courier_id']}, {order['status_id']}, {order['items']}")
                id = int(input("Enter Order id: "))
                status = db.get_status()
                for s in status:
                    print(f"{s['status_id']}. {s['status_name']}")
                status_id = int(input("Enter Status id: "))
                db.update_order_status(status_id, id)

               
            # elif(orders_menu_options == 4):
            #     load_orders(orders_list)
            #     for index, order in enumerate(orders_list):
            #          print(index, order)
            #     orders_index = int(input("Enter Order Index: "))
                        
            # elif(orders_menu_options == 5):
            #     pass
               