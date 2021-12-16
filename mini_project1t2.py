from data import load_orders, load_products, save_products, clear_screen, add_product, load_couriers, add_courier, save_couriers
from menus import main_menu, products_menu, couriers_menu, orders_menu

print("WELCOME TO CAFE COFFEE")

products_list = load_products("products.txt")
couriers_list = load_couriers("couriers.txt")
orders_list = load_orders("orders.csv")
#print(orders_list)

#main menu options
while(True):
    print(main_menu)
    main_menu_options = int(input("Enter option: "))
    if (main_menu_options == 0):
        save_products("products.txt", products_list)
        save_couriers("couriers.txt", couriers_list)
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
                products = load_products(products_list)
                print(f"Your products are: {products}")
            elif products_menu_options == 2:
                clear_screen()
                #Add new product
                products = load_products(products_list)
                new_product = input("Please add new product: ")
                new_product = add_product(new_product)
            elif products_menu_options == 3:
                clear_screen()
                # Update Product
                try:
                    index = int(input("Enter product index:  "))
                except:
                     print("Invalid Entry")
                new_product = input("Please enter product: ")
                products = load_products(products_list)
                products[index] = new_product
                save_products(products)
            elif products_menu_options == 4:
                clear_screen()
                products = load_products(products_list)
                try:
                    index = int(input("Enter product index: "))
                except:
                     print("Invalid Entry")
                del products[index]
                save_products(products)
               
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
                couriers = load_couriers(couriers_list) 
                print(f"Your couriers are: {couriers}")
            elif couriers_menu_options == 2:
                clear_screen()
                 #Add new product
                couriers = load_couriers(couriers_list)
                new_courier = input("Please add new courier: ")
                new_courier = add_courier(new_courier)
            elif couriers_menu_options == 3:
                clear_screen()
                # Update courier
                try:
                    index = int(input("Enter courier index: "))
                except:
                    print("Invalid Entry")
                new_courier = input("Please enter courier: ")
                couriers = load_couriers(couriers_list)
                couriers[index] = new_courier
                save_couriers(couriers)
            elif couriers_menu_options == 4:
                clear_screen()
               # delete courier
                couriers = load_couriers(couriers_list)
                try:
                    index = int(input("Enter courier index: "))
                except:
                    print("Invalid Entry")
                del couriers[index]
                save_couriers(couriers)
                
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
                # Order: {'customer_name': 'john', 'customer_address': '55 iceroad london e15 3qj', 
                # 'customer_phone': '0744', 'courier': '0', 'status': 'pending'
                # }
                new_order = {
                    "customer_name" : customer_name,
                    "customer_address" : customer_address,
                    "customer_phone_number": customer_phone_number,
                    "courier": courier,
                    "status": status
                    }
                orders_list.append(new_order)
            elif(orders_menu_options == 3):
                for index, order in enumerate(orders_list):
                    print(index, order)
                    orders = int(input("Enter Order Index: "))
                    for index, status in enumerate(orders_list):
                        print(index, status)
                        updated_status = input("Enter New Status: ")
                        orders_list.append(updated_status)
            elif(orders_menu_options == 4):
                pass
            elif(orders_menu_options == 5):
                pass