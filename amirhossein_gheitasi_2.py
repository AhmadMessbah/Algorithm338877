#print("hello im  amirhossein_gheitasi")

num=[]
n=int(input("Enter number:"))
for i in range(2,n+1,2):
    if i%7==0:
        num.append(i)
        print(i)
av=sum(num)/len(num)
print(av)

