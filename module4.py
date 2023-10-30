N = int(input("Please enter N: "))

numbers = []

for i in range(N):
  numbers.append(int(input("Please enter the next number: ")))

X = int(input("Please enter X: "))

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
