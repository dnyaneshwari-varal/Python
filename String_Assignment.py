#que_1

import re
print('''1.split the string into words while removing punchuation
2.join the words back into a sentence with a custom separation(' | ')
3.Partition the string based on the first occurrence of that character 
4.reverce the words order using split() and join
5.count vowels and consonants,numbers,special characters
6.remove Duplicate characters
7.count a specific character in string''')
#text=input("Enter text: ")
for i in range(7):
    text=input("Enter text: ")
    choice=int(input("ENTER YOUR CHOICE: "))
    

    if(choice == 1):
        print("split the string into words while removing punchuation: ")
        #print(str.split())
        #re.sub(pattern(r'[^\w\s]' replace anything not repace a-z A-Z 0-9,underscore), replacement('' means replace with nothing), text)
        words=re.sub(r'[^\w\s]','',text).split()
        print(words)
        #re.sub means replacement substitute
    
    if(choice==2):
        print('|'.join(words))

    if(choice==3):
        first_char=text[0]
        words=text.split()

        part=[]
        current=""
        for i in words:
            if i[0]==first_char and current !="":
                part.append(current.strip())
                current=i
            else:
                if current:
                    current += " "+i
                else:
                    current =i
        part.append(current.strip())

        for j in part:
            print(part)


    if(choice==4):
        word=text.split()
        word.reverse()
        reversed_text=' '.join(word)
        print(reversed_text)

    if(choice==5):
        text=text.lower()
        vowels=0
        consonants=0
        numbers=0
        special=0

        for ch in text:
            if ch in "aeiou":
                vowels +=1
            elif ch.isalpha():
                consonants +=1
            elif ch.isdigit():
                numbers +=1
            else:
                special +=1

        print("count of vowels is: ",vowels)
        print("count of consonats is: ",consonants)
        print("count of numbers is: ",numbers)
        print("count of special char is: ",special)


    if(choice == 6):
        result=""
        for ch in text:
            if ch  not in result:
                result +=ch
        print("original text: ",text)
        print("after removing duplicate: ",result)

    if(choice==7):
        specific_char=input("Enter specif character: ")
        count=0
        for ch in text:
            if ch==specific_char:
                count +=1

        if count>0:
             print("specific character {} occures {} times: ".format(specific_char,count))    
        else:
             print("specific char {} is not present in text".format(specific_char))






            
