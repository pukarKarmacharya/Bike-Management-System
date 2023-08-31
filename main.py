#import all the function from function.py file
from function import *

def userInput():
    inputLoop=True
    display_message("Welcome to Bike Management System")
    while inputLoop:
        display_main_menu()
        uservalue = try_invalid_int("Enter the option: ")
        if uservalue == 1:
            sell_bike()
            
        elif uservalue == 2:
            order_bike()
            
        elif uservalue == 3:
            print()
            print(get_bike())
            print()
            
        elif uservalue == 4:
            print()
            display_message("Thank you for using Bike Management System")
            inputLoop = False
            
        else:
            print()
            display_message("INVALID INPUT\nPlease enter the options.")       

if __name__ == '__main__':
    userInput()
