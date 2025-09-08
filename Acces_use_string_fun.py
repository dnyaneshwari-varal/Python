import use_string as s
while True:
    print('''1.split the string into words while removing punchuation
         2.join the words back into a sentence with a custom separation(' | ')
         3.Partition the string based on the first occurrence of that character 
         4.count vowels and consonants,numbers,special characters
         5.remove Duplicate characters''')

    text=input("Enter text: ")
    choice=int(input("ENTER YOUR CHOICE: "))
    if choice==1:
        s.string_word(text)
    elif choice==2:
        s.join_word(text)
    elif choice==3:
        s.string_partition(text)
    elif choice==4:
        s.decount_vcns(text)

    elif choice==5:
        s.remove_dup(text)
