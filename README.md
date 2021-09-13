# UCR SRC Frequency

## Introduction
This project was initially started because I wanted to find the best, thus least busy hours to go to the gym. I was planning to simply scrape the hours and count of students, then graph to find when is least busy. However, like with most projects I do, I was inspired to add and do more after progressing. 


## [Gym](https://github.com/kristoffhernan/ucrGymFrequency/tree/main/gym)
Created is a python script that uses the requests_html library allowing me scrape websites with JavaScript imbedded. I originally planned to use the requests library but that only works with pure html. I then selected the text I wanted based on their class and cleaned it up a bit. From the [website](https://connect2concepts.com/connect2/?type=circle&key=593DB611-499B-418E-8082-7263A32860D5) I am grabbing: 

`Capacity(%)` - How full the area is

`Area` - The area of the gym (i.e. Treadmill, Swimming Pool)

`O/C` - If the area is closed or open

`Count` - The count of students in the area

`LastUpdated` - When the data was last updated. The gym is only open M-Th (12:00 PM - 8:00 PM) and F (12:00 PM - 6:30 PM)

`CurrentDateTime` - Current date and time when the data was scraped (*not* taken from the gym website)

**Issues**

There are a few issues I'm worried about for the data I'm scraping.
1. For my tests, the data is updated every 1-3 hours. This is problematic as I'd have hours of missing data.
	a. Because the data is updated every 1-3 hours, it would be difficult to tell how often someone stays in a certain area before leaving. 
2. I don't know how the students are tracked or if the count of students is tracked accurately.
3. Fall 2021-2022 gym hours are completely different than in the past before COVID. If the hours go back to the original hours where it's open from 6:00 AM - 12:00 AM and open on the weekends as well, I don't thing the models would work as well because I'd be extrapolating. 


## [Weather](https://github.com/kristoffhernan/ucrGymFrequency/tree/main/weather)
I created the weather script because I wanted to combine it with the gym frequency dataset to create some models to predict how the frequency would be like based on weather conditions. 

This program uses the requests library to get data from the [weather API](https://openweathermap.org/api) on openweathermap.org. To do this I had to use .get with my full url which contained the city, state, units and my API key. Because the weather API gave back the data in json format I also had to use the json library to read the data. Once read, I selected the variables:

`Temperature` - Temperature in Fahrenheit

`Humidity` - Humidity in %

`Pressure` - Pressure in hP

`Main` - The main weather forecast (i.e. clear)

`CurrentDateTime` - Current date and time when the data was requested (*not* taken from the gym website)


## [Writing the Data](https://github.com/kristoffhernan/ucrGymFrequency/blob/main/writeGymWeatherData.py)
I wrote a separate script to import the other python files and only use the necessary function to produce the data. I don't know if this is the correct way to do things, but it was cleaner to me. This files main function is to call the necessary functions and write the data to csv files. Because I only need to call this file once, it will make scheduling the scraper and API easier. It will also make it easier to write the date and time of requesting and writing the date be the exact same. I need the date and times to be the exact same because I will eventually join the datasets and I need a similar column to which I can join the them. 

To get the date and time, I will be using the datetime library. For now, the time is in  PDT, but it will change to PST on Nov 7th. I'm still unsure how to account for that change. 


## Conclusion
I am planning to run this script for either 2 months or the full Fall 2021-2022 quarter at UCR. The script will be ran every hour unless I see the website being update more often. Even though I will be graduating this Fall, I would still like to perform the analysis on the dataset.

Thank you for reading. Any questions or if you're hiring, my email is below. 

email: khern045@ucr.edu
