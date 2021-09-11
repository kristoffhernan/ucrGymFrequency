

from requests_html import HTMLSession

def get_page():
    HEADER = { 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }
    URL = "https://connect2concepts.com/connect2/?type=circle&key=593DB611-499B-418E-8082-7263A32860D5"

    session = HTMLSession()

    r = session.get(URL, headers = HEADER)
    return r

def get_text():
    r = get_page()
    r.html.render()

    container = r.html.find('.panel-body')
    locations = container[0].find('.col-md-3')
    return locations

def clean_data():
    ls = []
    locations = get_text()

    for i in range(0,15):
        location = locations[i].text
        location = location.replace('Last Count: ', '').replace('Updated: ', '').replace('(', '').replace(')', '').replace('%', '')
        
        if "NA" not in location:
            location = list(location.split("\n"))
            ls.append(location)

    return ls