import requests 
from bs4 import BeautifulSoup
import pandas as pd
import csv
import validators 
from urllib.parse import urlparse


# function to scrape just links from a given file
def scrape_links():
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name="FCS")
    roster_links = df.iloc[:,2]
    return roster_links

all_links = scrape_links().tolist()

invalid_links = []
no_image_links = []

with open('player_images.csv', "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Image Source'])

    for i in range(len(all_links)):
        URL = all_links[i]
        page = requests.get(URL)
        valid_url = False
        valid_url = validators.url(URL)

        parsed_url = urlparse(URL)
        base = parsed_url.scheme + "://" + parsed_url.netloc
        print('Link: ', all_links[i])

        soup = BeautifulSoup(page.text, "html.parser")

        images = soup.find_all('img')

        if len(images) < 50:
            no_image_links.append(all_links[i])

        print(no_image_links)

        for image in images:
            name_src = []
            
            # and ((image.get('alt') != None) or (image.get('alt') != "")) 
            
            if image.get('src') != None:
                try: 
                    if image.get('src')[0] == '/':
                        name_src.append(image.get('alt'))
                        name_src.append(base + image.get('src'))
                    else:
                        name_src.append(image.get('alt'))
                        name_src.append(image.get('src'))
                except:
                    invalid_links.append(URL)

            
            if name_src != []:
                if name_src[0] != "" and name_src[0] != '' and name_src[0] != None:
                    writer.writerow(name_src)

