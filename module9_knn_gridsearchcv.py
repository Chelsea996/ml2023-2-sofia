import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

def read_data(size):
    X = []
    Y = []
    for i in range(size):
        x = float(input("Please enter the next x value: "))
        y = int(input("Please enter the next y value: "))
        if y < 0:
            print("Error: y is negative")
            exit(0)
        X.append([x])
        Y.append(y)
    return (np.array(X), np.array(Y))

# The program asks the user for input N (positive integer) and reads it
N = int(input("Please enter N: "))
if N <= 0:
    print("Error: N is not positive")
    exit(0)

# Read trainning data
X_train, y_train = read_data(N)

# The program asks the user for input M (positive integer) and reads it
M = int(input("Please enter M: "))
if M <= 0:
    print("Error: M is not positive")
    exit(0)

# Read test data
X_test, y_test = read_data(M)

best_accuracy = -1
best_k = -1

for k in range(1, min(11, N + 1)):
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)
    y_pred = knn_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    if best_k == -1 or accuracy > best_accuracy:
        best_k = k
        best_accuracy = accuracy

print("Best k:")
print(best_k)

print("Test accuracy:")
print(best_accuracy)
