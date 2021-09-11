from weather.weatherAPI import return_weather_results
from gym.ucrGymScraper import clean_data
import csv

weather_data = return_weather_results()

with open ('weather/weatherData.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    #csv_writer.writerow(['Temperature', 'Humidity', 'Pressure', 'Weather Report'])

    csv_writer.writerow([weather_data['temperature'], weather_data['humidity'], weather_data['pressure'], weather_data['weather_report']])

    file.close()

gym_data = clean_data()


with open('gym/ucrGymScraperData.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    #csv_writer.writerow(['Capacity(%)', 'Area', 'O/C', 'Count'])

    csv_writer.writerows(gym_data)
    
    csv_file.close()
