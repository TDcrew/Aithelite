import pandas as pd
import validators 
from selenium import webdriver
import os
from bs4 import BeautifulSoup
from tkinter.filedialog import askopenfilename

# function to scrape just links from a excel file
def scrape_links(filename):
    df_fbs = pd.read_excel(filename, sheet_name="FBS")
    fbs_roster_links = df_fbs.iloc[:,2]
    df_fcs = pd.read_excel(filename, sheet_name="FCS")
    fcs_roster_links = df_fcs.iloc[:,2]
    return fcs_roster_links, fbs_roster_links

#function to scrape team names from excel file
def scrape_team_names(filename):
    df_fbs = pd.read_excel(filename, sheet_name="FBS")
    fbs_roster_names = df_fbs.iloc[:,1]
    df_fcs = pd.read_excel(filename, sheet_name="FCS")
    fcs_roster_links = df_fcs.iloc[:,1]
    return fbs_roster_names, fcs_roster_links

# function to remove blank spaces from string
def remove(string):
    return string.replace(" ", "")

# given all links iterate through the links and add each link to the same dataframe
def gather_data(links, names, fbs_fcs):
    # set directory path name for outputs
    dir_path = './' + fbs_fcs + '_files'
    # check to make sure directory is made and if not create the directory
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    # create a list to keep track of links that could not be scraped by pandas or selenium currently
    links_not_scrapable = []
    # count the amount of links not scrapable by pandas or selenium currently
    count = 0
    # fitler out nan values from list
    links_filtered = links.dropna()
    # iterate through links and put each links data into the dataframe
    for index, link in links_filtered.iteritems():
        # check to make sure the given field is a url
        url_value = validators.url(link)
        # if the given field is a url then try to get data from said url
        if url_value==True:
            # by default we need to not create a csv or try selenium before using pandas
            create_csv = False
            try_selenium = False
            # catch all links that are scrapable by the pd.read_html() function
            try:
                #put data pulled from all tables in the html with pandas into one dataframe
                df = pd.concat(pd.read_html(link))
                # insert the school name into the dataframe
                df.insert(8, "Current School Name", names[index], allow_duplicates=True)
                # setting create_csv equal to True lets us know that pandas worked and we want to save the dataframe to a csv later in the file
                create_csv = True
            # if a link is not scrapable with pandas then a error message is thrown to the user and will try selenium to scrap web data
            except Exception: 
                print("THIS LINK IS NOT SCRAPABLE WITH PANDAS TRYING SELENIUM", link)
                try_selenium = True
            # if you could not grab tables from website using pandas alone, try using selenium
            if try_selenium:
                try:
                    # create a session and load the page and set webdriver to not display any messages in the console
                    options = webdriver.ChromeOptions()
                    options.add_experimental_option('excludeSwitches', ['enable-logging'])
                    driver = webdriver.Chrome(options=options)
                    driver.get(link)
                    # wait for the page to fully load
                    driver.implicitly_wait(5)
                    # parse HTML code and grab tables with BeautifulSoup 
                    soup = BeautifulSoup(driver.page_source, 'lxml')
                    # find all tables in html code with BeautifulSoup
                    tables = soup.find_all('table')
                    # read tables with Pandas read_html()
                    df = pd.read_html(str(tables))
                    # grab first table in pandas dataframe to work with player data
                    df = df[0]
                    # insert school name into the dataframe
                    df.insert(8, "Current School Name", names[index], allow_duplicates=True)
                    # close webdriver
                    driver.close()
                    print(link, "this link was succesfully scraped with selenium")
                    # if succesfully scraped then set create_csv to True, so a csv can be created for the dataframe
                    create_csv = True
                except Exception:
                    print("THIS LINK IS NOT SCRAPABLE WITH SELENIUM ", link)
                    # append the link to a list due to it not being scrapable with selenium or pandas
                    links_not_scrapable.append(link)
                    # increase the count of links by one for the current link not be scrapable by selenium or pandas 
                    count+=1
                    create_csv = False
            # if the csv was able to be read then we put the dataframe into a csv
            if create_csv:
                # grab the team name from the team names that were passed into the function 
                team_name = remove(names[index])
                # make a link name by appending .csv to the end of the team name
                link_name = str(team_name + '.csv')
                #add team to its own csv if scrapable by pandas or selenium
                path =  os.path.join(dir_path, link_name)
                df.to_csv(path)
                # let user know what the file name is of current team
                print(team_name + " was added to a csv file")
        # if not a url then let the user know the field was not a url
        else:
            print("Not a URL")
    print("A total of ", count, " links not scrapable currently.")
    print("Here is a list of links that could not be scraped for " + fbs_fcs + " " + links_not_scrapable)

# main function 
def main():
    #make user select the excel file with team links in it
    print("Select excel file with team links:")
    filename = askopenfilename()
    #execute functions to scrape data from links in file 
    roster_links = scrape_links(filename)
    roster_names = scrape_team_names(filename)
    #send fcs and fbs data to gather all the data from the links using gather_data() function
    fcs_data = gather_data(roster_links[0], roster_names[1], 'FCS')
    fbs_data = gather_data(roster_links[1], roster_names[0], 'FBS')

# execute main funciton
if __name__ == "__main__":
    main()