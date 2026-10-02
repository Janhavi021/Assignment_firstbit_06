# 1. Python Program to Add a Key-Value Pair to the Dictionary using data structures
dictionary = {}
key = input("Enter the key: ")
value = input("Enter the value: ")
dictionary[key] = value
print("Updated dictionary:", dictionary)
# 2. Python Program to Concatenate Two Dictionaries Into One
dict1 = {"id": 1, "name": "Alice"}
dict2 = {"age": 25, "city": "New York"}
concatenated_dict = {**dict1, **dict2}
print("Concatenated dictionary:", concatenated_dict)
# 3. Python Program to Check if a Given Key Exists in a Dictionary or Not
key_to_check = input("Enter the key to check: ")
if key_to_check in dictionary:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n = int(input("Enter a number: "))
squares_dict = {x: x*x for x in range(1, n+1)}
print("Dictionary with squares:", squares_dict)

# 5. Python Program to Sum All the Items in a Dictionary
dic={"id":1,"name":"Alice","age":25}
sum_of_values = sum(dic.values())
print("Sum of all values in the dictionary:", sum_of_values)

#Python Program to Multiply All the Items in a Dictionary
dic={"id":1,"name":"Alice","age":25}
product_of_values = 1
for value in dic.values():
    product_of_values *= value
print("Product of all values in the dictionary:", product_of_values)

#Python Program to Remove the Given Key from a Dictionary
key_to_remove = input("Enter the key to remove: ")
if key_to_remove in dic:    
    del dic[key_to_remove]
    print(f"Key '{key_to_remove}' removed. Updated dictionary:", dic)
else:
    print(f"Key '{key_to_remove}' not found in the dictionary.")

#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
string = input("Enter a string: ")
words = string.split()
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print("Word frequency dictionary:", word_frequency)


