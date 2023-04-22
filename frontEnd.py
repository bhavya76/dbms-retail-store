import mysql.connector as connector
import datetime

con = connector.connect(host='localhost', user='root', passwd='artha121', database='flipMart')
if con.is_connected():
    print("Success")
else:
    print("Failure")

mycursor = con.cursor()

def adminOrCustomer():
    print("Enter 1 for Admin and 2 for Customer:")
    n = int(input())
    return n

def adminMenu():
    print("Enter 1 to view all the available products.")
    print("Enter 2 to add a product to the catalog.")
    print("Enter 3 to alter the quantity of a product in the catalog.")
    print("Enter 4 to change password.")
    print("Enter 5 to view the number of deleted admins.")
    print("Enter 10 to view buying trends and statistics.")
    print("Enter 0 to exit.")
    ch = int(input("Enter choice: "))
    return ch

def viewAvailableProducts(pincode):
    mycursor.execute(f"select product.product_name, product.price, available.quantity from product,available where product.product_id = available.product_id and available.pincode = {pincode};")
    listprods = mycursor.fetchall()
    print("Product_Name\tPrice\tQuantity")
    for i in listprods:
        print(f"{i[0]}\t{i[1]}\t{i[2]}")
    return 0

def viewCart(customer_id):
    mycursor.execute(f"Select * from Cart where user_id = {customer_id}")
    listprods = mycursor.fetchall()
    print("Product_ID\tProduct_Name\tPrice\tQuantity")
    for i in listprods:
        mycursor.execute(f"Select * from product where product_id = {i[1]}")
        prod = mycursor.fetchall()[0]
        prod_name = prod[1]
        price = prod[2]
        print(f"{i[1]}\t{prod_name}\t{price}\t{i[2]}")
    return 0

def addToCart(customer_id,pincode):
    product_id = int(input("Enter product id:"))
    quantity = int(input("Enter quantity"))
    mycursor.execute(f"insert into cart (select {customer_id}, {product_id},{quantity} from available where available.pincode = {pincode} and available.product_id ={product_id} and available.quantity>{quantity});")
    return 0

def delFromCart(customer_id):
    mycursor.execute(f"Select * from Cart where user_id = {customer_id}")
    listprods = mycursor.fetchall()
    n = len(listprods)
    if n==0:
        print("Your cart is empty.")
        return
    for i in listprods:
        prod_id = i[1]
        quant = i[2]
        mycursor.execute(f"Select * from product where product_id = {prod_id}")
        prod = mycursor.fetchall()[0]
        prod_name = prod[1]
        price = prod[2]
        print("Product_ID\tProduct_Name\tPrice\tQuantity")
        print(f"{prod_id}\t{prod_name}\t{price}\t{quant}")
        new_quant = int(input("Enter new quantity: "))
        if new_quant < 1:
            #delete from cart
            mycursor.execute(f"delete from cart where product_id = {prod_id} and user_id = {customer_id}")
        else:
            #change quantity
            mycursor.execute(f"update cart set quantity = {new_quant} where product_id = {prod_id} and user_id = {customer_id}")
    print("Your updated cart: ")
    viewCart(customer_id)

def placeOrder(customer_id):
    print("Please choose if you would like to remove any items from your cart before placing your order: ")
    mycursor.execute(f"Select * from Cart where user_id = {customer_id}")
    listprods = mycursor.fetchall()
    n = len(listprods)
    if n==0:
        print("Your cart is empty.")
        return
    for i in listprods:
        prod_id = i[1]
        quant = i[2]
        mycursor.execute(f"Select * from product where product_id = {prod_id}")
        prod = mycursor.fetchall()[0]
        prod_name = prod[1]
        price = prod[2]
        print("Product_ID\tProduct_Name\tPrice\tQuantity")
        print(f"{prod_id}\t{prod_name}\t{price}\t{quant}")
        new_quant = int(input("Enter new quantity: "))
        if new_quant < 1:
            #delete from cart
            mycursor.execute(f"delete from cart where product_id = {prod_id} and user_id = {customer_id}")
        else:
            #change quantity
            mycursor.execute(f"update cart set quantity = {new_quant} where product_id = {prod_id} and user_id = {customer_id}")
    #order is finalized
    #follow these steps to place the order:

    #coupon table will be updated if the customer is eligible to use one
    #view new available products --> quantity will have been reduced in 'available'
    #cart will be emptied for this customer
    #the contents of the order will be added to products_in_order
