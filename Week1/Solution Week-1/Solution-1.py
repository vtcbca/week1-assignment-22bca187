#1.Write a Python script to enter an y number and check its prime or not
def prime(num):
    ans=True
    for i in range(2,num):
        if(num%2==0):
            ans=False
    if(ans==True):
        print(f"Number {num} is prime!!")
    else:
        print(f"Number {num} is not prime!!")


number=int(input("Enter a number:"))
prime(number)