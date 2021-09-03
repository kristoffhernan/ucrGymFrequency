
#from datetime import date
from requests_html import HTMLSession
import csv

with open('ucrGymScraperData.csv', 'a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    #csv_writer.writerow(['Capacity(%)', 'Area', 'O/C', 'Count', 'LastUpdated'])

    headers = { 
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    }

    URL = "https://connect2concepts.com/connect2/?type=circle&key=593DB611-499B-418E-8082-7263A32860D5"

    session = HTMLSession()

    r = session.get(URL, headers = headers)

    r.html.render()

    container = r.html.find('.panel-body')

    locations = container[0].find('.col-md-3')

    ls = []

    for i in range(0,15):
        location = locations[i].text
        location = location.replace('Last Count: ', '').replace('Updated: ', '').replace('(', '').replace(')', '').replace('%', '')
        
        if "NA" not in location:
            location = list(location.split("\n"))
            ls.append(location)

    for row in range(0,len(ls)):
        csv_writer.writerow([ls[row][0], ls[row][1], ls[row][2], ls[row][3], ls[row][4]])

    #csv_writer.writerow([])

    csv_file.close()

    #print("Writing Complete")