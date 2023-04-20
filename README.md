# Aithelite
Repository to gather files that are used to develop Aithelite application.

DEPENDENCIES: 
* Andaconda3 navigator
* VS Code v1.16.2
* Selenium v4.8.3
* beautifulsoup4 v4.11.1
* Validators v0.14.0
* Pandas v1.4.4
* Python v3.9.13


Installation: 
  Install the [Andaconda3 Navigator](https://www.anaconda.com/download/).
  Install needed dependencies with command line inside of andaconda3 navigator with the CMD.exe Prompt.
  * above installs can be done with commands: 
    * conda install -c conda-forge validators
    * conda install -c anaconda beautifulsoup4
    * conda install -c conda-forge selenium.
                                                

How to Use:
In the folder labeled /Scripts the user should run the main.py file.  This file will execute the needed scripts in order to scrape player data.  Starting with Scraper.py is a script that searches a excel file and gets links from it for fcs or fbs schools to scrape roster data off a website.  Then, Concat_rosters.py is a script that combines all files gathered from Scraper.py for fcs and fbs into one file each containing all roster data for each conference.  Followed by, Roster_data.py is a file that uses beautifulsoup to scrap a single given web address.  Then, Coach_pull.py is a file that uses scripts to grab all the coaches from the fbs or fcs all data links and removes them from the csv and puts them into their own csv.  Last script run is, Roster_Scruber.py is a file that aggregates data within FCS and FBS into there respective files.

Existing problems:
With both list of links below is links that are not storing data in a table on their websites that could be scraped with Pandas or Selenium.  The websites listed above are storing there player data in list or unique classes for displaying on there webpages. 

Here is a list of links that could not be scraped for FCS ['https://cuse.com/sports/football/roster/2022?view=2', 'https://hokiesports.com/sports/football/roster', 'https://godeacs.com/sports/football/roster?view=2', 'https://tulsahurricane.com/sports/football/roster', 'https://meangreensports.com/sports/football/roster/2022-23', 'https://soonersports.com/sports/football/roster', 'https://wkusports.com/sports/football/roster', 'https://www.liberty.edu/flames/football/roster/', 'https://broncosports.com/sports/football/roster', 'https://csurams.com/sports/football/roster', 'https://gobulldogs.com/sports/football/roster', 'https://utahstateaggies.com/sports/football/roster', 'https://gowyo.com/sports/football/roster', 'https://ragincajuns.com/sports/football/roster/2022']

Here is a list of links that could not be scraped for FBS ['https://cuse.com/sports/football/roster/2022?view=2', 'https://hokiesports.com/sports/football/roster', 'https://godeacs.com/sports/football/roster?view=2', 'https://tulsahurricane.com/sports/football/roster', 'https://meangreensports.com/sports/football/roster/2022-23', 'https://cyclones.com/sports/football/roster', 'https://soonersports.com/sports/football/roster', 'https://wkusports.com/sports/football/roster', 'https://www.liberty.edu/flames/football/roster/', 'https://broncosports.com/sports/football/roster', 'https://csurams.com/sports/football/roster', 'https://gobulldogs.com/sports/football/roster', 'https://utahstateaggies.com/sports/football/roster', 'https://gowyo.com/sports/football/roster', 'https://ragincajuns.com/sports/football/roster/2022', 'https://herdzone.com/sports/football/roster']


