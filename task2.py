nameList=("Lebron", "Kobe","Michael","Shaq","Dennis")
name=input("Enter a name: ")
value=name in nameList
for name in nameList:
    if value==True:
        print("The name is a match.")
        break
    else: 
        print("The name does not match.")
        break

    
