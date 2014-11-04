'''
CLASS: Web Scraping in Python
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# read in a page and convert requests text into 'soup' object
def get_page(pageNumber):
    r = requests.get('http://www.gadventures.com/search/?page=' + str(pageNumber))
    soup = BeautifulSoup(r.content)

    # find the section of relevant links and then parse into iterable rows
    links_section = soup.find(name='div', attrs={'id':'results'})
    link_rows = links_section.find_all(attrs={'class':'trip-tile-footer'})      
    sub_links = ['http://gadventures.com' + row.a['href'] for row in link_rows]
    return sub_links
    
# go through the pages and get all the links    
category_links = []
countries_visited = []
for i in range(1,3):
    sub_links = get_page(i)
    for j in range(len(sub_links)):
        category_links.append(sub_links[j])
    
# function that takes a link and returns a dictionary of info about that page
def get_category_winners(category_link, country):
    category_link = category_link.replace('2014','2015')
    r = requests.get(category_link)
    soup = BeautifulSoup(r.text)

    driver = webdriver.PhantomJS()
    driver.get(category_link)
    dateScript = driver.find_element_by_id("departures-list")
    dateSoup= BeautifulSoup(driver.execute_script("return arguments[0].innerHTML", dateScript))
    driver.quit

    startDateScript = dateSoup.find_all(name='span', attrs={'class':'date start'})
    startDate = [];
    for date in startDateScript:
        startDate.append(date.text[5:])
    
    endDateScript = dateSoup.find_all(name='span', attrs={'class':'date end'})
    endDate = [];
    for date in endDateScript:
        endDate.append(date.text[5:])
        
    spaceScript = dateSoup.find_all(name='span', attrs={'class':'avail'})
    spaces = [];
    for date in spaceScript:
        spaces.append(date.text.strip())
    spaces.pop(0)
    
    return {"name":         soup.find(name='span', attrs={'itemprop':'name'}).string,
            "code":         soup.find(name='div', attrs={'title':'Trip Code'}).string,            
            "url":          category_link,
            "price":        float(soup.find(name='span', attrs={'class':'price'}).string),
            "duration":     float(soup.find(name='span', attrs={'class':'duration'}).string[:-6]),
            "from":         soup.find(name='span', attrs={'class':'start_finish'}).string.split(' to ')[0],
            "to":           soup.find(name='span', attrs={'class':'start_finish'}).string.split(' to ')[1],
            "style":        soup.find(name='div', attrs={'id':'trip-style'}).find('strong').string,
            "service":      soup.find(name='div', attrs={'id':'trip-service'}).find('strong').string,
            "type":         soup.find(name='div', attrs={'id':'trip-type'}).find('strong').string,
            "physical":     soup.find(name='div', attrs={'id':'trip-physical'}).find('strong').string,
            "start":        startDate,
            "end":          endDate,
            "spaces":       spaces
            }
