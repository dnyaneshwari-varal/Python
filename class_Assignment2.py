class Product:
    product_name=None
    price=None
    discount_rate=0.1  #(10% discount)

    def __init__(self,prod_name,p):
        self.product_name=prod_name
        self.price=p
        
        

    def final_price(self):
        print("Product name is: ",self.product_name)
        print("Original Price: ",self.price)
        f_p=self.price-self.discount_rate
        return f_p
    

    @staticmethod
    def cal_shipping(weight):
        if weight <5 :
            print("Shipping cost is Rs=50!")
            #print("TO pay: ",self.f_p+50)
            value=50
        elif weight >=5:
            print("Shipping cost is Rs=100!")
            #print("TO pay: ",self.f_p+100)
            value=100
        return value
            

#Product.discount_rate=float(input("Change discount: "))    



while True:
    print("1.Add a new product")
    print("2.Display all product with discount and shipping")
    print("3.Change discount rate")
    print("4.exit")
    choice=int(input("choice: "))

    if choice==1:
         
         #weigth=float(input("Enter weight of product: "))
         prod1_name=input("Enter product name: ")
         prod1_price=int(input("Enter product price: "))
         #ch=int(input("if want to add press 1 else press 0: "))
         
        
   
    elif choice==2:
        obj1=Product(prod1_name,prod1_price)
        final_price=obj1.final_price()
        print("Final price after applying discount is: ",final_price)
        print("------***------")
        weight=int(input("Enter weight of product: "))
        shipping_amt=Product.cal_shipping(weight)
        print("Toatl amount to pay: ",final_price+shipping_amt)


        

    elif choice==3:
        print("exit")


    elif choice==4:
        break
        
    
