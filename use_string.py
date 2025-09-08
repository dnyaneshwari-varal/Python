#que_1


  
def string_word(text):
        print("split the string into words while removing punchuation: ")
        #print(str.split())
        #print(words)
        for ch in text:
           if ch.isalnum() or ch ==' ':
               print(ch, end=" ")
        print() 
        
    
def join_word(text):
        print("2.join the words back into a sentence with a custom separation(' | ')")
        words=text.split()
        print('|'.join(words))

def string_partition(text):
        print("3.Partition the string based on the first word occurrence of that character ")
        words=input("enter seperator: ")
        part=text.partition(words)
        print("partition of string is: ",part)
  

def count_vcns(text):
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


def remove_dup(text):
        result=""
        for ch in text:
            if ch  not in result:
                result +=ch
        print("original text: ",text)
        print("after removing duplicate: ",result)

    
  

        


            
