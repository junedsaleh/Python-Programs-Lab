city = []
lst = []
i=0
j=0

n = int(input("enter list size "))

while(i < n):
    city.append(input("enter city "))
    i = i + 1  

ch = input("enter character ")

while(j < len(city)):
    lst.append(city[j].count(ch))
    j = j + 1

print("\ncitys are : ")
print(city)

print("occurance of character : ")
print(lst)
print("---End---")
