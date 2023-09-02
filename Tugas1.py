import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

data = pd.read_csv('Customers.csv')

# Drop unnecessary columns
columns_to_drop = ['Gender', 'Profession', 'Work Experience', 'Family Size']
data = data.drop(columns_to_drop, axis=1)

# Filter data with age < 20
data = data[data['Age'] < 20]

# Calculate quantiles for both columns
quantiles_column1 = data['Age'].quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9])
quantiles_column2 = data['Spending Score (1-100)'].quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9])

# Create Q-Q plot
plt.scatter(quantiles_column1, quantiles_column2)
plt.xlabel('Quantiles of Age')
plt.ylabel('Quantiles of Spending Score (1-100)')
plt.title('Q-Q Plot - Comparing Age and Spending Score')

plt.show()