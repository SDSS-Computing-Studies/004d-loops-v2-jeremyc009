num=int(input("Enter an integer smaller than 10: "))
if num>=10:
    print("That integer is larger than 10")
    quit()
digit="1"
a=0
b=0
c=0
d=0
for i in range(1,num+1):
    
    b=int(i*digit)
    d=b+c
    c=d
    
    
print("the sum of the series is "+str(d))

    
    