def addProduct(pincode):
    prod_id = int(input("Enter Product ID: "))
    mycursor.execute(f"Select * from Product where product_id = {prod_id}")
    listprods = mycursor.fetchone()
    if listprods != None:
        print("A product with this Product ID already exists: ")
        print("Product ID\tProduct_Name\tPrice")
        print(f"{listprods[0]}\t{listprods[1]}\t{listprods[2]}")
        ch = int(input("Enter 1 to enter another Product ID or 0 to exit: "))
        if ch == 1:
            addProduct(pincode)
        else:
            return 0
    prod_name = input("Enter Product Name: ")
    prod_price = int(input("Enter Product Price: "))
    quant = int(input("Enter quantity available: "))
    mycursor.execute(f"Insert into product VALUES ({prod_id},'{prod_name}',{prod_price})")
    mycursor.execute(f"Insert into available VALUES ({pincode},{prod_id},{quant})")
    return 0

def changeQuant(branch_pincode):
    prod_id = int(input("Enter Product ID: "))
    mycursor.execute(f"Select * from Product where product_id = {prod_id}")
    listprods = mycursor.fetchone()
    if len(listprods) == 0:
        print("No such product found")
        return 0
    prod_quant = int(input("Enter new quantity: "))
    if prod_quant == 0:
        mycursor.execute(f"Delete from available where pincode = {branch_pincode} and product_id = {prod_id}")
        mycursor.execute(f"Delete from product where product_id = {prod_id}")
    mycursor.execute(f"Update available set quantity = {prod_quant} where pincode = {branch_pincode} and product_id = {prod_id}")

def changePassword(customer_id):
    new = input("Enter new password:")
    mycursor.execute(f"update admin set Pass_word = '{new}' where user_id = {customer_id}")

def viewDelAdmins():
    mycursor.execute(f"select count(Username) from admin where user_id is null")

def olap():
    while (True):
        print("1. Viewing all orders on different order dates and delivery dates, and then all ordrs on a single order date")
        print("2. Viewing no of products in cart of different users with different product ids , and then all ordrs in the cart of a single user")
        print("3. Veiwing price or product grouping with only product id")
        print("4. Viewing coupons the store has offered upto a date to a given user, and then all the coupons offered upto that date")
        print("0. Exit from statistics")
        ch = int(input("Enter choice: "))
        if (ch == 1):
            mycursor.execute(f"select if(grouping(order_date)=1,'all order dates',order_date) as order_date,if(grouping(delivery_date)=1,'all delivery dates',delivery_date) as delivered_on,count(total_price) as no_of_orders from orders group by order_date,delivery_date with rollup union select if(grouping(order_date)=1,'all order dates',order_date) as order_date,if(grouping(delivery_date)=1,'all delivery dates',delivery_date) as delivered_on,count(total_price) as no_of_orders from orders group by delivery_date,order_date with rollup")
            listprods = mycursor.fetchall()
            print("Order_Date\tDelivery_Date\tNumber_Of_Orders")
            for i in listprods:
                print(f"{i[0]}\t{i[1]}\t{i[2]}")
        elif (ch==2):
            mycursor.execute(f"select if(grouping(user_ID)=1,'products in cart of all users',user_ID) as User_ID,if(grouping(product_ID)=1,'all products in the cart of user',product_ID) as Product_ID, sum(quantity) as no_of_products from cart group by user_ID,product_ID with rollup order by( grouping(user_id)+grouping(product_id)) desc")
            listprods = mycursor.fetchall()
            print("User_ID\tProduct_ID\tNo_Of_Products")
            for i in listprods:
                print(f"{i[0]}\t{i[1]}\t{i[2]}")
        elif (ch==3):
            mycursor.execute(f"select product_ID,product_name,sum(price) from product group by product_ID,product_name with rollup having grouping(product_name) = 1;")
            listprods = mycursor.fetchall()
            print("Product_ID\tProduct_ID\tTotal_Price")
            for i in listprods:
                print(f"{i[0]}\t{i[1]}\t{i[2]}")
        elif (ch==4):
            mycursor.execute(f"select valid_until_date,user_id, max(discount_offered) as max_discount,count(coupon_id) as total_no_of_coupons_given from coupon group by valid_until_date,user_id with rollup order by( grouping(user_id)+grouping(valid_until_date)) asc ")
            listprods = mycursor.fetchall()
            print("Valid_Until_Date\tUser_ID\tMax_Discount_Offered\tTotal_No_Of_Coupons_Given")
            for i in listprods:
                print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}")
        else:
            break
    
