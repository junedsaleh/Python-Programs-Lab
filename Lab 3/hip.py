lst = [19,15,13,12,16,21,3,2,11]
i,j,k=0,0,0
n=(len(lst))//2
swap=0
#print(n)

print("before swap",lst)
print()

for i in lst:
    while(n>j):
            l=(2*n)
            r=(2*n)+1
            #print(l,r)
            if(r > (len(lst)-1) ):
                if(lst[l]>lst[n] ):
                    lst[l],lst[n]=lst[n],lst[l]
                    swap=1
            elif((lst[l]>lst[n] or lst[r]>lst[n])):
                if(lst[l]>lst[r]):
                    lst[l],lst[n]=lst[n],lst[l]
                    swap=1
                else:
                    lst[r],lst[n]=lst[n],lst[r]
                    swap=1
            n=n-1
            k=k+1
    if(k > len(lst)*4):
        continue
            
print("after swap",lst)
