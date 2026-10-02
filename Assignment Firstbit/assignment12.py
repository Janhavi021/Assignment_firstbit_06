# Python Program to Replace all Occurrences of ‘a’ with $ in a String using data structures
string = input("Enter a string: ")
string = string.replace('a', '$')
print("Modified string:", string)

# Python Program to Remove the nth Index Character from a Non-Empty String
string = input("Enter a string: ")
n = int(input("Enter the index of the character to remove: "))
if 0 <= n < len(string):
    string = string[:n] + string[n+1:]
print("Modified string:", string)

# Python Program to Detect if Two Strings are Anagrams using data structures
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    
# Python Program to Form a New String where the First Character and the Last Character have been Exchanged
string = input("Enter a string: ")
if len(string) > 1:
    string = string[-1] + string[1:-1] + string[0]
print("Modified string:", string)
