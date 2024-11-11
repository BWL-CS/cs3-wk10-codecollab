import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize

zoo_data = {
    'Animal': ['Tiger', 'Elephant', 'Giraffe', 'Monkey', 'Kangaroo'],
    'Count': [5, 4, 6, 15, 7],
    'Avg Weight (kg)': [190, 5000, 800, 40, 90]
}

df = pd.DataFrame(zoo_data)

# Line plot for animal count
plt.subplot(2, 2, 1)
plt.plot(df['Animal'], df['Count'], marker='o')
plt.title("Line Plot of Animal Count")
plt.xticks(rotation=45)

# Scatter plot for average weight
plt.subplot(2, 2, 2)
df_weight_sorted = df.sort_values(by='Avg Weight (kg)', ascending=False)
plt.scatter(df_weight_sorted['Animal'],
            df_weight_sorted['Avg Weight (kg)'],
            c='m')
plt.title("Scatter Plot of Avg Weight")
plt.xticks(rotation=45)

# Histogram for average weight
plt.subplot(2, 2, 3)
plt.hist(df['Avg Weight (kg)'], bins=30, alpha=0.75, color='blue')
plt.title("Histogram of Avg Weight")
plt.xticks(df['Avg Weight (kg)'])  # Set tick marks to data values
plt.tick_params(axis='x', rotation=45)

# Bar chart for animal count
plt.subplot(2, 2, 4)
df_count_sorted = df.sort_values(by='Count', ascending=False)
colors = ['red', 'yellow', 'green', 'blue', 'purple']
plt.bar(df_count_sorted['Animal'],
        df_count_sorted['Count'],
        color=colors,
        width=0.6)
plt.title("Bar Chart of Animal Count")
plt.xticks(rotation=45)

# Display 4 plots
plt.tight_layout()
plt.savefig("ZooData.png")

# Pie chart showing the animal counts
plt.figure()  # Create a new figure 
colors = ['red', 'green', 'blue', 'yellow', 'purple']
plt.pie(df['Count'],
        labels=df['Animal'].tolist(),
        colors=colors,
        autopct='%1.1f%%',
        startangle=140)
plt.title("Pie Chart of Animal Count")
plt.savefig("ZooData_PieChart.png")
