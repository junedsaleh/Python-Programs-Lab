lst, lst1, i ,j = [], [], 0, 0

n=int(input("enter size of array "))

while(j<n):
    lst.append([int(input("\nenter num 1 ")),int(input("enter num 2 ")),int(input("enter num 3 "))])
    j=j+1

for i in lst:
    if( (i[0] + i[1]) == i[2]):
        lst1.append("T")
    else:
        lst1.append("F")
        

print(lst)
print(lst1)
            
