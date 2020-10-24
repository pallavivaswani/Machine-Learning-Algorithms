import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading Data
data = pd.read_csv('AreaRent.csv')
print("DATASET \n",data)

# Collecting X and Y
X = data['Area'].values
Y = data['Rent'].values

# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)
 
# Total number of values
n = len(X)

# Using the formula to calculate m and c
numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)
 
# Print coefficients
print("\nb1=" , b1 , "\nb0=" ,b0)

#Print Equation
print("Therefore, \nThe Linear Regression for given model is: y=",round(b1,3),"x+ (",round(b0,3),")")

#Finding Value of y
X1=input("Predicting Rent \n Enter Area(X): ")
y1= b1*float(X1) + b0
print("Area ", X1, "sq. ft has Rent of Rs. = ",y1)

# Plotting Values and Regression Line
max_x = np.max(X) + 5
min_x = np.min(X) - 5
# Calculating line values x and y
x = np.linspace(min_x, max_x)
y = b0 + b1 * x 
 
# Ploting Line
plt.plot(x, y, c='#52b920', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef4423', label='Scatter Plot')
plt.xlabel('Area')
plt.ylabel('Rent')
plt.legend()
plt.show()
