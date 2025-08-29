#que_1

import re
  
while True:
    print('''1.split the string into words while removing punchuation
         2.join the words back into a sentence with a custom separation(' | ')
         3.Partition the string based on the first occurrence of that character 
         4.reverce the words order using split() and join
         5.count vowels and consonants,numbers,special characters
         6.remove Duplicate characters
         7.count a specific character in string''')

    text=input("Enter text: ")
    choice=int(input("ENTER YOUR CHOICE: "))
    

    if(choice == 1):
        print("split the string into words while removing punchuation: ")
        #print(str.split())
        #print(words)
        for ch in text:
           if ch.isalnum() or ch ==' ':
               print(ch, end=" ")
        print() 
        
    
    if(choice==2):
        print("2.join the words back into a sentence with a custom separation(' | ')")
        
        print('|'.join(words))

    elif(choice==3):
        print("3.Partition the string based on the first word occurrence of that character ")
        words=input("enter seperator: ")
        part=text.partition(words)
        print("partition of string is: ",part)
    elif(choice==4):
        word=text.split()
        word.reverse()
        reversed_text='|'.join(word)
        print(reversed_text)

    elif(choice==5):
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


    elif(choice == 6):
        result=""
        for ch in text:
            if ch  not in result:
                result +=ch
        print("original text: ",text)
        print("after removing duplicate: ",result)

    elif(choice==7):
        specific_char=input("Enter specif character: ")
        count=0
        for ch in text:
            if ch==specific_char:
                count +=1

        if count>0:
             print("specific character {} occures {} times: ".format(specific_char,count))    
        else:
             print("specific char {} is not present in text".format(specific_char))






            
