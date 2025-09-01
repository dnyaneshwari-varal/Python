d1={1:12,2:13}
for i in d1:
    print(i) #it will print keys


    
d1={1:12,2:13,3:"Ram"}
for i in d1:
    print(i,d1[i])


    
#print onnly values
for keys in d1.keys():
    print(d1[keys],end="\t")
print()

for value in d1.values():
    print(value,end="\t")
print()

#code1
d1={}
print(d1,type(d1))#{} <class 'dict'>

#code2
d2=dict()
print(d2,type(d2)) #{} <class 'dict'>


#code3
nums={1:"One",2:"Two",3:"Three",4:"Four",3:"five"}

print(nums) #{1: 'One', 2: 'Two', 3: 'five', 4: 'Four'}
print(nums[3]) #five
print(nums,type(nums))


#code4
cities={"India":"Delhi","Italy":"Rome","England":"London"}
print(cities)
print(cities,type(cities))

#code5
fruits=dict({1:"Apple",2:"Mangoes"})
print(fruits)#{1: 'Apple', 2: 'Mangoes'}





#add element in dictionary
d1={1:12,2:13}
print(d1) #{1: 12, 2: 13}
d1["add"]="Done" #add this to d1 dictionary
print(d1)  #{1: 12, 2: 13, 'update': 'Done'}


#update
d1[1]="Hii"
print(d1) #{1: 'Hii', 2: 13, 'add': 'Done'}


#pop(key)
d2={1:"Hii","age":25,3:"Good"}
print(d2)
d2=d2.pop("age")
print(age)
print(d2)


#remove last inserted item
d2={1:"Hii","age":25,3:"Good"}
last_item=d2.popitem()
print(last_item)
print(d2)

#Delete
d2={1:"Hii",2:"Hello",3:"Good"}
del d2[1]
print(d2)

#clear all items
d2={1:"Hii",2:"Hello",3:"Good"}
d2.clear()
print(d2)





















