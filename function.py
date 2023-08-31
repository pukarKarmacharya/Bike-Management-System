import csv
import datetime

def display_message(msg):
    print("| ----------------------------------------------- |")
    print("| "+msg)
    print("| ----------------------------------------------- |")
    
def display_main_menu():
    print("/---------------------------------------------\\")
    print("|1. Sell Bikes.                               |")
    print("|2. Order Bikes.                              |")
    print("|3. Bikes Avaliable.                          |")
    print("|4. Exit.                                     |")
    print("\---------------------------------------------/")
      
def return_2d_list():
    file = open("bikes.csv","r")
    listNew = []
    for line in file:
        line = line.replace("\n", "") 
        line = line.split(",")
        listNew.append(line) 
    file.close()
    return listNew

def get_bike():
    print("")
    print("| -------------------------------------------------------------------------------------- |")
    print("| Bike ID\tBike-Name\tCompany\t\tColor\t\tStock\tPrice\t\t |")
    print("| -------------------------------------------------------------------------------------- |")

    bike = []
    bike = return_2d_list()
    bike_id = 1

    for i in range(len(bike)):
        print("| "+str(bike_id)+"\t\t"+str(bike[i][0])+"\t\t"+str(bike[i][1])+"\t\t"+str(bike[i][2])+ "\t\t"+str(bike[i][3]) +"\t"+"NPR "+ str(bike[i][4])+"\t |")
        bike_id+=1
        
    print("| -------------------------------------------------------------------------------------- |")

def try_empty_string(msg):
    while True:
        try:
            name = input(msg)
            if not name:
                raise ValueError("Empty String. Please enter a string.")
            else:
                break
        except ValueError as e:
            print(e)
    return name

def try_invalid_int(msg):
    check = True
    while check:
        try:
            value = int(input(msg))
            check = False
            if(value <0):
                display_message("Please enter a positive number.")
                print()
                check = True
            if(value == 0):
                display_message("Please enter a higher number.")
                print()
                check = True   
        except:
            display_message("Invalid entry. Please enter a number.")
            print()
            check = True
    return value

def validate_bike_Id():
    valid_bike_id = try_invalid_int("Enter a value for Bike ID: ")
    while valid_bike_id > len(return_2d_list()):
        display_message("Enter a valid Bike ID")
        print()
        print(get_bike())
        valid_bike_id = try_invalid_int("Enter a valid Bike ID: ")
    return valid_bike_id

def validate_quantity(bike_id):
    qty = try_invalid_int("Enter a value for quantity: ")
    stock_qty = return_2d_list()[bike_id - 1][3]
    while qty > int(stock_qty) :
        display_message("Invalid Quantity")
        print()
        print(f"There are only {str(stock_qty)} unit in stock.")
        print(get_bike())
        qty = try_invalid_int("Enter a valid quantity: ")
    return(qty)

def sell_quantity(bike_id, quantity):
    bikes = return_2d_list()
    bikes[bike_id - 1][3] = int(bikes[bike_id - 1][3]) - quantity
    update_stock(bikes)
    print()

def order_quantity(bikeId, quantity):
    bikes = return_2d_list()
    bikes[bikeId - 1][3] = int(bikes[bikeId - 1][3]) + quantity
    update_stock(bikes)
    print()

def update_stock(listNew):
    file = open("bikes.csv", "w")  
    for list_1d in listNew:
        file.write(str(list_1d[0]) + "," + str(list_1d[1]) + "," + str(list_1d[2]) + "," + str(list_1d[3]) + "," + str(list_1d[4]))
        file.write("\n")
    file.close()

def new_order(new_dict):
    file = open("bikes.csv", "a")
    for key in new_dict:
        file.write(str(new_dict[key][0]) + "," + str(new_dict[key][1]) + "," + str(new_dict[key][2]) + "," + str(new_dict[key][3]) + "," + str(new_dict[key][4]))
        file.write("\n")
    file.close()


def get_datetime_integer():
    import datetime
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    return second+minute+hour+day+month+year

