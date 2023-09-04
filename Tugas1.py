import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

data = pd.read_csv('Customers.csv')
quantile_array = []

# Create an array from 1/100 to 99/100 for the quantiles argument
for i in range(1, 100):
    quantile_array.append(i/100)

# Drop unnecessary columns
columns_to_drop = ['Gender', 'Profession', 'Work Experience', 'Family Size']
data = data.drop(columns_to_drop, axis=1)

# Calculate quantiles for both columns
quantiles_column1 = data['Age'].quantile(quantile_array)
quantiles_column2 = data['Spending Score (1-100)'].quantile(quantile_array)

# Create Q-Q plot
plt.scatter(quantiles_column1, quantiles_column2)
plt.xlabel('Quantiles of Age')
plt.ylabel('Quantiles of Spending Score (1-100)')
plt.title('Q-Q Plot - Comparing Age and Spending Score')

# Plot standard distribution line
min_value = min(quantiles_column1.min(), quantiles_column2.min())
max_value = max(quantiles_column1.max(), quantiles_column2.max())
plt.plot([min_value, max_value], [min_value, max_value], color='red')
plt.savefig("Figure_1.png")
plt.show()