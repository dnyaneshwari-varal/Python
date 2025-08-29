data=[1,2,3,4,5,6]
data2=["a","b"]
#append
data.append("merge 2 list")
print(data)#[1, 2, 3, 4, 5, 6, 'merge 2 list']


#extend
data.extend(data2)
print(data)#[1, 2, 3, 4, 5, 6, 'merge 2 list', 'a', 'b']


data2.extend(data)
print(data2)

data2.extend("varal")
print(data2)


#insert
data3=['a','b',"seed","c","d"]
data3.insert(3,"Pune")
print(data3)


#reverse
data3=['a','b',"seed","c","d"]
data3.reverse()
print(data3)


#sort
data5=[4,2,6,3,8,5,1]
data5.sort()
print(data5)#[1, 2, 3, 4, 5, 6, 8] accending order

data5=[4,2,6,3,8,5,1]
data5.sort(reverse=True) #decending order 
print(data5)#[8, 6, 5, 4, 3, 2, 1]


##########################################
#using len
a=[1,2,3,4,5,6,8]
print(len(a))


a=[1,2,3,2]
b=a.copy()
print(b)

a=[1,2,3,4,2,6]
print(a.count(2))

a=[1,2,3,4,2,6]
print(a.index(4))

nums=[2,3,5,7]
nums.reverse()
print("reverse list: ",nums)

xnums=[10,2,8,6,4]
xnums.sort()
print(xnums)
xnums.sort(reverse=True)
print(xnums)


programming_language=["python","swift","java","c","cpp","go"]
programming_language.sort(key=len)
print(programming language)

bers
my_numbers=[10,8,3,22,33,7,11,100,54]
my_number_sorted=sorted(my_numbers)
print(my_numbers)
print(my_number_sorted)


lt1=[5,10,15,20,25,30]
lt2=[2,4,6,8,10,12]
print("minimum value element: "min(lt1))
print("maximum value element: "max(lt2))

res_lt=[]
for x in range(0,len(lt1)):
    res_lt.append(lt1[x]+lt2[x])
print("addition of list lt1 and lt2: "+str(res_lt))



lt1=[5,10,15,20,25,30]
print("total element: ",len(lt1))




















