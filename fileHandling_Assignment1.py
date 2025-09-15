'''
#Q1. write a code to store details of 4-5 students in file named student.txt (Roll, Name, Percentage) and display the details of student in upper case.
try:
  while True:
    data=open("stud_info.txt","a+")
    Roll_no=int(input("Enter roll no of student: "))
    name=input("Enter student name: ")
    Perc=float(input("Enter persentage of student: "))

    dataW=f"Roll no:{Roll_no},Name: {name},percentage:{Perc}\n"
    data.write(dataW)
    data.close()

    ch=input("Want to continue then press y else n: ")
    if ch=="n":
        break
except Exception as e:
    print("Some exception: ",e)
    
#display
print("--Student data--")
data=open("stud_info.txt","r")
for line in data:
  print(line.upper(), end="")
'''

#write one paragraph or poem and store in poem.txt and find out the number of vowels & consonant and numbers from that file.
  
#Poem.txt

try:
  file=open("Poem.txt","r")
  data=file.read()
  perfOpe=data.lower()
  vowel=0
  cons=0
  num=0
  for i in perfOpe:
    if i in "aeiou":
      vowel +=1
    elif i.isalpha():
      cons +=1
    if i in "0123456789":
      print(i)
      num+=1

  print("Vowel: ",vowel)
  print("Consonants: ",cons)
  print("Number: ",num)
except:
  print("Some error occure")
