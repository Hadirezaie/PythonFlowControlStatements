lst1=eval(input("Enter the list of elements: "))
print(lst1)
lst2=[]
for each_value in lst1:
    if each_value not in lst2:
        lst2.append(each_value)
print(lst2)

#  second method
set1= set(lst1)
print(set1)