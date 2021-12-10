from mp_functions import load_products, save_products, clear_screen, add_product, load_couriers, add_courier, save_couriers
print("WELCOME TO CAFE COFFEE")

main_menu = '''
MAIN MENU
---------
0. Save And Exit
1. Products Menu
2. Couriers Menu
3. Order Menu'''

products_menu = '''
PRODUCTS MENU
-------------
0. Return To Main Menu
1. Display Product list 
2. Create New Product
3. Update Product List
4. Delete Product
'''
couriers_menu = '''
0. Return To Main Menu
1. Display Courier List
2. Add New Courier
3. Update Courier List
4. Delete Courier'''

orders_menu = '''
0. Return To Main Menu
1. Display Orders Dictionary
'''


    
products_list = load_products("products.txt")
couriers_list = load_couriers("couriers.txt")

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
                products = load_products()
                print(f"Your products are: {products}")
            elif products_menu_options == 2:
                clear_screen()
                #Add new product
                products = load_products()
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
                products = load_products()
                products[index] = new_product
                save_products(products)
            elif products_menu_options == 4:
                clear_screen()
                products = load_products()
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
                couriers = load_couriers() 
                print(f"Your couriers are: {couriers}")
            elif couriers_menu_options == 2:
                clear_screen()
                 #Add new product
                couriers = load_couriers()
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
                couriers = load_couriers()
                couriers[index] = new_courier
                save_couriers(couriers)
            elif couriers_menu_options == 4:
                clear_screen()
               # delete courier
                couriers = load_couriers()
                try:
                    index = int(input("Enter courier index: "))
                except:
                    print("Invalid Entry")
                del couriers[index]
                save_couriers(couriers)
                
    # elif main_menu_options == 3:
    #      while(True):
    #         print(couriers_menu)
    #         orders_menu_options = int(input("Enter option: "))
    #         if orders_menu_options == 0:
    #             print("Return to main menu")
    #             break
    #         elif orders_menu_options == 1
                
                
 