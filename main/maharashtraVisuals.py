import matplotlib.pyplot as plt

# Data for slum population and density in various districts of Maharashtra
districts = [
    "Mumbai", "Pune", "Thane", "Nagpur", "Nashik",
    "Aurangabad", "Solapur", "Amravati", "Kolhapur",
    "Nanded", "Jalgaon", "Latur", "Akola", "Chandrapur", "Sangli"
]
population = [
    5206473, 1046230, 1784000, 900000, 523125,
    484000, 372000, 310000, 287500,
    275000, 238000, 210000, 187000, 160000, 140000
]
density = [
    20482, 9362, 8470, 7625, 5400,
    6310, 4980, 3820, 3650,
    3500, 3300, 2980, 2750, 2500, 2200
]

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot slum population
color = 'tab:blue'
ax1.set_xlabel('Districts')
ax1.set_ylabel('Slum Population', color=color)
ax1.bar(districts, population, color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(districts, rotation=45, ha='right')

# Create another y-axis to plot population density
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Population Density (per sq. km)', color=color)
ax2.plot(districts, density, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Add titles and labels
plt.title('Slum Population and Population Density in Various Districts of Maharashtra')
fig.tight_layout()

# Display the plot
plt.show()
