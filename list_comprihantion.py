#code1
lst=[1,2,3,4,5]
new_lst=[]
for i in lst:
    x=i*2
    new_lst.append(x)
    
print(new_lst) #[2, 4, 6, 8, 10]


#with help of list comprihension
number=[1,2,3,4]
numlist=[num*2 for num in number]
print(numlist) #[2, 4, 6, 8]


#code2
#sqr of all even num for 1 to 10
even_list=[]
for i in range(1,11):
    if i%2==0:
        sqr=i*i
        even_list.append(sqr)
print(even_list)  #[4, 16, 36, 64, 100]


#with help of list comprihension
even_list1=[]
new_even=[i**2 for i in range(1,10) if i%2==0  ]
print(new_even)


#code3
lst1=[]
for i in range(1,11):
    if(i%2==0):
        lst1.append("even")
    else:
        lst1.append("odd")
print(lst1) #['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

#with help of list comprihension

lst2=["even" if i%2==0 else "odd" for i in range(1,11)]
print(lst2)
#['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']



#code4
matrix=[["apple","banana","cherry"],
        ["date","fig","grape"],
        ["kiwi","lemon","orange"]]
new_m=[]
for row in matrix:
    for  fruit in row:
        new_m.append(fruit.capitalize())

print(new_m)#['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grape', 'Kiwi', 'Lemon', 'Orange']

#with help of list comprihension
       
matrix1=[["apple","banana","cherry"],
        ["date","fig","grape"],
        ["kiwi","lemon","orange"]]
new_m1=[[fruit.capitalize() for fruit in row]for row in matrix1]
print(new_m1)
#[['Apple', 'Banana', 'Cherry'], ['Date', 'Fig', 'Grape'], ['Kiwi', 'Lemon', 'Orange']]

