#4.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.

def arms(num):
    if(num.isdigit()):
   
        num=int(num)
        ans=num
        rem=0
        sum=0
   
        while(num!=0):
            rem=num%10
            sum=sum+(rem**3)
            num=num//10
        if(ans==sum):
            print(f"The number {ans} is an armstrong number!")
        else:
            print(f"The number {ans} is  not an armstrong number!")
    else:
        print(f"The given input {num} is not valid number!!")


number=input("Enter a number!!:")
arms(number)