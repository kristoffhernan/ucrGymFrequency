from weather.weatherAPI import return_weather_results
from gym.ucrGymScraper import gym_data
import csv
from datetime import datetime

date_time = datetime.now()

# writing weather data to csv
weather_data = return_weather_results()
with open ('weather/weatherData.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    #csv_writer.writerow(['Temperature', 'Humidity', 'Pressure', 'Weather Report'])

    csv_writer.writerow([weather_data['temperature'], weather_data['humidity'], weather_data['pressure'], weather_data['weather_report'], date_time])

    file.close()


gym_data = gym_data()
# adding date time to each nested list
[ls.append(date_time) for ls in gym_data]

# writing gym data to csv
with open('gym/ucrGymScraperData.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    #csv_writer.writerow(['Capacity(%)', 'Area', 'O/C', 'Count'])

    csv_writer.writerows(gym_data)
    
    csv_file.close()
