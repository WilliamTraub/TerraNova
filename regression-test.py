import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Create a synthetic 5D dataset
np.random.seed(42)
n_samples = 1000  # Number of samples
n_features = 5    # Number of features (5D)

# Generate random features (X) with 5 dimensions
X = np.random.rand(n_samples, n_features)

# Define a linear relationship with some noise
coefficients = np.array([2.5, -1.3, 0.7, 3.2, -0.5])  # Coefficients for each feature
intercept = 1.0  # Intercept
y = np.dot(X, coefficients) + intercept + np.random.randn(n_samples) * 0.5  # Add noise

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 5: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Step 6: Interpret the results
print(f"Coefficients: {model.coef_}")  # Should be close to [2.5, -1.3, 0.7, 3.2, -0.5]
print(f"Intercept: {model.intercept_}")  # Should be close to 1.0

#plt.show()