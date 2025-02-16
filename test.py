import numpy as np
from matplotlib import pyplot as plt

# Example data (you should replace these with your actual arrays)
array_predict = np.array([10, 20, 30, 40, 50])
array_test = np.array([12, 18, 29, 42, 48])

# Calculate the discrepancy
discrepancy = array_predict - array_test

# Create a figure with two subplots
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# First plot: Predicted vs. Test values
ax[0].plot(array_test, label="Test Values", marker='o', linestyle='', color='blue')
ax[0].plot(array_predict, label="Predicted Values", marker='x', linestyle='', color='red')
ax[0].set_title("Predicted vs. Test Values")
ax[0].set_xlabel("Index")
ax[0].set_ylabel("Value")
ax[0].legend()

# Second plot: Discrepancy between predicted and test values
ax[1].bar(np.arange(len(discrepancy)), discrepancy, color='orange')
ax[1].set_title("Discrepancy between Predicted and Test Values")
ax[1].set_xlabel("Index")
ax[1].set_ylabel("Discrepancy")

# Show the plot
plt.tight_layout()
plt.show()