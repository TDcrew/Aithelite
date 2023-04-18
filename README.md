# Aithelite
Repository to gather files that are used to develop Aithelite application. 
Scritps folder contains 4 scripts:
  Scraper.py is a script that searches a excel file and gets links from it for fcs or fbs schools to scrape roster data off a website.  
  Concat_rosters.py is a script that combines all files gathered from Scraper.py for fcs and fbs into one file each containing all roster data for each conference
  Roster_data.py is a file that uses beautifulsoup to scrap a single given web address
  Coach_pull.py is a file that uses scripts to grab all the coaches from the fbs or fcs all data links and removes them from the csv and puts them into their own csv
 Roster_Scruber.py is a file that aggregates data within FCS and FBS into there respective files.

Here is a list of links that could not be scraped ['https://cuse.com/sports/football/roster/2022?view=2', 'https://hokiesports.com/sports/football/roster', 'https://godeacs.com/sports/football/roster?view=2', 'https://tulsahurricane.com/sports/football/roster', 'https://meangreensports.com/sports/football/roster/2022-23', 'https://soonersports.com/sports/football/roster', 'https://wkusports.com/sports/football/roster', 'https://www.liberty.edu/flames/football/roster/', 'https://broncosports.com/sports/football/roster', 'https://csurams.com/sports/football/roster', 'https://gobulldogs.com/sports/football/roster', 'https://utahstateaggies.com/sports/football/roster', 'https://gowyo.com/sports/football/roster', 'https://ragincajuns.com/sports/football/roster/2022']

The list above is links that are not storing data in a table on their websites.  The websites listed above are storing there player data in list or unique classes for displaying on there webpages. 


ENVIORNMENT: 
Andaconda3 navigator
VS Code v1.16.2
Selenium v4.8.3
beautifulsoup4 v4.11.1
Validators v0.14.0
Pandas v1.4.4
