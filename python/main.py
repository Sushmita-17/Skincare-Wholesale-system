from Operation import display_Products,Buy_Products,Sell_Products
import read
from write import generate_Buy_bills,generate_Sell_bills

def main():
    while  True:
        print("\n Welcome to the product Wholesale system, Kathmandu")
        print("..................................."*5)
        print("1.Display all products")
        print("2.Sell products")
        print("3.Buy Products")
        print("4.Exit the system")
        user_choice = int(input("Enter your choice: "))
        try:
             if user_choice == 1:
                display_Products()
        
             elif user_choice == 2:
                 Sell_Products()
                 
                

             elif user_choice == 3:
               Buy_Products()
              
             elif user_choice == 4:
                print("Thank you for exiting")
                break
             
        
             else:
                  print("Invalid input")
        except ValueError:
               print("invalid input")
              
main()


