# 1. Python Program to Put Even and Odd elements of a List into two Different Lists
li=[20,30,40,50,60,70,80,90,100]
even_li=[]
odd_li=[]
for ind in range(len(li)):
    if li[ind]%2==0:
        even_li.append(li[ind])
    else:
        odd_li.append(li[ind])
print("Even elements:", even_li)
print("Odd elements:", odd_li)
# 2. Python Program to Merge Two Lists and Sort it
li1=[1, 2, 3, 4, 5]
li2=[6, 7, 8, 9, 10]
merged_li=li1+li2
merged_li.sort()
print("Merged and sorted list:", merged_li)

# 3. Python Program to Sort the List According to the Second Element in Sublist
li=[[1, 2], [3, 1], [5, 4], [2, 3]]
li.sort(key=lambda x: x[1])
print("List sorted by second element:", li)

# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort
li=[10, 20, 30, 40, 50]
n=len(li)
for i in range(n):
    for j in range(0, n-i-1):
        if li[j] < li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print("Second largest number:", li[1])

# 5. Python Program to Sort a List According to the Length of the Elements within the list.
li=["apple", "banana", "cherry", "date"]
li.sort(key=len)
print("List sorted by length:", li)

# 6. Python Program to Find the Union of two Lists
li1=[34, 54, 67, 89, 90]
li2=[]
union_li=list(set(li1) | set(li2))
print("Union of lists:", union_li)

# 7. Python Program to Find the Intersection of Two Lists.
li1=[34, 54, 67, 89, 90]
li2=[34, 54, 67, 89, 90]
intersection_li=list(set(li1) & set(li2))
print("Intersection of lists:", intersection_li)

# 8. Print 1 to 100 in snakes and ladder pattern.
li=[i for i in range(1, 101)]
for i in range(10):
    if i % 2 == 0:
        print(li[i*10:(i+1)*10])
    else:
        print(li[i*10:(i+1)*10][::-1])
# 9. Write a program to create three lists of numbers, their squares and cubes.
li=[1, 2, 3, 4, 5]
squares_li=[x**2 for x in li]
cubes_li=[x**3 for x in li]
print("Original list:", li)
print("Squares list:", squares_li)
print("Cubes list:", cubes_li)

# 10. Write a program to print list after removing even numbers.
li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li=[x for x in li if x%2!=0]
print("List after removing even numbers:", li)
