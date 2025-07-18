from datetime import datetime
from write import generate_Sell_bills, generate_Buy_bills
Products = {}

def display_Products():
    try:
         with open("Products.txt","r") as file:
            lines = file.readlines()
            count = 1
            for line in lines:
                print(line.split())
                count +=1
                
            for key, values in Products.items():
                print(key +1 , end="\t")
                for i in range(len(values)):
                    if i == 3:
                        Selling_price = int(values[i]) * 2
                        print(Selling_price, end="\t")
                    elif i == 0 or i == 1 or i == 2 or i == 4 or i == 5:
                            print(values[i], end="\t")
                    else:
                            print("Invalid Syntax", end="\t")
    except :
                print("There is no existing products available")
print()

def Buy_Products():
    name_of_manufacturer = input("Enter the name of manufacturer: ")
    name_of_product = input("Enter the name of product:")
    Product_id = int(input("Enter the Product ID: "))
    quantity = int(input("Enter the quantity: "))
    Cost_price = int(input("Enter the price: "))
    Origin = input("Enter Origin of product:")
    date_time: datetime.now()
    if Product_id in Products :
       Products[Product_id]["quantity"]+=quantity
    else:
        
        Products[Product_id] = {
            "manufacturer": name_of_manufacturer,
            "product": name_of_product,
            "quantity": quantity,
            "Cost_price": Cost_price,
            "Origin": Origin,
            
        }

        print("Updated stock for " + str(Product_id)+ ": " + str(Products[Product_id]["quantity"]))
        generate_Buy_bills(name_of_manufacturer, name_of_product, Product_id, quantity, Cost_price, Origin)
def generate_Buy_bills(name_of_manufacturer,name_of_product, Product_id,quantity,Cost_price,Origin):
    Total_amount = Cost_price * quantity
    vat_13 = 0.13
    Total_with_vat = Total_amount *(1 + vat_13)
    try:    
      with open("Buy_bill.txt", "w") as file:
           
           file.write("Name of manufacturer:"+ str(name_of_manufacturer))
           file.write("-----------------------------------------------------")
           file.write("/n")
           file.write("Product id\t Product name\t Cost price\tquantity\t brand\t Total")
           file.write("\n")
           file.write("Product id :" + str(Product_id))
           file.write("\n")
           file.write("..................."*5)
           file.write("Product name :" + str(name_of_product))
           file.write("........................"*5)
           file.write("\n")
           file.write("Quantity:" + str(quantity))
           file.write(".................."*5)
           file.write("\n")
           file.write("Origin:" + str(Origin))
           file.write("................"*5)           
           file.write("Total VAT(13%):$" +str(Total_amount))
           file.write(".................."*5)
           file.write("\n")        
           file.write("\n")
           file.write("-------------------------------------------------------------------")
           file.write("\n")
           print("Buy bill generated")
                      
           print(".................Bills...............................")
           print("...............Transaction Type....................")
           print ("Name of manufacturer:"+ str(name_of_manufacturer))
           print("-----------------------------------------------------")
           print("Product id :" + str(Product_id))
           print("\n")
           print("............................."*5)
           print("Product name :"  + str(name_of_product))
           print(".........................."*5)
           print("\n")
           print("Quantity:" + str(quantity))
           print("\n")
           print("Origin:" + str(Origin))
           print("\n")    
           print("Total VAT(13%):$" +str(Total_with_vat))
           print("\n")        
           print("\n")
           print("-------------------------------------------------------------------")
           print("\n")
           print("\n")
    except Exception as e:
                     print("Error generating:",e)
def Sell_Products():
    customer_name = input("Enter the name of customer: ")
    name_of_product = input("Enter the name of product: ")
    Product_id = int(input("Enter the Product ID: "))
    quantity = int(input("Enter the quantity: "))
    brand = input("Enter the brand: ")

    today = datetime.now()

    if Product_id in Products:
        if "Cost_price" not in Products[Product_id]:
            print("Error: Cost price not found for Product ID " + str(Product_id))
            return
        
        Cost_price = Products[Product_id]["Cost_price"]
        
        if Products[Product_id]["quantity"] >= quantity:
            Products[Product_id]["quantity"] -= quantity
        else:
            print("Not enough stock to sell.")
            return
    else:
        print("Product not found in stock.")
        return

    free_items = quantity // 3
    total_quantity = quantity + free_items

    Selling_price = Cost_price * 2
    total = Selling_price * quantity

    with open("sell.txt", 'w') as bill:
        bill.write("Customer name: " + customer_name + '\n')
        bill.write("Date: " + today.strftime('%Y%m%d_%H%M%S') + '\n')
        bill.write("- " + name_of_product + " (" + brand + ") x " + str(total_quantity) + " + " + str(free_items) + " free - Rs. " + str(total) + '\n')
        Products[Product_id]["quantity"] -= total_quantity
        bill.write("\nTotal: Rs. " + str(total) + '\n')

    print("Updated stock for " + str(Product_id) + ": " + str(Products[Product_id]["quantity"]))
    generate_Sell_bills(customer_name, name_of_product, Product_id, quantity, brand, Selling_price)


def generate_Sell_bills(customer_name,name_of_product, Product_id,quantity,brand,Selling_price):
    vat_13 = 0.13
    Total = Selling_price * quantity
    Total_with_vat = Total *(1 + vat_13)
    free_items = quantity // 3
    try:
        with open("Sell_bill.txt", "w") as file:
           
           file.write("Customer_name:"+ str(customer_name))
           file.write("-----------------------------------------------------")
           file.write("/n")

           file.write("Product id\t Product name\t Selling_price\tquantity\t brand\ttt Total")
           file.write("\n")
           file.write("Product id :" + str(Product_id)+"\n")
           file.write(str(Product_id) + "\t" + str(name_of_product) + "\t" + str(Selling_price) +
                   "\t" + str(quantity) + "\t" + str(brand) + "\t" + str(Total_with_vat) + "\n")
           file.write("\n")
           file.write("--------------------------------------------")           
           file.write("Total VAT(13%):$" +str(Total_with_vat))
           file.write("Free Items: " + str(free_items) + " free\n")
           file.write("\n")        
           file.write("\n")
           file.write("-------------------------------------------------------------------")
           file.write("\n")
           file.write("\n")
           print("Sell bill generated")
           print("...............................Sells bill...............................")
           print("Customer Name:" + str(customer_name))
           print("-----------------------------------------------------")
           print("/n")
           print("Product id\t Product name\t Cost price\tquantity\t brand\ttt Total")
           print("..........................................................................")
           print("Name_of_Product:" + str(name_of_product))
           print("..........................................................................")
           print("\n")
           print("Product id :" + str(Product_id)+"\n")
           print("\n")
           print("................."*5)
           print("Quantity:" + str(quantity))
           print("..........................................................................")
           print("Brand:"  + str(brand))
           print("...........................................................................")
           print("\n")
           print("..........................................................................")
           print("Selling price:" +str( Selling_price))
           print("Free Items: " + str(free_items) + " free\n")
           print("..........................................................................")           
           print ("Total VAT(13%):$" +str(Total_with_vat))
           print("\n")        
           print("\n")
           print("-------------------------------------------------------------------")
           print("\n")
           print("\n")
    except Exception as e:
       print("Error invalid number",e)
