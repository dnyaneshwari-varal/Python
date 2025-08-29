#1
#update and delete elements

while True:
    print("1.update and delete elements")
    choice=int(input("Enter your choice: "))

    
    if(choice==1):
        lst=["Apple","Mango","Grapes","Banana","Chery"]
        print(lst)
        #replace 3rd fruit with another fruit
        lst[2]="Orange"
        print(lst)
        #remove last fruit
        lst_size=len(lst)
        lst.remove(lst[lst_size-1])
        print(lst)
        #insert new fruit at the beginning
        lst.insert(0,"kiwi")
        print(lst)


    elif(choice==2):
        lst=["Ram","Sham","Tulsidas","sita"]

        name=input("enter name which you want to search: ")
        size=len(lst)
        for i in range(0,size):
            if(lst[i]==name):
                print("name {} is present in list ".format(name))
                break


    elif(choice==3):
        lst=[[25,28,19],[29,27,20],[19,26,30]]
        print("marks of student 2 in subject 3 is ",lst[1][2])

    elif(choice==4):
        print("find common elements from 2 list")
        lst1=[10,20,43,23,67]
        lst2=[30,40,10,23,78]
        for i in lst1:
            for j in lst2:
                 if(i == j ):
                     print("common element is: ",i)
                     break
    elif(choice==5):
        print("remove duplicates:")
        lst=[10,20,40,38,10,20,10,20]
        result=[]
        for i in lst:
            if i not in result:
                result.append(i)
        for i in result:
            print(i,end=" ")
        print()

















                
