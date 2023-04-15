import requests 
from bs4 import BeautifulSoup
import pandas as pd
import csv
from urllib.parse import urlparse
from selenium import webdriver


# Returns values in a column as a lifrom the provided roster links file
def return_column(sheet, column_index):
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name=sheet) # Select which sheet to grab links from
    roster_links = df.iloc[:,column_index]
    return roster_links.tolist()


# Scrape all links, separating output based on sheet name
def scrape_links(output_file, sheet):

    invalid_links = []

    # Get all links from roster links file
    all_links = return_column(sheet, 2)

    # Grabs list of school names from provided roster links file
    school_name = return_column(sheet, 1)

    with open(output_file, "w", newline='') as file:
        writer = csv.writer(file)

        # Set column names data will be written to
        writer.writerow(['Name', 'School', 'Image Source', 'Source Image?'])

        for i in range(len(all_links)):
            URL = all_links[i]
            page = requests.get(URL)

            # Get base of the current URL
            parsed_url = urlparse(URL)
            base = parsed_url.scheme + "://" + parsed_url.netloc

            print('Getting data from: ', all_links[i])

            # Setup selenium driver
            driver = webdriver.Chrome()
            driver.get(URL)

            soup = BeautifulSoup(page.text, "html.parser")

            table = soup.find('tr')

            try: 

                if table:

                    # Render page using selenium
                    html = driver.page_source

                    # Parse render using BeautifulSoup
                    soup = BeautifulSoup(html, "html.parser")

                    table = str(soup.find_all('table')[0])

                    df = pd.read_html(table)[0]

                    df.columns = df.columns.str.lower()
                

                if df.columns.str.contains('name').any():

                    # Render page using selenium
                    html = driver.page_source

                    # Parse render using BeautifulSoup
                    soup = BeautifulSoup(html, "html.parser")

                    table = str(soup.find_all('table')[0])

                    soup = BeautifulSoup(table, 'html.parser')
                    
                    df = pd.read_html(table, extract_links="body")[0]

                    df.columns = df.columns.str.lower()

                    # Get player names from table
                    names = df.loc[:, df.columns.str.contains('name')]

                    names = names.values.tolist()

                    # Some name columns show up empty, check to avoid them
                    if names != [[]]:
                        
                        # Write each row to output csv
                        for j in range(len(names)):
                            name_school_src = []
                            name_school_src.append(names[j][0][0])
                            name_school_src.append(school_name[i])
                            name_school_src.append(base + names[j][0][1])
                            name_school_src.append('no')

                            writer.writerow(name_school_src)

                    driver.close()

                else:

                    images = soup.find_all('img')
            

                    for image in images:
                        name_school_src = []
                                    
                        if image.get('src') != None:
                            try: 
                                if image.get('src')[0] == '/': # Indicates a relative path to image, must append to base link
                                    name_school_src.append(image.get('alt'))
                                    name_school_src.append(school_name[i])
                                    name_school_src.append(base + image.get('src'))
                                    name_school_src.append('yes')
                                else: 
                                    name_school_src.append(image.get('alt'))
                                    name_school_src.append(school_name[i])
                                    name_school_src.append(image.get('src'))
                                    name_school_src.append('yes')
                            except:
                                invalid_links.append(URL)

                        
                        if name_school_src != []:
                            if name_school_src[0] != "" and name_school_src[0] != '' and name_school_src[0] != None:
                                writer.writerow(name_school_src)
            except:
                invalid_links.append(URL)

        # Create output file for links that could not be scraped
        with open("invalid_links_" + sheet + ".csv", "w", newline="") as file:
            writer = csv.writer(file)
            for link in invalid_links:
                writer.writerow([link])



def main():

    sheet = input("Enter sheet name to scrape: ")

    scrape_links("player_images_" + sheet + ".csv", sheet)

    print('Done scraping!')

main()