myDict = {}
myDict1 = {}
lst={}
i,j,match,m,n=0,0,0,0,0

m= int(input("Enter number of MATCHES "))

for i in range(m):

    match=(input("\nenter Match name "))
    n = int(input("enter NUMBER of PLAYERS "))
    
    for i in range(n):
        name=(input("\nenter names  "))
        score=(input("enter score "))
        myDict1[name] = score
    
    myDict[match] = myDict1.copy()
    myDict1={}

for i in myDict.keys():
    m=myDict[i]
    for j in m:
        if(j not in lst):
            lst[j]=m[j]
        else:
            lst[j]=(int(m.get(j))+int(lst.get(j)))
            
temp = []
for i in lst:
    temp.append(int(lst[i]))
m = max(temp)
print(m)
l = lst.keys()
for i in l:
    if(int(lst[i]) == m):
        print(i,lst[i])

    
