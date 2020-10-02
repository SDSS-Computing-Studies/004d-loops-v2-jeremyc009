nameList=("Lebron", "Kobe","Michael","Shaq","Dennis",)
name=input("Enter a name: ")
value=name in nameList
for name in nameList:
    if value==True:
        print("That name is on the list")
        break
    else: 
        print("That name is not on the list")
        break

    
