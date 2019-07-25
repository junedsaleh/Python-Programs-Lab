
lst=[11,12,1,44,44,44,1,1,11,11,11]
lst1,mode=[],[]
i,m,j=0,0,0


for i in lst:
    m=lst.count(i)
    if(m>1):
        if(i not in lst1):
            lst1.append(i)
            mode.append(m)


print("your list ",lst)
print("modes on ",lst1)
print("mode count ",mode)


if(mode == [] ):
	print("no mode")
elif(mode.count(max(mode)) == 1):
	print("uni mode", max(mode) ,"times")
elif(mode.count(max(mode)) > 1):
	print("multie mode")
