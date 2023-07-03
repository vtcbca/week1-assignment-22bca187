##5.Write a python script to enter any string and count vowel.

def countvowl(stri):
    cou=0
    vow=('a','e','i','o','u','A','E','I','O','U')

    for i in stri:
        if i in vow:
            cou=cou+1
    print(f"The vowels count in '{stri}' is {cou}")


strig=input("Enter a string:")
countvowl(strig)