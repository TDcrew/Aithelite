import pandas as pd
import validators 

# function to scrape just links from a excel file
def scrape_links():
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name="FBS")
    roster_links = df.iloc[:,2]
    return roster_links

#function to scrape team names from excel file
def scrape_team_names():
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name="FBS")
    roster_names = df.iloc[:,1]
    return roster_names

# function to remove blank spaces from string
def remove(string):
    return string.replace(" ", "")

# given all links iterate through the links and add each link to the same dataframe
def gather_data(links, names):
    links_not_scrapable = []
    count = 0
    # fitler out nan values from list
    links_filtered = links.dropna()
    # iterate through links and put each links data into the dataframe
    for index, link in links_filtered.iteritems():
        url_value = validators.url(link)
        print(index)
        if url_value==True:
            create_csv = False
            # catch all links that are not scrapable by the pd.read_html() fucntion
            try:
                df = pd.concat(pd.read_html(link))
                create_csv = True
            except Exception: 
                print("THIS LINK IS NOT SCRAPABLE", link)
                links_not_scrapable.append(link)
                count+=1
            # if the csv was able to be read then we put the dataframe into a csv
            if create_csv:
                team_name = remove(names[index])
                link_name = str(team_name + '.csv')
                df.to_csv(link_name)
        else:
            print("Not a URL")
    print("A total of ", count, " links not scrapable currently.")
    print("Here is a list of links that could not be scraped", links_not_scrapable)

# main function 
def main():
    all_roster_links = scrape_links()
    all_roster_names = scrape_team_names()
    final_data = gather_data(all_roster_links, all_roster_names)
    print(final_data)

# execute main funciton
if __name__ == "__main__":
    main()