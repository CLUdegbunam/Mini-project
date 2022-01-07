from data import load_orders, load_products, save_products, clear_screen,load_couriers,save_couriers, save_orders
from menus import main_menu, products_menu, couriers_menu, orders_menu

print("WELCOME TO CAFE COFFEE")

products_list = load_products([])
couriers_list = load_couriers([])
orders_list = load_orders([])
#print(orders_list)

#main menu options
while(True):
    print(main_menu)
    main_menu_options = int(input("Enter option: "))
    if (main_menu_options == 0):
        save_products(products_list)
        save_couriers(couriers_list)
        save_orders(orders_list)
        print("Exit\nGoodBye")
        break
        
    elif main_menu_options == 1:
    # product menu
        while(True):
            print(products_menu)
            products_menu_options = int(input("Enter option: "))
            if products_menu_options == 0:
                print("Return to main menu")
                break
            elif products_menu_options == 1:
                clear_screen()
                print(f"Your products are {products_list}")
            elif products_menu_options == 2:
                clear_screen()
                #Add new product
                product_name = input("Please add new product: ")
                price = float(input("Enter Price: "))
                new_product = {
                                "product_name": product_name,
                                "price": price
                                }
                products_list.append(new_product)
                
            elif products_menu_options == 3:
                clear_screen()
                # Update Product
                for index, product in enumerate(products_list):
                    print(index, product)
                product_index = int(input("Enter product Index: "))
                product_to_update = products_list[product_index]
                updated_product_name = input("Enter New product: ")
                updated_price = float(input("Enter Price: "))
                product_to_update.update({"product_name": updated_product_name, 
                                          "price": updated_price})
               
            elif products_menu_options == 4:
                clear_screen()
                #Delete product
                for index, product in enumerate(products_list):
                    print(index, product)
                try:
                    index = int(input("Enter product index: "))
                except:
                     print("Invalid Entry")
                del products_list[index]
               
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
                print(f"Your couriers are: {couriers_list}")
            elif couriers_menu_options == 2:
                clear_screen()
                 #Add new courier
                courier_name = input("Please add new courier: ")
                phone = int(input("Enter Phone Number: "))
                new_courier = {
                                "courier_name": courier_name,
                                "phone": phone
                                }
                couriers_list.append(new_courier)
                
            elif couriers_menu_options == 3:
                clear_screen()
                # Update courier
                for index, courier in enumerate(couriers_list):
                    print(index, courier)
                courier_index = int(input("Enter courier Index: "))
                courier_to_update = couriers_list[courier_index]
                updated_courier_name = input("Enter New courier: ")
                updated_phone = int(input("Enter Phone: "))
                courier_to_update.update({"courier_name": updated_courier_name, 
                                          "phone": updated_phone})
                   
            elif couriers_menu_options == 4:
                clear_screen()
               # delete courier
                for index, courier in enumerate(couriers_list):
                    print(index, courier)
                try:
                    index = int(input("Enter courier index: "))
                except:
                    print("Invalid Entry")
                del couriers_list[index]
                
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
                for order in orders_list:
                    print(f"Order: {order}")
            elif(orders_menu_options == 2):
                clear_screen()
                # Collect some data
                customer_name = input("Enter Name: ")
                customer_address = input("Enter Address: ")
                customer_phone_number = int(input("Enter Phone Number: "))
                load_couriers(couriers_list)
                for index, courier in enumerate(couriers_list):
                    print(index, courier)

                courier = int(input("Enter Courier Index: "))
                status = input("Enter Status: ")
                new_order = {
                            "customer_name" : customer_name,
                            "customer_address" : customer_address,
                            "customer_phone": customer_phone_number,
                            "courier": courier,
                            "status": status
                            }
                orders_list.append(new_order)
                        
            elif(orders_menu_options == 3):
                #load_orders(orders_list)
                for index, order in enumerate(orders_list):
                    print(index, order)
                order_index = int(input("Enter Order Index: "))
                order_to_update = orders_list[order_index]
                updated_status = input("Enter New Status: ")
                #order_to_update["status"] = updated_status
                order_to_update.update({"status": updated_status})
               
            # elif(orders_menu_options == 4):
            #     load_orders(orders_list)
            #     for index, order in enumerate(orders_list):
            #          print(index, order)
            #     orders_index = int(input("Enter Order Index: "))
                        
            elif(orders_menu_options == 5):
                pass