def insideAdmin():
    print("Entering as Admin: ")
    username = input("Enter Username: ")
    passw = input("Enter password: ")
    mycursor.execute(f"Select * from Admin where Username = '{username}' and Pass_word = '{passw}'")
    listadmins = mycursor.fetchall()
    if len(listadmins) == 0:
        print("No such user found")
        ch = int(input("Enter 0 to continue or -1 to exit: "))
        return ch
    admin = listadmins[0]
    customer_id = admin[0]
    branch_pincode = admin[3]
    mycursor.execute(f"Select Area from Branch where Pincode = {branch_pincode}")
    branch_name = mycursor.fetchone()
    print(f"You have access to the records of Area: {branch_name}")
    while True:
        admin_ch = adminMenu()
        if admin_ch == 0:
            ret = int(input("Enter 0 to login again or -1 to exit the program: "))
            return ret
        if admin_ch == 1:
            admin_ch = viewAvailableProducts(branch_pincode)
        if admin_ch == 2:
            admin_ch = addProduct(branch_pincode)
        if admin_ch == 3:
            admin_ch = changeQuant(branch_pincode)
        if admin_ch == 4:
            admin_ch = changePassword(customer_id)
        if admin_ch == 5:
            admin_ch = viewDelAdmins()
        if admin_ch == 10:
            admin_ch = olap()

def customerMenu():
    print("Enter 1 to view all the available products.")
    print("Enter 2 to view your cart.")
    print("Enter 3 to add product to your cart.")
    print("Enter 4 to remove a product from your cart.")
    print("Enter 5 to place an order.")
    print("Enter 0 to exit.")
    ch = int(input("Enter choice: "))
    return ch

def insideCustomer():
    #put an infinite loop on customer_menu
    #only delete product from warehouse when the order has been placed
    #update addToCart function so that it returns a message if the quantity asked for was less than the quantity available and update cart accordingly
    print("Entering as Admin: ")
    name = input("Enter your name: ")
    mycursor.execute(f"Select * from Customer where Name = '{name}'")
    listcus = mycursor.fetchall()
    
    if len(listcus)==0:
        print("No such customer found")
        ch = int(input("Enter 0 to continue or -1 to exit: "))
        return ch
    customer = listcus[0]
    if len(listcus) > 1:
        userid = int(input("Enter User ID: "))
        mycursor.execute(f"Select * from Customer where User_ID = {userid}")
        customer = mycursor.fetchone()
    customer_id = customer[0]
    branch_pincode = customer[4]
    mycursor.execute(
        f"Select Area from Branch where Pincode = {branch_pincode}")
    branch_name = mycursor.fetchone()
    cus_ch = customerMenu()
    if cus_ch == 0:
        ret = int(input("Enter 0 to login again or -1 to exit the program: "))
        return ret
    elif cus_ch == 1:
        cus_ch = viewAvailableProducts(branch_pincode)
    elif cus_ch == 2:
        cus_ch = viewCart(customer_id)
    elif cus_ch == 3:
        cus_ch = addToCart(customer_id,branch_pincode)   
    elif cus_ch == 4:
        cus_ch = delFromCart(customer_id) 
    elif cus_ch == 5:
        cus_ch = placeOrder(customer_id,branch_pincode)

print("Welcome User!")
print("Are you an admin or customer?")
while True:
    aorc = adminOrCustomer()
    if aorc == 0:
        print("Goodbye user!")
        break
    elif aorc == 1:
        ch = insideAdmin()
        if ch == -1:
            break
        elif ch == 0:
            continue
    elif aorc == 2:
        ch = insideCustomer()
        if ch == -1:
            break
        elif ch == 0:
            continue
