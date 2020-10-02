num=int(input("Enter a number: "))
num1=0
num2=1
for i in range (0,num):
    num1=num-i
    num2=num1*num2

print(str(num)+"! is "+str(num2) +" where "+str(num)+" is the integer entered and " +str(num2)+ " is the calculated answer")

    
