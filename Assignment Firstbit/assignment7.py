n = 5

# Upper half of diamond
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")                      
print()

# Lower half of diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")         
print()


n = 5

# Upper increasing stars
for i in range(1, n + 1):
    print("* " * i)

# Lower decreasing stars
for i in range(n - 1, 0, -1):
    print("* " * i)
    
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # Print numbers on edges, space inside
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
print()

n = 5

for i in range(1, n + 1):
    # Spaces for alignment
    print("  " * (n - i), end="")
    
    # Print numbers from 1 to (2 * i - 1)
    for j in range(1, 2 * i):
        print(j, end=" ")
print()


n = 5

for i in range(1, n + 1):
    # Spaces for alignment
    print(" " * (n - i), end="")
    
    # Numbers with hollow center
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
    
    
n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = 5

for i in range(1, n + 1):
    # Spaces for alignment
    print("  " * (n - i), end="")
    
    # Increasing part: 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")
      
        
    # Decreasing part: (i - 1) down to 1
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
        
    print()