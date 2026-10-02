# 1. Write a Python program to find elements in a given set that are not in another set.
s1={10,20,30,40,50}
s2={40,50,60,70,80}
print("Elements in s1 but not in s2:", s1 - s2)

# 2. Write a Python program to remove the intersection of a second set with a first set.
s1={10,20,30,40,50}
s2={40,50,60,70,80}
s1 -= s2
print("Updated set s1 after removing intersection:", s1)

#Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
strings = ["hello", "world", "hello", "python", "world"]
unique_words = set(strings)
word_frequency = {word: strings.count(word) for word in unique_words}
print("Unique words:", unique_words)
print("Word frequency:", word_frequency)

#4. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
numbers = [1, 2, 3, 4, 5]
target_sum = 6
pairs = [(x, y) for i, x in enumerate(numbers) for y in numbers[i+1:] if x + y == target_sum]
print("Pairs with sum equal to", target_sum, ":", pairs)

#Write a Python program to find the longest common prefix of all strings. Use the Python set.
strings = ["hello", "help", "helicopter"]
common_prefix = set()
for s in strings:
    if not common_prefix:
        common_prefix = set(s)
    else:
        common_prefix &= set(s)
print("Longest common prefix:", ''.join(common_prefix))
# 6. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.
numbers = [1, 2, 3, 4, 5]
max_product = float('-inf')
for i, x in enumerate(numbers):
    for y in numbers[i+1:]:
        product = x * y
        if product > max_product:
            max_product = product
print("Maximum product:", max_product)
# 7. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1
print("Missing in set2:", missing_in_set2)
print("Missing in set1:", missing_in_set1)
# 8. Write a Python program to find all the anagrams and group them together from a given list of strings.
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

used = []

for i in range(len(words)):
    
    if words[i] not in used:
        
        group = [words[i]]
        used.append(words[i])
        
        for j in range(i + 1, len(words)):
            
            if sorted(words[i]) == sorted(words[j]):
                group.append(words[j])
                used.append(words[j])
        
        print(group)
# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
numbers = [2, 3, 4, 5, 6, 7, 8]
target = 15

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            
            if numbers[i] + numbers[j] + numbers[k] == target:
                print(numbers[i], numbers[j], numbers[k])    
