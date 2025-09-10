#Tuple
tup1=(1,2,3,4,5,1,6)
#index
#check where the 6 element present in tuple in which index
print(tup1.index(6))   #5
#count
#it count how mant time num occure in tup1
print(tup1.count(1))   #2




#concatinate 2 tuples

t1=(1,2,3,4,5)
t2=("Radha","Krishn","Ram","Siya")
t3=t1+t2
print(t3) #(1, 2, 3, 4, 5, 'Radha', 'Krishn', 'Ram', 'Siya')

t4=tuple(["hii","hello"])
print(type(t4)) #<class 'tuple'>
print(t4)  #('hii', 'hello')


#empty tuple using tuple constructor
tup2=tuple(())
print(tup2)


#tuple slicing
tupl1=(1,2,3,4,5,6,7)
print(tupl1[1:4])
#reverse 
print(tupl1[::-1])



#print tuple element with help of for loop
for ele in tupl1:
    print(ele)

#convert tuple to list
t1=("Ram",3,"Prem")
t2=list(t1)
print(type(t2))
print(t2)



#nested Tuple
tup1=(1,2,("sham","Ram"),7,9)
print(tup1[2][1])   #Ram
