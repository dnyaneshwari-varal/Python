#code1
print("code 1")
message='python is easy to learn'
print(message.endswith('easy')) #false
print(message.endswith ('to learn')) #true
print(message.startswith('pyth')) #true
print(message.startswith('python is')) #true
print(message.startswith('Pyth')) #false


#code2
print()
print("code2")
name="Student"
age=26
greeting="my name is {} and I am {} year old.".format(name,age)
print(greeting)
greeting="my name is {0} and I am {1} year old.".format(name,age)
print(greeting)

#code3
print()
print("code3")
greeting="my name is {name_stud} and I am {age_stud} years old".format(name_stud="sumit",age_stud=25)
print(greeting)
#output=my name is sumit and I am 25 years old


#code4
print()
print("code 4")
print("python  "*4) #print python 4 times
#output= python  python  python  python 


#code5
print()
print("code5")
print("Default argument")
print("Hi {}, contacjt no-{}".format("sakshi",1234567))

#code6
print()
print("code6")
print("positional argument")
print("Hi {0}, contacjt no-{1}".format("sakshi",1234567))


#code 7
print()
print("code7")
print("keyword argument")
print("Hi there {name} and I am {conum} year old".format(name="sakshi",conum=1234567))

#code 8
print("code 8")
print("mixed argument")
print("hello {0}, your balance is {blc}".format("sham",blc=12345))

#code9
print("code 9")
age=10
gret=f"My name is {name} and I am {age+1} year old"
print(gret) #My name is Student and I am 11 year old
print(f"Next year, {name} and I am {age+1} year old")



#code10
print("code 10")
#n is line boundary
text=''''python is easy to learn \n
It is oop based\n its super cool language'''
#split text from space
print(text.splitlines())


#code11
print("code11")
numbers=["1","2","3","4"]
comma_seperated=", ".join(numbers)
print(comma_seperated)


#code12
print("code12")
words=["python","java","are","languages"]
space_seperated=", ".join(words)
print(space_seperated)



#code 13
print("code13")
text="hello ,to the world of python!"
result=text.partition(",")
print(result)


#code14
text="It is raining"
print(text.zfill(15))
print(text.zfill(30))
print(text.zfill(65))


#code15
number="-246"
print(text.zfill(15))
number="+523"
print(text.zfill(6))
text="--random+text"
print(text.zfill(20))






































