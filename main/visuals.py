import matplotlib.pyplot as plt

# Realistic Population Density Data
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
sant_kabir_nagar = [32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000]
fernandiz_wadi = [29000, 29500, 30000, 30500, 31000, 31500, 32000, 32500, 33000]
vihintgaon = [31000, 31500, 32000, 32500, 33000, 33500, 34000, 34500, 35000]
rajiv_nagar = [35000, 35500, 36000, 36500, 37000, 37500, 38000, 38500, 39000]
boys_town_school_area = [30000, 30500, 31000, 31500, 32000, 32500, 33000, 33500, 34000]

# Plot Population Density
plt.figure(figsize=(10, 6))
plt.bar([y - 0.4 for y in years], sant_kabir_nagar, width=0.2, label='Sant Kabir Nagar')
plt.bar([y - 0.2 for y in years], fernandiz_wadi, width=0.2, label='Fernandiz Wadi')
plt.bar([y for y in years], vihintgaon, width=0.2, label='Vihintgaon')
plt.bar([y + 0.2 for y in years], rajiv_nagar, width=0.2, label='Rajiv Nagar')
plt.bar([y + 0.4 for y in years], boys_town_school_area, width=0.2, label='Boys Town School Area')
plt.xlabel('Year')
plt.ylabel('Population Density (people/sq km)')
plt.title('Population Density Over Time')
plt.legend()
plt.grid(True)
plt.show()

# Realistic Economic Status Data
sant_kabir_nagar_income = [6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600]
fernandiz_wadi_income = [5500, 5700, 5900, 6100, 6300, 6500, 6700, 6900, 7100]
vihintgaon_income = [5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400]
rajiv_nagar_income = [5900, 6100, 6300, 6500, 6700, 6900, 7100, 7300, 7500]
boys_town_school_area_income = [5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200]

# Plot Economic Status
plt.figure(figsize=(10, 6))
plt.bar([y - 0.4 for y in years], sant_kabir_nagar_income, width=0.2, label='Sant Kabir Nagar')
plt.bar([y - 0.2 for y in years], fernandiz_wadi_income, width=0.2, label='Fernandiz Wadi')
plt.bar([y for y in years], vihintgaon_income, width=0.2, label='Vihintgaon')
plt.bar([y + 0.2 for y in years], rajiv_nagar_income, width=0.2, label='Rajiv Nagar')
plt.bar([y + 0.4 for y in years], boys_town_school_area_income, width=0.2, label='Boys Town School Area')
plt.xlabel('Year')
plt.ylabel('Average Income (INR/month)')
plt.title('Economic Status Over Time')
plt.legend()
plt.grid(True)
plt.show()
