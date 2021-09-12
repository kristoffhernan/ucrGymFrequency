

from requests_html import HTMLSession

def get_page():
    # need header for HTTP requests, not always needed?
    HEADER = { 
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        }
    URL = "https://connect2concepts.com/connect2/?type=circle&key=593DB611-499B-418E-8082-7263A32860D5"

    session = HTMLSession()

    r = session.get(URL, headers = HEADER)
    return r

def get_text():
    r = get_page()
    # need to render because of java
    r.html.render()

    container = r.html.find('.panel-body')
    locations = container[0].find('.col-md-3')
    return locations

def gym_data():
    ls = []
    locations = get_text()
    indexes = [0,3,4]

    for i in range(0,32):
        location = locations[i].text
        location = location.replace('Last Count: ', '').replace('Updated: ', '').replace('(', '').replace(')', '').replace('%', '')
        location = list(location.split("\n"))

        if "Closed" not in location:
            ls.append(location)
        else:
            for index in indexes:
                location[index] = None
            ls.append(location)
    return ls
