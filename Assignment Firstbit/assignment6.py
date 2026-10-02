# Write a program print following patterns:
for i in range(1, 6):
    for j in range(1, 6):
        if(i==1 or i==5 or j==1 or j==5):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
rows = 4

for i in range(rows):
    # Print spaces for alignment
    print(" " * (rows - i - 1), end="")
    
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()


num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
        
print() 

for i in range(1, 6):
    for j in range(i):
        # chr(65) is 'A', chr(66) is 'B', etc.
        print(chr(65 + j), end=" ")
    print()
    
for i in range(1, 6):
    for j in range(1, 6 + 1):
        print('', end="")
        for j in range(1, i + 1):
            print('*', end="")
            
rows = 5

for i in range(1, rows + 1):
    # Print spaces
    print("  " * (rows - i), end="")
    # Print letters
    for j in range(2 * i - 1):
        print(chr(65 + j), end=" ")
    print()