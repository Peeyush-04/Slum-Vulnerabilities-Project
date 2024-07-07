import matplotlib.pyplot as plt

# Data for socio-economic status
categories = ["Poverty Rate (%)", "Average Monthly Income (INR)"]
nashik_values = [32, 6500]
maharashtra_values = [38, 5800]

# Create bar chart for socio-economic status
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(categories))

bar1 = plt.bar(index, nashik_values, bar_width, label='Nashik', color='blue')
bar2 = plt.bar([i + bar_width for i in index], maharashtra_values, bar_width, label='Maharashtra', color='red')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Socio-Economic Status Comparison: Nashik vs Maharashtra Slums')
plt.xticks([i + bar_width / 2 for i in index], categories)
plt.legend()
plt.tight_layout()
plt.show()

# Data for health status
categories = ["Access to Clean Water (%)", "Infant Mortality Rate (per 1000 live births)"]
nashik_values = [45, 45]
maharashtra_values = [50, 52]

# Create bar chart for health status
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(categories))

bar1 = plt.bar(index, nashik_values, bar_width, label='Nashik', color='blue')
bar2 = plt.bar([i + bar_width for i in index], maharashtra_values, bar_width, label='Maharashtra', color='red')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Health Status Comparison: Nashik vs Maharashtra Slums')
plt.xticks([i + bar_width / 2 for i in index], categories)
plt.legend()
plt.tight_layout()
plt.show()

# Data for household statistics
categories = ["Average Household Size", "Permanent Housing (%)"]
nashik_values = [5.2, 60]
maharashtra_values = [4.8, 55]

# Create bar chart for household statistics
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
index = range(len(categories))

bar1 = plt.bar(index, nashik_values, bar_width, label='Nashik', color='blue')
bar2 = plt.bar([i + bar_width for i in index], maharashtra_values, bar_width, label='Maharashtra', color='red')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Household Statistics Comparison: Nashik vs Maharashtra Slums')
plt.xticks([i + bar_width / 2 for i in index], categories)
plt.legend()
plt.tight_layout()
plt.show()
