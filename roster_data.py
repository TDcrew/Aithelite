import requests 
import csv
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://acusports.com/sports/football/roster"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

raw_data = soup.find_all("li", class_="sidearm-roster-player")

# write to a csv file 
with open('player_info.csv', "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Position', 'Height', 'Weight', 'Number', 'Year'])
    # for loop to iterate through list of players
    for indv_data in raw_data:
        # scrape player information
        if indv_data.find('img', alt=True) != None:
            player_number = indv_data.find("span", class_="sidearm-roster-player-jersey-number")
            player_name = indv_data.find("img", alt=True)
            player_pos = indv_data.find("span", class_="text-bold")
            player_height = indv_data.find("span", class_="sidearm-roster-player-height")
            player_weight = indv_data.find("span", class_="sidearm-roster-player-weight")
            player_year = indv_data.find("span", class_="sidearm-roster-player-academic-year hide-on-large")

            # put player info into a list
            individual_info = []
            individual_info.append(player_name['alt'])
            individual_info.append(player_pos.text.strip()[-2:])
            individual_info.append(player_height.text)
            individual_info.append(player_weight.text)
            individual_info.append(player_number.text.strip())
            individual_info.append(player_year.text)
            writer.writerow(individual_info)
    
print("Data added to csv file")