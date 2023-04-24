import mysql.connector as connector
import datetime
from datetime import date
import random
import traceback
con = connector.connect(host='localhost', user='root', passwd='artha121', database='flipMart')
if con.is_connected():
    print("Success")
else:
    print("Failure")

mycursor = con.cursor(buffered=True)

def adminOrCustomer():
    print("Enter 1 for Admin and 2 for Customer:")
    n = int(input())
    return n

def adminMenu():
    print("Enter 1 to view all the available products.")
    print("Enter 2 to add a product to the catalog.")
    print("Enter 3 to alter the quantity of a product in the catalog.")
    print("Enter 4 to change password.")
    print("Enter 5 to reward coupons.")
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
    if len(listprods)==0:
        print("Your cart is empty.")
        return 0
    print("Product_ID\tProduct_Name\tPrice\tQuantity")
    for i in listprods:
        mycursor.execute(f"Select * from product where product_id = {i[1]}")
        prod = mycursor.fetchall()[0]
        prod_name = prod[1]
        price = prod[2]
        print(f"{i[1]}\t{prod_name}\t{price}\t{i[2]}")
    return 0

def addToCart(customer_id,pincode):
    product_id = int(input("Enter product id: "))
    mycursor.execute(f"Select * from cart where user_id = {customer_id} and product_id = {product_id}")
    AlreadyPresent = mycursor.fetchall()
    if len(AlreadyPresent)!= 0:
        print("This item is already in your cart.")
        print("Returning to main menu where you can choose to change its quantity.")
        return
    mycursor.execute(f"Select * from available where pincode = {pincode} and product_id = {product_id}")
    listprods = mycursor.fetchall()
    if len(listprods) == 0:
        print("No such product is available at your branch.")
        ch = int(input("Enter 1 to add another product or 0 to go to main menu: "))
        if ch==0:
            return
        return addToCart(customer_id, pincode)
    else:
        print("Product_ID\tProduct_Name\tPrice\tQuantity_Available")
        mycursor.execute(f"Select * from product where product_id = {product_id}")
        listprod = mycursor.fetchone()
        mycursor.fetchall()
        print(f"{listprod[0]}\t{listprod[1]}\t{listprod[2]}\t{listprods[0][2]}")
        quantity = int(input("Enter quantity: "))
        if quantity>listprods[0][2]:
            print("This item is not available in this quantity.")
            ch = int(input("Enter 1 to try adding again or 0 to go to main menu: "))
            if ch==0:
                return
            return addToCart(customer_id, pincode)
        else:
            print(f"Adding {listprod[1]} to cart")
            mycursor.execute(f"insert into cart (select {customer_id}, {product_id},{quantity} from available where available.pincode = {pincode} and available.product_id ={product_id} and available.quantity>={quantity});")
    return 0

def delFromCart(customer_id,pincode):
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
        if new_quant < 1 or quant < 1:
            #delete from cart
            mycursor.execute(f"delete from cart where product_id = {prod_id} and user_id = {customer_id}")
        else:
            #change quantity
            mycursor.execute(f"Select * from available where pincode = {pincode} and product_id = {prod_id}")
            listprods = mycursor.fetchall()
            if new_quant>listprods[0][2]:
                print("This item is not available in this quantity.")
                ch = int(input("Enter 1 to try changing again or 0 to go to main menu: "))
                if ch==0:
                    return
                return delFromCart(customer_id,pincode)
            else:
                mycursor.execute(f"update cart set quantity = {new_quant} where product_id = {prod_id} and user_id = {customer_id}")
    print("Your updated cart: ")
    viewCart(customer_id)


def checkAvailableQuant(new_quantity, pincode, prod_id):
    mycursor.execute(f"Select * from available where pincode = {pincode} and product_id = {prod_id}")
    availQuants = mycursor.fetchall()
    for i in availQuants:
        availQuant = i[2]
    if new_quantity >= availQuant:
        return True
    return False

def findCartPrice(customer_id):
    totprice = 0
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
        prod_price = mycursor.fetchall()[0][2] * i[2]
        totprice += prod_price
    return totprice

