Products= {}
def read():
    print("ID\tproduct_name\tBrand\tQuantity\tSelling_Price\tOrigin")
    print("..................................."*5)
    file = open("Products.txt", "r")
    product = file.readlines()
    file.close()


    list_products =[]
    for line in product :
        line = line.replace("\n", "")
        list_products.append(line)


    count_lines = len(list_products)

    Products.clear()
    for i  in range(count_lines ):
        product_data= list_products[i].split(',')
        Products[i+1] = product_data

