#print("hello im  amirhossein_gheitasi")
wood_list=[]
while True:
    print("1)add wood")
    print("2)woods list")
    print("3)find best wood")
    print("0)Exit")
    print("-"*30)
    choice=int(input("Enter your choice:  "))

    if choice==0:
        break

    elif choice==1:
        wood = input("Enter wood:")
        wood_list.append(wood.capitalize())
        print("wood added")


    elif choice ==2:
        print("wood list:",wood_list)


    elif choice==3:
        wood=input("Enter wood to search:").capitalize()

        if wood in wood_list:
            print("wood found")

        else:
            print("wood not found!!!")

    else:
        print("Invalid choice!!!")

    print("-"*50)