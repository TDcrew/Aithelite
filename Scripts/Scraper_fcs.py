import pandas as pd
import validators 

# function to scrape just links from a given file
def scrape_links():
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name="FCS")
    roster_links = df.iloc[:,2]
    return roster_links

# given all links iterate through the links and add each link to the same dataframe
def gather_data(links):
    links_not_scrapable = []
    count = 0
    # fitler out nan values from list
    links_filtered = links.dropna()
    # iterate through links and put each links data into the dataframe
    for index, link in links_filtered.iteritems():
        url_value = validators.url(link)
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
            #issue in code with df.to_csv() function not working currently
            if create_csv:
                link_name = str(link[9:17] + '.csv')
                print(link_name)
                df.to_csv(link_name)
        else:
            print("Not a URL")
    print("A total of ", count, " links not scrapable currently.")
    print("Here is a list of links that could not be scraped", links_not_scrapable)

        

# main function 
def main():
    all_roster_links = scrape_links()
    final_data = gather_data(all_roster_links)
    print(final_data)

# execute main funciton
if __name__ == "__main__":
    main()