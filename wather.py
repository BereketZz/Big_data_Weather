# Importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Introduction
'''
This dataset originates from the Arbaminch University Metrology Department
and was acquired during my internship at Arbaminch University.
It encompasses a comprehensive collection of weather measurements,
including temperature, humidity, wind speed, solar radiation, and soil temperature.
The data provides valuable insights into the local climatic conditions,
allowing for exploratory data analysis and the exploration of relationships
between various meteorological parameters.The data spans from 2016 to June 2023, capturing a comprehensive timeline of
meteorological observations during this period. 
'''

row_data= pd.read_csv("weather.csv")
row_data.head()

#Questions
'''
What is the impact of solar radiation and humidity on soil temperature ?
  - How does solar radiation influence soil temperature, and are there discernible patterns or correlations?
  - Similarly, what is the relationship between humidity levels and soil temperature?
'''

#Data Wrangling
def preprocess_data(data):

    # Replace special characters with NaN
    data.replace("---", np.nan, inplace=True)

    # Fill missing values with backfill
    data = data.fillna(method="bfill")

    # Standardize column names
    data.columns = [col.lower().replace(" ", "_") for col in data.columns]

    return data
preprocessed_data = preprocess_data(row_data)
preprocessed_data.head()

Exploratory Data Analysis
'''
 In this phase, I leveraged the power of Matplotlib and Seaborn (sns) to visualize and analyze the dataset,
 unraveling intricate relationships among the three  meteorological variables. 
'''

# Extract relevant columns for analysis
selected_columns = [ 'out_hum','solar_rad.', 'soil_temp_1']
selected_data = preprocessed_data[selected_columns]

# Ensure 'solar_rad.','soil_temp_1','out_hum'  columns are in string format
selected_data['solar_rad.'] = selected_data['solar_rad.'].astype(str)
selected_data['soil_temp_1'] = selected_data['soil_temp_1'].astype(str)
selected_data['out_hum'] = selected_data['out_hum'].astype(str)

#Display  selected_data
selected_data.head()


# Visualize the relationship between soil temperature and humidity
sns.scatterplot(x="out_hum", y="soil_temp_1", data=selected_data)
plt.title("Soil Temperature vs. Humidity") 
plt.show()
# Visualize the relationship between soil temperature and solar radiation
plt.figure(figsize=(12, 6))
plt.scatter(selected_data['solar_rad.'], selected_data['soil_temp_1'], alpha=0.5, color='green')
plt.title("Relationship between Solar Radiation and Soil Temperature")
plt.xlabel("Solar Radiation")
plt.ylabel("Soil Temperature")
plt.show()

# Ensure 'solar_rad.' column is in float format
selected_data['solar_rad.'] = selected_data['solar_rad.'].astype(float)
plt.figure(figsize=(12, 8))
scatter = plt.scatter(selected_data['out_hum'], selected_data['soil_temp_1'], c=selected_data['solar_rad.'], cmap='viridis', alpha=0.5)

# Add colorbar
plt.colorbar(scatter, label='Solar Radiation')

# Set labels and title
plt.xlabel('Humidity')
plt.ylabel('Soil Temperature')
plt.title('Scatter Plot of Humidity and Soil Temperature with Solar Radiation Color-coded')

plt.show()

selected_data['out_hum'] = selected_data['out_hum'].astype(float)
selected_data['soil_temp_1'] = selected_data['soil_temp_1'].astype(float)

# Extract relevant columns
solar_rad = selected_data['solar_rad.']
out_hum = selected_data['out_hum']
soil_temp = selected_data['soil_temp_1']

# Calculate mean using NumPy
mean_solar_rad = np.mean(solar_rad)
mean_out_hum = np.mean(out_hum)
mean_soil_temp = np.mean(soil_temp)

# Calculate range 
range_solar_rad = solar_rad.max() - solar_rad.min()
range_out_hum = out_hum.max() - out_hum.min()
range_soil_temp = soil_temp.max() - soil_temp.min()

# Calculate correlation using Pandas
correlation_solar_soil = solar_rad.corr(soil_temp)
correlation_out_hum_soil = out_hum.corr(soil_temp)

# Print results
print(f"Range Solar Radiation: {range_solar_rad}")
print(f"Range Outdoor Humidity: {range_out_hum}")
print(f"Range Soil Temperature: {range_soil_temp}")

print(f"Mean Solar Radiation: {mean_solar_rad}")
print(f"Mean Outdoor Humidity: {mean_out_hum}")
print(f"Mean Soil Temperature: {mean_soil_temp}\n")

print(f"Correlation between Solar Radiation and Soil Temperature: {correlation_solar_soil}")
print(f"Correlation between Outdoor Humidity and Soil Temperature: {correlation_out_hum_soil}")

#Conclusion 

'''
# Analysis Reflection:

 # Reflection on Data Exploration:
 The data exploration involved thorough preprocessing, where I standardized column names, handled missing values,
 and ensured the data's consistency. Visualization played a crucial role in understanding the patterns within the dataset.

 # Summary of Main Findings:
 The scatter plot, titled "Relationship between Solar Radiation and Soil Temperature," vividly illustrates
 a positive relationship between solar radiation and soil temperature. As solar radiation levels increase,
 there is a tendency for soil temperature to rise as well. Clusters of data points are denser at lower levels
 of solar radiation, highlighting more occurrences of conditions with lower solar radiation and higher soil temperatures.
 Correlation between Outdoor Humidity and Soil Temperature: -0.3536
 Here, a moderate negative correlation is observed between outdoor humidity and soil temperature.
 The negative sign suggests an inverse relationship, implying that as humidity decreases,
 soil temperature tends to increase, and vice versa.

 # Identification of Additional Research Areas:
 My analysis identifies potential areas for further investigation. Specifically, the data exhibits gaps in the middle
 range of solar radiation and soil temperature, suggesting conditions that were either not measured or do not occur frequently.
 Additional research in these regions could provide valuable insights into the underlying factors influencing soil temperature.

 #Limitation Explanation:
 It is essential to acknowledge a limitation in my analysis. The data might be subject to limitations,
 such as gaps in measurements or the influence of unexplored variables. Understanding these limitations
 is crucial for interpreting the findings accurately.

 #Avoiding Causation Based Solely on Correlation:
 While I observe a positive correlation between solar radiation and soil temperature, it is important to emphasize
 that correlation does not imply causation. Other variables, not considered in this analysis, may contribute to the observed patterns.
 
'''