def placeOrder(customer_id, pincode):
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
        while (checkAvailableQuant(new_quant, pincode, prod_id)):
            new_quant = int(input(f"{new_quant} products are not available at your branch. Please enter new quantity: "))
        if new_quant < 1 or quant < 1:
            #delete from cart
            mycursor.execute(f"delete from cart where product_id = {prod_id} and user_id = {customer_id}")
        else:
            #change quantity
            mycursor.execute(f"update cart set quantity = {new_quant} where product_id = {prod_id} and user_id = {customer_id}")
    #order is finalized
    #follow these steps to place the order:
    mycursor.execute(f"select order_id  from orders")
    o_id =mycursor.fetchall()
    order_id = 0
    for i in range(len(o_id)):
        if(int(o_id[i][0])>order_id):
            order_id = int(o_id[i][0])
    order_id +=1
    mycursor.execute("SET autocommit = 0;")
    mycursor.execute("start transaction;")
    try:
        # alter table products_in_order
        # alter table product
        mycursor.execute(f"select {order_id}, '{date.today()}', (select if(sum(quantity*price) is not null,sum(quantity*price),0) from cart,product where cart.user_id={customer_id} and cart.product_id = product.product_id),'{date.today()+ datetime.timedelta(days=4)}',{pincode},{customer_id} where not exists(select cart.product_id as prod from available,cart where available.pincode = {pincode} and cart.user_id = {customer_id} and available.product_id = cart.product_id and available.quantity is not null and available.quantity < cart.quantity) and not exists(select cart.product_id  from cart  where cart.user_id = {customer_id} and cart.product_id not in (select product_id  from available where pincode = {pincode}));")
        entry = mycursor.fetchall()[0]
        e_2 = int(entry[2])
        entry = list(entry)
        entry[2] = e_2
        entry = tuple(entry)
        print(entry[2])
        mycursor.execute(f"insert into orders values({entry[0]},'{date.today()}',{entry[2]},'{date.today()+ datetime.timedelta(days=4)}',{entry[4]},{entry[5]})")
        mycursor.execute("delete from available where quantity = 0;")
        mycursor.execute(f"update customer set total_no_of_orders = total_no_of_orders +1 where customer.user_id = {customer_id};")
        #coupon table will be updated if the customer is eligible to use one
        cartPrice = findCartPrice(customer_id)
        print("Contents of your order: ")
        viewCart(customer_id)
        currdate = datetime.date.today()
        mycursor.execute(f"Select * from coupon where user_ID = {customer_id} and min_order_amt < {cartPrice} and order_id is null and order_date is null and valid_until_date > {currdate}")
        listcoupons = mycursor.fetchall()
        if len(listcoupons) < 1:
            print("No coupons applicable for this order.")
            print(f"Order Total: {cartPrice}")
        else:
            #apply max coupon and print that it has been applied and before and after of orderTotal
            disc = 0
            for j in listcoupons:
                if j[3]>disc:
                    disc = j[3]
            newPrice = (((100-disc)/100)*cartPrice)
            print(f"A coupon of {disc}% has been applied to your order.")
            print(f"Order Total before coupon: {cartPrice}")
            print(f"Order Total after coupon application: {newPrice}")
            mycursor.execute(f"update orders set total_price = {newPrice} where order_id = {order_id}")
            mycursor.execute(f"update coupon set order_date = '{date.today()}',order_id = {order_id} where user_id = {customer_id} and discount_offered = {disc} limit 1;")
        ch = int(input("Enter 0 to go back to menu or any other number to proceed to checkout: "))
        if ch == 0:
            mycursor.execute("rollback;")
            return 0

        # alter table cart
        # alter table available
        mycursor.execute(f"delete from cart where cart.user_id = {customer_id};")
        # alter table coupon
        
        ch = int(input("Enter payment method: 1.UPI\n2.Card\n3.Cash\n"))
        print("Order placed successfully. It will be delivered in 2-3 days. Happy shoppping!")
        mycursor.execute(f"select * from customer where user_id = {customer_id}")
        mycursor.execute("commit;")   
        
    except Exception  as e:
        mycursor.execute("rollback;")
        print("Error while placing order")
        print(e)
        traceback.print_exc()
        return 0
    mycursor.execute(f"select * from orders where order_id = {order_id};")
    listprods = mycursor.fetchall()
    for i in listprods:
        print(i)
    ch = int(input("Enter -1 to exit or any other number to continue shopping: "))
    mycursor.execute("SET autocommit = 1;")

def addProduct(pincode):
    prod_id = int(input("Enter Product ID: "))
    mycursor.execute(f"Select * from Product where product_id = {prod_id}")
    listprods = mycursor.fetchall()
    if len(listprods) != 0:
        listprods = listprods[0]
        print("A product with this Product ID already exists: ")
        print("Product ID\tProduct_Name\tPrice")
        print(f"{listprods[0]}\t{listprods[1]}\t{listprods[2]}")
        ch = int(input("Enter 1 to enter another Product ID or 0 to exit: "))
        if ch == 1:
            return addProduct(pincode)
        else:
            return 0
    prod_name = input("Enter Product Name: ")
    prod_price = int(input("Enter Product Price: "))
    quant = int(input("Enter quantity available: "))
    mycursor.execute(f"Insert into product VALUES ({prod_id},'{prod_name}',{prod_price})")
    mycursor.execute(f"Insert into available VALUES ({pincode},{prod_id},{quant})")
    return 0

