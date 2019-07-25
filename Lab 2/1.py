lst = []
i,j,k=0,0,0

n = int(input("enter list's size "))

while(i < n):
    lst.append(input("\nenter names  "))
    lst.append(input("enter city  "))
    lst.append(input("enter mobile  "))
    i = i + 1  

ch = input("\nenter city to search ")

print(lst)
for j in lst:
    if(j==ch):
        print("\nCity :"+lst[k])
        print("Name :"+lst[k-1])
        print("Number :"+lst[k+1])
    k = k + 1
    
print("\n---End---")
