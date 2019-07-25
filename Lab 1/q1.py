name = []
lst = []
i=0

n = int(input("enter list size "))

while(i < n):
    name.append(input("enter name "))
    lst.append([i,name[i]])
    i = i + 1  

print(name)
print(lst)
print("---End---")