def rewardCoupon(customer_id):
    print("Enter 1 to reward by number of orders")
    print("Enter 2 to reward randomly")
    n = int(input("Enter choice:"))
    mycursor.execute(f"select max(coupon_id) from coupon")
    coupon_id =mycursor.fetchall()[0]
    coupon_id = coupon_id[0]
    print(coupon_id+1)
    if(n==1):
        try:
            mycursor.execute("start transaction;")
            mycursor.execute(f"select user_id,count(*) as c1 from orders group by user_id having c1>= all(select count(*) as c1 from orders group by user_id);")
            user_id = mycursor.fetchall()[0]
            u = user_id[0]
            mycursor.execute(f"insert into coupon values({coupon_id+1},1000,'{date.today()+datetime.timedelta(days=10)}',{random.randint(1,30)},'{date.today()}',null,null,{u});")
            mycursor.execute("commit;")
        except:
            mycursor.execute("rollback;")
        print("Updated list of coupons")
        mycursor.execute(f"Select * from coupon")
        listcoupons = mycursor.fetchall()
        if len(listcoupons) < 1:
            print("No available coupons")
            return
        # print("Coupon_ID\tMin_Order_Amount\tDiscount_Offered\tValid_Until_Date\tIssue_Date")
        for i in listcoupons:
            print(i)
        
    else:
        mycursor.execute(f"select max(user_id) from customer")
        user_id =mycursor.fetchall()[0]
        u = int(user_id[0])
        u = random.randint(1,u)
        mycursor.execute(f"insert into coupon values({coupon_id+1},1000,'{date.today()+datetime.timedelta(days=10)}',{random.randint(1,30)},'{date.today()}',null,null,{u});")
        print("Updated list of coupons")
        mycursor.execute(f"Select * from coupon")
        listcoupons = mycursor.fetchall()
        if len(listcoupons) < 1:
            print("No available coupons")
            return
        for i in listcoupons:
            print(i)
        
        
def viewCoupons(customer_id):
    mycursor.execute(f"Select * from coupon where user_id = {customer_id} and coupon_id is not null and order_id is null and order_date is null")
    listcoupons = mycursor.fetchall()
    if len(listcoupons) < 1:
        print("No available coupons")
        return
    print("Coupon_ID\tMin_Order_Amount\tDiscount_Offered\tValid_Until_Date\tIssue_Date")
    for i in listcoupons:
        print(f"{i[0]}\t{i[1]}\t{i[3]}\t{i[2]}\t{i[4]}\t{i[5]}\t{i[6]}")

def changeQuant(branch_pincode):
    prod_id = int(input("Enter Product ID: "))

    mycursor.execute(f"Select * from available where product_id = {prod_id} and pincode = {branch_pincode}")
    listprods = mycursor.fetchall()
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
    print("Entering as Admin... ")
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
    branch_name = mycursor.fetchall()[0]
    print(f"You have access to the records of Area: {branch_name}")
    while True:
        admin_ch = adminMenu()
        if admin_ch == 0:
            ret = int(input("Enter 0 to login again or -1 to exit the program: "))
            return ret
        elif admin_ch == 1:
            admin_ch = viewAvailableProducts(branch_pincode)
        elif admin_ch == 2:
            admin_ch = addProduct(branch_pincode)
        elif admin_ch == 3:
            admin_ch = changeQuant(branch_pincode)
        elif admin_ch == 4:
            admin_ch = changePassword(customer_id)
        elif admin_ch==5:
            admin_ch = rewardCoupon(customer_id)
        elif admin_ch == 10:
            admin_ch = olap()

def customerMenu():
    print("Enter 1 to view all the available products.")
    print("Enter 2 to view your cart.")
    print("Enter 3 to add product to your cart.")
    print("Enter 4 to remove or change the quantity of a product present in your cart.")
    print("Enter 5 to place an order.")
    print("Enter 6 to view all available coupons.")
    print("Enter 0 to exit.")
    ch = int(input("Enter choice: "))
    return ch

def insideCustomer():
    #put an infinite loop on customer_menu
    #only delete product from warehouse when the order has been placed
    #update addToCart function so that it returns a message if the quantity asked for was less than the quantity available and update cart accordingly
    print("Entering as Customer... ")
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
        customer = mycursor.fetchall()[0]
    customer_id = customer[0]
    branch_pincode = customer[4]
    mycursor.execute(f"Select Area from Branch where Pincode = {branch_pincode}")
    # branch_name = mycursor.fetchall()[0]
    while True:
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
            cus_ch = delFromCart(customer_id,branch_pincode) 
        elif cus_ch == 5:
            cus_ch = placeOrder(customer_id,branch_pincode)
            if cus_ch == -1:
                return -1
        elif cus_ch == 6:
            cus_ch = viewCoupons(customer_id)

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
