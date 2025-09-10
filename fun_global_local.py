#local variable
def localvar():
  x=10
  print(x)  #10



localvar()
#print(x)   #NameError: name 'x' is not defined

'''
#by this we can handle exception
try:
  print(x) 
except Exception as e:
    print(e)
'''


#global variable


var=10   #global variable
def globalVar():
    global var    # needed because we want to change the global variable
    var=10+10
    #add=var+5
    print(var)

    
def acc():
    print(var) #now var value is change bcoz we change it in globalvar 

    
globalVar()
print(var)

acc()


    
