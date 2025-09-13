
try:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))

    result=num1%num2

except Exception as e:
    print(e)
    try:
        num3=int(input("Enter num3: "))
        num4=int(input("Enter num4: "))
    
    except Exception as e:
        print(e)
        
print(10)



#correct way of nested try

#ZeroDevisionError
try:
    num1=int(input("Enter num1: "))
    num2=int(input("Enter num2: "))

    result=num1%num2
    #value Error
    try:
        num1=int(input("Enter num1: "))
        num2=int(input("Enter num2: "))
        

    except Exception as e:
        print(e)

except Exception as e:
        print(e)        
        
print(10)
