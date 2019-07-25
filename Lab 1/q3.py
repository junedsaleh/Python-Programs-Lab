names = []
city = []
mobile = []
i=0

n = int(input("enter list's size "))

while(i < n):
    names.append(input("\nenter names  "))
    city.append(input("enter city  "))
    mobile.append(input("enter mobile  "))
    i = i + 1  

ch = input("\nenter city to search ")

print(names[city.index(ch)])
print(mobile[city.index(ch)])
    
print("\n---End---")
