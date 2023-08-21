#3.Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.

def pali(num):
    if(num.isdigit()):
        ans=str(num)
        if(ans==ans[::-1]):
            print(f"The number {num} is a palindrome number!!")
        else:
            print(f"The number {num} is not a palindrome number!!")
    else:
        print(f"The given input {num} is not valid number!!")

number=input("Enter a number!!:")
pali(number)