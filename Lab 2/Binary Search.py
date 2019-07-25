lst=[]
i,j,high,low,mid,found=0,0,0,0,0,False

n = int(input("enter list's size "))

while(i < n):
    lst.append(int(input("enter num  ")))
    i = i + 1
print(lst)

high=len(lst)-1

se = int(input("enter search element "))

while(low <= high and found == False):

    mid=int((high+low)/2)

    if(lst[mid] == se):
        found=True
    elif(lst[mid]<se):
        low=mid+1
    else:
        high=mid-1

print(found)
print("----- END -----")
            
