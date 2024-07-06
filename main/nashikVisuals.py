import matplotlib.pyplot as plt

# New data for slum population and density in specific areas of Nashik
areas = [
    "Fernandiz Wadi Jai Bhavani Road", "Sant Kabir Nagar near Bhonsala Campus", 
    "Vihintgaon Devlali", "Rajiv Nagar Nashik", "Boys Town School and Junior College Nashik"
]
area_population = [20000, 18000, 25000, 22000, 16000]
area_density = [18000, 15000, 20000, 17000, 14000]

# District-level data for comparison
districts = ["Surgana", "Kalwan", "Trimbakeshwar"]
population = [39491, 38129, 28385]
density = [1600, 1800, 1500]

# Create a figure and axis for areas in Nashik
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot slum population in specific areas of Nashik
color = 'tab:blue'
ax1.set_xlabel('Areas in Nashik')
ax1.set_ylabel('Slum Population', color=color)
ax1.bar(areas, area_population, color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(areas, rotation=45, ha='right')

# Create another y-axis to plot population density in specific areas of Nashik
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Population Density (per sq. km)', color=color)
ax2.plot(areas, area_density, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Add titles and labels
plt.title('Slum Population and Population Density in Specific Areas of Nashik')
fig.tight_layout()

# Display the plot for specific areas in Nashik
plt.show()

# Create a figure and axis for district-level data
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot slum population in districts of Nashik
color = 'tab:blue'
ax1.set_xlabel('Districts in Nashik')
ax1.set_ylabel('Slum Population', color=color)
ax1.bar(districts, population, color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(districts, rotation=45, ha='right')

# Create another y-axis to plot population density in districts of Nashik
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Population Density (per sq. km)', color=color)
ax2.plot(districts, density, color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Add titles and labels
plt.title('Slum Population and Population Density in Districts of Nashik')
fig.tight_layout()

# Display the plot for districts in Nashik
plt.show()
