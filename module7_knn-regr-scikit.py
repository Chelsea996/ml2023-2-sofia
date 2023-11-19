import numpy as np
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor

# The program asks the user for input N (positive integer) and reads it
N = int(input("Please enter N: "))

# The program asks the user for input k (positive integer) and reads it
k = int(input("Please enter k: "))

# Data initialization
X = []
y = []

# The program asks the user to provide N (x, y) points (one by one) and reads all of them
for i in range(N):
    X.append([float(input("Please enter the next x value: "))])
    y.append(float(input("Please enter the next y value: ")))

X = np.array(X)
y = np.array(y)

# Train the k-NN model
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X, y)

# The program asks the user to input X (integer)
x = [[float(input("Please enter x for prediction: "))]]

# and outputs: ther result (Y) of k-NN Regression if k <= N
if k <= N:
    prediction = knn_model.predict(x)
    
    print("k-NN prediction result is: ")
    print(prediction[0])

    print("Coefficient of determination is: ")
    print(r2_score(y, knn_model.predict(X)))
else:
    print("Error: k is larger than N")
