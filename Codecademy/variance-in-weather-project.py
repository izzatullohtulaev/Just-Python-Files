import pandas as pd
import numpy as np

london_data = pd.read_csv('Datasets/london_weather.csv')
# print(london_data.head())
# print(london_data.dtypes)
# print(london_data.describe())

# print(london_data['Time'].count())

# print(london_data.head())

temp = london_data['TemperatureC']
# average_temp = np.mean(temp)
# print(average_temp)

temperature_var = np.var(temp)
# print(temperature_var)

temperature_standard_deviation = np.std(temp)
# print(temperature_standard_deviation)

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]

july = london_data.loc[london_data["month"] == 7]['TemperatureC']
# print(np.mean(june))
# print(np.mean(july))

# print(np.std(june))
# print(np.std(july))
#
# for i in range(1, 13):
#     month = london_data.loc[london_data["month"] == i]["TemperatureC"]
#     print("Average temperature for month "+str(i)+": "+str(format(np.mean(month), '.1f')))
#     print("\tStandard deviation for month "+str(i)+": "+str(format(np.std(month), '.1f'))+'\n')
#

# mean_humidities = []
# for i in range(1, 13):
#     month = london_data.loc[london_data['month'] == i]['Humidity']
#     print("Humidity for month "+str(i)+' is '+str(format(np.mean(month), '.1f')))
#     mean_humidities.append(np.mean(month))
# print(mean_humidities.index(max(mean_humidities))+1)

# mean_temps = []
# for i in range(0, 24):
#     hour = london_data.loc[london_data['hour'] == i]['TemperatureC']
#     mean_temps.append(np.mean(hour))
#     print(f"Mean temp for hour {i} is {mean_temps[i]}")
# print(mean_temps.index(max(mean_temps)))



