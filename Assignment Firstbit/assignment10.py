# (Do all questions without using inbuilt functions)
# Write a program to find sum of all elements of list
from numpy import number


li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum=0
for i in li:
    sum+=i
print("Sum of all elements:", sum)
# Write a program to find maximum and minimum element in a list.
li=[45,34,81,77,53,34,26,82]
max=li[0]
for ind in range(1,len(li)):
    if li[ind]>max:
        max=li[ind]
print("Maximum element:", max)
min=li[0]
for ind in range(1,len(li)):
    if li[ind]<min:
        min=li[ind]
print("Minimum element:", min)

# Write a program to find the second largest element in the list.
li=[45,34,81,77,53,34,26,82]
max1=li[0]
max2=li[0]
for ind in range(1,len(li)):
    if li[ind]>max1:
        max2=max1
        max1=li[ind]
    elif li[ind]>max2 and li[ind]!=max1:
        max2=li[ind]
print("Second largest element:", max2)

# Write a program to reverse the list.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_li=[]
for ind in range(len(li)-1,-1,-1):
    reversed_li.append(li[ind])
print("Reversed list:", reversed_li)
# Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num=int(input("Enter a number to check: "))
count=0
for ind in range(len(li)):
    if li[ind]==num:
        count+=1
if count>0:
    print("Element is present in the list.")
    print("Number of times it is present:", count)
else:
    print("Element is not present in the list.")
    
# Write a program to remove duplicates from the list.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
unique_li=[]
for ind in range(len(li)):
    if li[ind] not in unique_li:
        unique_li.append(li[ind])
print("List after removing duplicates:", unique_li)

# 7. Write a program to create a new list from existing list which contains cube of each number of list.
li=[1, 2, 3, 4, 5]
cube_li=[]
for ind in range(len(li)):
    cube_li.append(li[ind]**3)
print("List of cubes:", cube_li)

# 8. Write a program to create a duplicate of an existing list. It should not point to same list.
li=[1, 2, 3, 4, 5]
duplicate_li=[]
for ind in range(len(li)):
    duplicate_li.append(li[ind])
print("Duplicate list:", duplicate_li)

# 9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have even elements and other will have odd elements.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_li=[]
odd_li=[]
for ind in range(len(li)):
    if li[ind]%2==0:
        even_li.append(li[ind])
    else:
        odd_li.append(li[ind])
print("Even elements:", even_li)
print("Odd elements:", odd_li)

# 10. Write a program to remove all occurrences of a given element in the list.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element=int(input("Enter the element to remove: "))
li=[x for x in li if x!=element]
print("List after removing the element:", li)

# 11. Write a program to print all numbers which are divisible by m and n in the list.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
print("Numbers divisible by both", m, "and", n, ":")
for num in li:
    if num%m==0 and num%n==0:
        print(num)
    else:
        print(num, "is not divisible by both", m, "and", n)
        
# 12. Write a program to create three lists of numbers, their squares and cubes.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares=[x**2 for x in li]
cubes=[x**3 for x in li]
print("Original list:", li)
print("Squares:", squares)
print("Cubes:", cubes)

# 13 . Write a program to print list after removing even numbers.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li=[x for x in li if x%2!=0]
print("List after removing even numbers:", li)