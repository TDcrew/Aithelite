import requests 
from bs4 import BeautifulSoup
import pandas as pd
import csv
import validators 
from urllib.parse import urlparse
from selenium import webdriver


# function to scrape just links from a given file
def scrape_links():
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name="FCS")
    roster_links = df.iloc[:,2]
    return roster_links

all_links = scrape_links().tolist()

school_name = pd.read_excel('2023_roster_links.xlsx', sheet_name="FCS").iloc[:,1]

invalid_links = []
no_image_links = []

with open('player_images.csv', "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'School', 'Image Source'])

    for i in range(len(all_links)):
        URL = all_links[i]
        page = requests.get(URL)
        valid_url = False
        valid_url = validators.url(URL)

        parsed_url = urlparse(URL)
        base = parsed_url.scheme + "://" + parsed_url.netloc
        print('Link: ', all_links[i])

        driver = webdriver.Chrome()
        driver.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")

        table = soup.find('tr')

        if table:
            html = driver.page_source

            soup = BeautifulSoup(html, "html.parser")

            table = str(soup.find_all('table')[0])

            soup = BeautifulSoup(table, 'html.parser')

            df = pd.read_html(table)[0]

            df.columns = df.columns.str.lower()
            
        if df.columns.str.contains('name').any():
            print('has name column')
            html = driver.page_source

            soup = BeautifulSoup(html, "html.parser")

            table = str(soup.find_all('table')[0])

            soup = BeautifulSoup(table, 'html.parser')
            
            df = pd.read_html(table, extract_links="body")[0]

            df.columns = df.columns.str.lower()

            names = df.loc[:, df.columns.str.contains('name')]

            names = names.values.tolist()

            print(names)

            if names != [[]]:

                for j in range(len(names)):
                    name_school_src = []
                    name_school_src.append(names[j][0][0])
                    name_school_src.append(school_name[i])
                    name_school_src.append(base + names[j][0][1])


                    print(name_school_src)
                    writer.writerow(name_school_src)

            driver.close()

        else:
            print('no table ')
            images = soup.find_all('img')

            if len(images) < 50:
                no_image_links.append(all_links[i])

    

            for image in images:
                name_school_src = []
                            
                if image.get('src') != None:
                    try: 
                        if image.get('src')[0] == '/':
                            name_school_src.append(image.get('alt'))
                            name_school_src.append(school_name[i])
                            name_school_src.append(base + image.get('src'))
                        else:
                            name_school_src.append(image.get('alt'))
                            name_school_src.append(school_name[i])
                            name_school_src.append(image.get('src'))
                    except:
                        invalid_links.append(URL)

                
                if name_school_src != []:
                    if name_school_src[0] != "" and name_school_src[0] != '' and name_school_src[0] != None:
                        writer.writerow(name_school_src)

