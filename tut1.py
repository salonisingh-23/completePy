#list
shopping=["bread","curd","fruits"]
print(shopping)

for items in shopping:
    print(items)

for items in range(3):
    print(shopping[items],end=" /") #end removes next line

#Append
shopping.append("shampoo")
print(shopping)

#count
ages=[12,22,23,22,4,7,16,14,5]
print(ages.count(22))
print(ages.count(3))

#len
print(len(ages))

#insert
ages.sort()
print(ages)

#reverse
ages.reverse()
print(ages)

#mean of the list_name
import statistics
print(statistics.median(ages))

#lexographical sort
shopping.sort()
print(shopping)

#insert 
shopping.insert(1,"oil")
print(shopping)

shopping.insert(-2,"vegies") #inserts from the end
print(shopping)

shopping.insert(-6,"nutella")
print(shopping)

#slicing
#list_name[start:end+1]
#list_name[startindex:endindex+1]

print(shopping[1:5])
print(shopping[:])
print(shopping[3:])
#default start index =0, defult end index=len(list)

#concatenate and type casting
print(6+5)
print(str(6)+'a')

#remove an element at a particular element from a list
print(ages.pop())#removes from the last element
print(ages.pop())
print(ages.pop(2))
print(ages.pop(-1))
print(ages)