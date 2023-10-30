# The program asks the user for input N (positive integer) and reads it
N = int(input("Please enter N: "))

numbers = []

# The program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
for i in range(N):
  numbers.append(int(input("Please enter the next number: ")))

X = int(input("Please enter X: "))

# The program asks the user to input X (integer) and outputs: "-1" if there were no such X among N read numbers
# or the index (from 1 to N) of this X if the user inputted it before.

idx = -1
for i in range(N):
  if numbers[i] == X:
    idx = i
    break

print("X index is:")
if idx == -1:
  print(-1)
else:
  print(idx + 1)
