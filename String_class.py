#code1
s1="HELLOWORLD"
print(s1[2:6])   #LLOW
print(s1[2:-4]) #LLOW
print(s1[4:-2])  #OWOR
print(s1[-7:-2])#LOWOR
print(s1[4:]) #OWORLD
print(s1[:7]) #HELLOWO
print(s1[::-1]) #DLROWOLLEH
print(s1[2:9:2]) #LOOL
print(s1[-7:-1:2]) #LWR


#code2
data=[1,2,3,[22,34,56],12.2,"Dnyana"]

for i in data:
    print(i)
print(data[3])


#code3
data=[1,2,3,[22,34,56],12.2,"Dnyana"]
for i in data[3]:
    print(i)
#output: 22 34,56



#membership opetator for string
#code4
str1="dnyaneshwari"
str2="shivani"
print("Dn" in str1)
print("yh" not in "python")
print("ne" not in str1)
print("xz" in str1)

print(str1==str2)
print(len(str1))
print(len(str2))
print(str1>str2) # why it give false?  its not compare char to char it compare character ascii value




#code5
example="Hello Emma,\"Whats up?\""
print(example)

#escape single quotes

example='She responded saying,"\t\it\'s Diwali festival"'
print(example)

print('certificates\\Awards')
print('Hello\t There')
print('One \nTwo')





#code6 count() method
msg="Python is popular programming language"
print("Occurance of p: ",msg.count("po")) #1
print("occurance of  p: ",msg.count("p")) #3

#code 6 endswith()
msg="Python is popular and easy to learn"
print(msg.endswith("easy to Learn")) #false
print(msg.endswith("easy to learn")) #True
print(msg.endswith("to learn"))  #true
print(msg.endswith("to no")) #false

#code 7 startswith()
msg="Python is popular and easy to learn"
print(msg.startswith("easy to Learn")) #false
print(msg.startswith("python")) #False
print(msg.startswith("Python is"))  #true



#code8 split()
data='''hello student
to the class
'''
print(data.split())
print(data.splitlines())



#code9 zfill
text="it is raining"
print(text.zfill(15))  #00it is raining
















