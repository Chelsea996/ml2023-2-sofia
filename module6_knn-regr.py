import numpy as np

# The program asks the user for input N (positive integer) and reads it
N = int(input("Please enter N: "))

# The program asks the user for input k (positive integer) and reads it
k = int(input("Please enter k: "))

# Data initialization
XY = []

# The program asks the user to provide N (x, y) points (one by one) and reads all of them
for i in range(N):
    x = float(input("Please enter the next x value: "))
    y = float(input("Please enter the next y value: "))
    XY.append([x, y])

XY = np.array(XY)

# The program asks the user to input X (integer)
x = float(input("Please enter x for prediction: "))

# and outputs: ther result (Y) of k-NN Regression if k <= N
if k <= N:
    # calculate the distance
    XY[:, 0] = np.abs(XY[:, 0] - x)

    # sort the distance
    XY = XY[np.argsort(XY[:, 0])]

    # calculate the average
    y = np.mean(XY[:k, 1])
    
    print("k-NN prediction result is: ")
    print(y)
else:
    print("Error: k is larger than N")
