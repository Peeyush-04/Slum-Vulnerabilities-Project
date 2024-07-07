import matplotlib.pyplot as plt

# New data for socio-economic status, health status, and household statistics for specific areas in Nashik and overall in Maharashtra slums

# Specific areas in Nashik
nashik_areas = [
    "Fernandiz Wadi Jai Bhavani Road", "Sant Kabir Nagar near Bhonsala Campus", 
    "Vihintgaon Devlali", "Rajiv Nagar Nashik", "Boys Town School and Junior College Nashik"
]
nashik_area_poverty_rate = [35, 34, 38, 37, 33]
nashik_area_monthly_income = [6200, 6000, 6300, 6100, 5900]
nashik_area_clean_water = [50, 45, 48, 46, 44]
nashik_area_infant_mortality = [42, 43, 44, 45, 41]
nashik_area_household_size = [5.1, 5.3, 5.4, 5.2, 5.0]
nashik_area_permanent_housing = [62, 61, 60, 63, 59]

# Maharashtra slums (overall for comparison)
maharashtra_poverty_rate = 38
maharashtra_monthly_income = 5800
maharashtra_clean_water = 50
maharashtra_infant_mortality = 52
maharashtra_household_size = 4.8
maharashtra_permanent_housing = 55

# Plot socio-economic status for specific areas in Nashik
categories = ["Poverty Rate (%)", "Average Monthly Income (INR)"]
fig, ax = plt.subplots(figsize=(14, 8))

for i, area in enumerate(nashik_areas):
    plt.bar([x + i*0.15 for x in range(len(categories))], 
            [nashik_area_poverty_rate[i], nashik_area_monthly_income[i]], width=0.15, label=area)

# Adding Maharashtra slums data for comparison
plt.bar([x + len(nashik_areas)*0.15 for x in range(len(categories))], 
        [maharashtra_poverty_rate, maharashtra_monthly_income], width=0.15, label='Maharashtra', color='grey')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Socio-Economic Status Comparison: Specific Areas in Nashik vs Maharashtra Slums')
plt.xticks([x + len(nashik_areas)*0.15/2 for x in range(len(categories))], categories)
plt.legend()
plt.tight_layout()
plt.show()

# Plot health status for specific areas in Nashik
categories = ["Access to Clean Water (%)", "Infant Mortality Rate (per 1000 live births)"]
fig, ax = plt.subplots(figsize=(14, 8))

for i, area in enumerate(nashik_areas):
    plt.bar([x + i*0.15 for x in range(len(categories))], 
            [nashik_area_clean_water[i], nashik_area_infant_mortality[i]], width=0.15, label=area)

# Adding Maharashtra slums data for comparison
plt.bar([x + len(nashik_areas)*0.15 for x in range(len(categories))], 
        [maharashtra_clean_water, maharashtra_infant_mortality], width=0.15, label='Maharashtra', color='grey')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Health Status Comparison: Specific Areas in Nashik vs Maharashtra Slums')
plt.xticks([x + len(nashik_areas)*0.15/2 for x in range(len(categories))], categories)
plt.legend()
plt.tight_layout()
plt.show()

# Plot household statistics for specific areas in Nashik
categories = ["Average Household Size", "Permanent Housing (%)"]
fig, ax = plt.subplots(figsize=(14, 8))

for i, area in enumerate(nashik_areas):
    plt.bar([x + i*0.15 for x in range(len(categories))], 
            [nashik_area_household_size[i], nashik_area_permanent_housing[i]], width=0.15, label=area)

# Adding Maharashtra slums data for comparison
plt.bar([x + len(nashik_areas)*0.15 for x in range(len(categories))], 
        [maharashtra_household_size, maharashtra_permanent_housing], width=0.15, label='Maharashtra', color='grey')

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Household Statistics Comparison: Specific Areas in Nashik vs Maharashtra Slums')
plt.xticks([x + len(nashik_areas)*0.15/2 for x in range(len(categories))], categories)
plt.legend()
plt.tight_layout()
plt.show()
