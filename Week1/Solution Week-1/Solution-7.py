#7.Write a python script to enter any string, replace vowel with its position number.
#For Example: input: Amit
#             output:0m2t

string=input("Enter a string:")
ans=''
vo=('a','e','i','o','u','A','E','I','O','U')
for index,j in enumerate(string):
    if(j in vo):
        ans=ans+str(index)
    else:
        ans=ans+j
    
print(f"The string '{string}' after change is '{ans}' ")