def generate_bill(typeOfTransaction, name, todaysDate, bike_dict):
    import datetime
    total_price = 0
    i = 1
    printed_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    filename = name[0] + "_" + get_datetime_integer() +"_"+ typeOfTransaction
    
    file = open(filename+".txt", "w")
    file.write("| ----------------------------------------------------------------------------- |")
    file.write("\n")
    file.write("|                         PYTHON TRADING COMPANY Pvt. Ltd.                      |")
    file.write("\n")
    file.write("|                    Kantipath, Kathmandu, Phone No. :5355555                   |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                        VAT Registration No. : 600230005                       |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                                    INVOICE                                    |")
    file.write("\n")
    file.write("| ----------------------------------------------------------------------------- |")
    file.write("\n")
    
    
    print("| ----------------------------------------------------------------------------- |")
    print("|                         PYTHON TRADING COMPANY Pvt. Ltd.                      |")
    print("|                    Kantipath, Kathmandu, Phone No. :5355555                   |")
    print("|                                                                               |")
    print("|                        VAT Registration No. : 600230005                       |")
    print("|                                                                               |")
    print("|                                    INVOICE                                    |")
    print("| ----------------------------------------------------------------------------- |")

    if typeOfTransaction == "sale":
        file.write("| Invoice No:\t\t"+str(get_datetime_integer())+"\t\t\t\t\t\t\t  |")
        file.write("\n")
        file.write("| Invoice Date:\t\t" + str(todaysDate) + "\t\t\t\t\t\t\t\t  |")
        file.write("\n")
        file.write("| Invoice Type:\t\tSale                                                    |")
        file.write("\n")
        file.write("| Buyer Name:\t\t"+str(name[0]))
        file.write("\n")
        file.write("| Buyer Address:\t\t"+str(name[1]))
        file.write("\n")
        file.write("| Buyer Contact No:\t"+str(name[2]))
        file.write("\n")
        file.write("| ----------------------------------------------------------------------------- |")
        file.write("\n")

        print("| Invoice No:\t\t"+str(get_datetime_integer())+"\t\t\t\t\t\t|")
        print("| Invoice Date:\t\t" + str(todaysDate) + "\t\t\t\t\t\t|")
        print("| Invoice Type:\t\tSale                                                    |")
        print("| Buyer Name:\t\t"+str(name[0]))
        print("| Buyer Address:\t"+str(name[1]))
        print("| Buyer Contact No:\t"+str(name[2]))
        print("| ----------------------------------------------------------------------------- |")
        
    elif typeOfTransaction == "order":
        file.write("| Invoice No:\t\t\t"+str(get_datetime_integer())+"\t\t\t\t\t\t  |")
        file.write("\n")
        file.write("| Invoice Date:\t\t\t" + str(todaysDate) + "\t\t\t\t\t\t\t  |")
        file.write("\n")
        file.write("| Invoice Type:\t\t\tOrder\t\t\t\t\t\t\t\t  |")
        file.write("\n")
        file.write("| Shipping Company Name:\t"+str(name[0]))
        file.write("\n")
        file.write("| Shipping Company Address:\t"+str(name[1]))
        file.write("\n")
        file.write("| Shipping Company Contact No:"+str(name[2]))
        file.write("\n")
        file.write("| ----------------------------------------------------------------------------- |")
        file.write("\n")

        print("| Invoice No:\t\t\t"+str(get_datetime_integer())+"\t\t\t\t\t|")
        print("| Invoice Date:\t\t\t" + str(todaysDate) + "\t\t\t\t\t|")
        print("| Invoice Type:\t\t\tOrder\t\t\t\t\t\t|")
        print("| Shipping Company Name:\t"+str(name[0]))
        print("| Shipping Company Address:\t"+str(name[1]))
        print("| Shipping Company Contact No:\t"+str(name[2]))
        print("| ----------------------------------------------------------------------------- |")
                           
    file.write("| S.N\tBikeName\tCompany\tColor\tQty.\tUnit Price\tAmount\t\t\t  |")
    file.write("\n")
    file.write("| ----------------------------------------------------------------------------- |")
    file.write("\n")
    
    print("| S.N\tBikeName\tCompany\tColor\tQty.\tUnit Price\tAmount\t\t|")
    print("| ----------------------------------------------------------------------------- |")
    
    for key in bike_dict:
        total_price += bike_dict[key][5]
        
    for key in bike_dict:
        file.write("| "+str(i)+"\t"+str(bike_dict[key][0])+"\t\t"+str(bike_dict[key][1])+"\t\t"+str(bike_dict[key][2])+ "\t"+str(bike_dict[key][3]) +"\t"+ str(bike_dict[key][4])+"\t"+ str(bike_dict[key][5])+"\t\t\t  |")
        file.write("\n")
        file.write("|                                                                               |")
        file.write("\n")

        print("| "+str(i)+"\t"+str(bike_dict[key][0])+"\t\t"+str(bike_dict[key][1])+"\t"+str(bike_dict[key][2])+ "\t"+str(bike_dict[key][3]) +"\t"+ str(bike_dict[key][4])+"\t\t"+ str(bike_dict[key][5])+"\t\t|")
        print("|                                                                               |")

        i+=1

    file.write("| ----------------------------------------------------------------------------- |")
    file.write("\n")
    file.write("|                                             Total NPR Amount:\t\t" + str(total_price)+"  |")
    file.write("\n")
    file.write("| ----------------------------------------------------------------------------- |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("| (E. & O. E) Goods once sold are not exchangeable or returnable                |")
    file.write("\n")
    file.write("|                                                                               |")
    file.write("\n")
    file.write("|                                              Printed On :" + str(printed_date)+"  |")
    file.write("\n")
    file.write("| ----------------------------------------------------------------------------- |")
    file.write("\n")
    
    print("| ----------------------------------------------------------------------------- |")
    print("|                                             Total NPR Amount:\t\t" + str(total_price)+"\t|")
    print("| ----------------------------------------------------------------------------- |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("|                                                                               |")
    print("| (E. & O. E) Goods once sold are not exchangeable or returnable                |")
    print("|                                                                               |")
    print("|                                               Printed On :" + str(printed_date)+" |")
    print("| ----------------------------------------------------------------------------- |")
    file.close()

def sell_bike():
    print()
    display_message("Lets sell bikes.")
    
    total_price = 0
    anotherSale = True
    
    each_qty_sold_dict = {}
    each_amount_sold_dict = {}
    bike_sold_dict = {}
    customer = []
    
    bikes= return_2d_list()

    customer_name = try_empty_string("Enter customer name: ")
    customer_address = try_empty_string("Enter customer address: ")
    customer_contact =try_invalid_int("Enter customer contact No. : ")

    customer = [customer_name,customer_address,customer_contact]

    print()
    display_message("These Bikes are available:")
    print(get_bike())
    
    while anotherSale:
        bikeId = validate_bike_Id()
        quantity = validate_quantity(bikeId)
        
        sell_quantity(bikeId, quantity)

        #if there is bikeId in dict then append the quantity of the same
        if bikeId in each_qty_sold_dict:
            each_qty_sold_dict[bikeId] += quantity

        #if there is no key as bikeId in dict then add quantity for that bikeid
        if bikeId not in each_qty_sold_dict:
            each_qty_sold_dict[bikeId] = quantity
        
        price = int(bikes[bikeId-1][4])
   
        while True:
            display_message("Sell another bike?")
            continueSale = input("Do you want to continue selling bikes(Y/N)? ").upper()
            if continueSale == "Y":
                anotherSale = True
                break
            elif continueSale == "N":
                anotherSale = False
                
                #calculating the amount for each type of bike selected using total_qty_dict as dictionary
                for key in each_qty_sold_dict:
                    price = int(bikes[key-1][4])
                    each_amount_sold_dict[key] = price * each_qty_sold_dict[key]
                    bike_sold_dict[key] = [bikes[key-1][0],bikes[key-1][1],bikes[key-1][2],each_qty_sold_dict[key],bikes[key-1][4],each_amount_sold_dict[key]]
                    
                today_date = datetime.datetime.now().strftime("%d/%m/%Y")
                
                generate_bill("sale", customer, today_date, bike_sold_dict)
                break
            
            else:
                display_message("Invalid Entry!")
                continue
    print()

def order_bike():
    total_price = 0
    total_amount = 0
    newbike_id = 1
    anotherOrder = True
    newOrder = False

    each_qty_order_dict = {}
    each_amount_order_dict = {}
    bike_order_dict = {}
    shipping = []
    new_order_list = []
    new_order_dict = {}
    
    display_message("Lets order bikes. ")

    bikes= return_2d_list()

    shipping_name = try_empty_string("Enter Shipping Company name: ")
    shipping_address = try_empty_string("Enter Shipping Company address: ")
    shipping_contact = try_invalid_int("Enter Shipping Company contact No. : ")

    shipping = [shipping_name, shipping_address, shipping_contact]

    print()
    display_message("These Bikes are available:")
    print(get_bike())

    while True:
        print()
        display_message("Order New bike?")
        #print("Order New bike?")
        continueNewOrder = input("Do you want to add new bikes(Y/N)? ").upper()
        if continueNewOrder == "Y":
            newOrder = True
            break
        elif continueNewOrder == "N":
            newOrder = False
            break
        else:
            print("Invalid Entry!")
            continue

    while newOrder:

        bike_name = try_empty_string("Enter Bike Name: ")
        company_name = try_empty_string("Enter Bike Company: ")
        color = try_empty_string("Enter the color of the bike: ")

        bikes= return_2d_list()
        
        for i in range(len(bikes)):
            while bike_name.upper() == bikes[i][0].upper() and color.upper() == bikes[i][2].upper() and company_name.upper() == bikes[i][1].upper():
                print()
                print(f" The {bike_name} Bike of {company_name} company having {color} color already exist. ")
                display_message("Add another bike?")
                bike_name = try_empty_string("Enter Bike Name: ")
                company_name = try_empty_string("Enter Bike Company: ")
                color = try_empty_string("Enter the color of the bike: ")
            
        quantity = try_invalid_int("Enter the quantity of the bike: ")
        bike_price = try_invalid_int("Enter the price of the bike: ")

        new_order_dict[newbike_id] = [bike_name,company_name,color,quantity,bike_price]
        
        anotherOrder = False
        newbike_id += 1
        
        while True:
            display_message("Add another bike?")
            continueAdd = input("Do you want to continue adding bikes(Y/N)? ").upper()
            if continueAdd == "Y":
                newOrder = True
                break
            elif continueAdd == "N":
                newOrder = False

                #calculating the amount for each type of bike selected using total_qty_dict as dictionary
                for key in new_order_dict:
                    total_amount = new_order_dict[key][3] * new_order_dict[key][4]
                    new_order_dict[key].extend([total_amount])

                new_order(new_order_dict)
                
                today_date = datetime.datetime.now().strftime("%d/%m/%Y")
                generate_bill("order", shipping, today_date, new_order_dict)
                break
            else:
                display_message("Invalid Entry!")
                continue
    
    while anotherOrder:
        print()
        display_message("Order bike")
        
        bikeId = validate_bike_Id()
        quantity = try_invalid_int("Enter a value for quantity: ")
        
        order_quantity(bikeId, quantity);

        #if there is bikeId in dict then append the quantity of the same
        if bikeId in each_qty_order_dict:
            each_qty_order_dict[bikeId] += quantity

        #if there is no key as bikeId in dict then add quantity for that bikeid
        if bikeId not in each_qty_order_dict:
            each_qty_order_dict[bikeId] = quantity

        while True:
            display_message("Order another bike?")
            continueOrder = input("Do you want to continue ordering bikes(Y/N)? ").upper()
            if continueOrder == "Y":
                anotherOrder = True
                break
            elif continueOrder == "N":
                anotherOrder = False

                #calculating the amount for each type of bike selected using total_qty_dict as dictionary
                for key in each_qty_order_dict:
                    price = int(bikes[key-1][4])
                    each_amount_order_dict[key] = price * each_qty_order_dict[key]
                    bike_order_dict[key] = [bikes[key-1][0],bikes[key-1][1],bikes[key-1][2],each_qty_order_dict[key],bikes[key-1][4],each_amount_order_dict[key]]
                
                today_date = datetime.datetime.now().strftime("%d/%m/%Y")
                generate_bill("order", shipping, today_date, bike_order_dict)
                break
            
            else:
                display_message("Invalid Entry!")
                continue
            
    print()








