names=[]
dot_list=['i','j']
while True:
    name=input("Enter your name:")
    names.append(name.lower())
    if name.lower()=="exit":
        print("Exit")
        break

    print("total dot in:",name.count('i')+name.count('j'))