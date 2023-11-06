from module5_mod import SearchableArray

# The program asks the user for input N (positive integer) and reads it
N = int(input("Please enter N: "))

# Data initialization
array = SearchableArray()

# The program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
for i in range(N):
    array.insert(int(input("Please enter the next number: ")))

X = int(input("Please enter X: "))

# The program asks the user to input X (integer) and outputs: "-1" if there were no such X among N read numbers
# or the index (from 1 to N) of this X if the user inputted it before.

print("X index is:")
print(array.search(X))

