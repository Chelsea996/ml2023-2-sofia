import numpy as np
from sklearn.metrics import precision_score, recall_score

# The program asks the user for input N (positive integer) and reads it
N = int(input("Please enter N: "))

# Data initialization
X = []
Y = []

# The program asks the user to provide N (x, y) points (one by one) and reads all of them
for i in range(N):
    X.append(int(input("Please enter the next x value: ")))
    Y.append(int(input("Please enter the next y value: ")))

X = np.array(X)
Y = np.array(Y)

# Calculate precision
precision = precision_score(X, Y)
print("Precision:")
print(precision)

# Calculate recall
recall = recall_score(X, Y)
print("Recall:")
print(recall)
