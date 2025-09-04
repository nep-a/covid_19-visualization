import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('COVID_19 Dataset.csv')
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns

# First subplot: density plot
df.plot(kind='density', y='total_tests', ax=axes[0])
axes[0].set_xlabel('Population')
axes[0].set_ylabel('Total Tests')
axes[0].set_title('Population vs Tests')
axes[0].grid(axis='y', color='g')

# Second subplot: scatter plot
df.plot(kind='scatter', x='continent', y='total_cases', ax=axes[1])
axes[1].set_xlabel('Continent')
axes[1].set_ylabel('Cases')
axes[1].set_title('Cases Per Continent')

# Add overall title
plt.suptitle('Covid-19 Global Data')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()
