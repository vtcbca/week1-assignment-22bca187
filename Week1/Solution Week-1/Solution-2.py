#2.Write a python script to enter any number and print the sum of its digit.

def sum(num):
    rem=0
    sum=0
    ans=num
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n=n//10
    print(f"The sum of digit of number {ans} is {sum}!")  

number=int(input("Enter a number:"))
sum(number)    