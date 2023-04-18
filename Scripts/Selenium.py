# file using beautifulsoup to gather data from a single website 
import requests 
import csv
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import os

# test to see if links can be scraped using BeautifulSoup
def BS_Scraper():
    rosters = ['https://gocards.com/sports/football/roster', 'https://godeacs.com/sports/football/roster?view=2', 'https://owlsports.com/sports/football/roster', 'https://tulsahurricane.com/sports/football/roster', 'https://meangreensports.com/sports/football/roster/2022-23', 'https://uabsports.com/sports/football/roster', 'https://baylorbears.com/sports/football/roster', 'https://cyclones.com/sports/football/roster', 'https://soonersports.com/sports/football/roster', 'https://iuhoosiers.com/sports/football/roster', 'https://gophersports.com/sports/football/roster', 'https://wkusports.com/sports/football/roster', 'https://www.liberty.edu/flames/football/roster/', 'https://umassathletics.com/sports/football/roster', 'https://gozips.com/sports/football/roster', 'https://goairforcefalcons.com/sports/football/roster', 'https://broncosports.com/sports/football/roster', 'https://csurams.com/sports/football/roster', 'https://gobulldogs.com/sports/football/roster', 'https://utahstateaggies.com/sports/football/roster', 'https://gowyo.com/sports/football/roster', 'https://osubeavers.com/sports/football/roster', 'https://georgiadogs.com/sports/football/roster', 'https://utsports.com/sports/football/roster/2022', 'https://ragincajuns.com/sports/football/roster/2022', 'https://herdzone.com/sports/football/roster']
    #url = ''https://gocards.com/sports/football/roster', https://cuse.com/sports/football/roster/2022?view=2', 'https://hokiesports.com/sports/football/roster'
    index = 0
    for url in rosters:   
        create_csv = True 
        try:
            # Step 1: Create a session and load the page
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options)
            #driver = webdriver.Chrome()
            driver.get(url)

            # Wait for the page to fully load
            driver.implicitly_wait(10)

            # Step 2: Parse HTML code and grab tables with Beautiful Soup
            soup = BeautifulSoup(driver.page_source, 'lxml')
            tables = soup.find_all('table')
            # Step 3: Read tables with Pandas read_html()
            df = pd.read_html(str(tables))
            df_new = df[0]
            print(df_new)
            #print(df[0])
            driver.close()
            print(url + " this link was scrapable")
        except Exception:
            print(url + " is not scrapable")
            create_csv = False
        if create_csv:
            print(url + " is scrapable")
            url = url[5:10]
            path = str(index) + ".csv"
            df_new.to_csv(path)
        index+=1    

def main():
    BS_Scraper()
    print("Tried beautifulsoup on files that could not be scarped by pandas.")

if __name__ == "__main__":
    main()