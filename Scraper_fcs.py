import pandas as pd
import validators 

# function to scrape just links from a given file
def scrape_links():
    df = pd.read_excel('2023_roster_links.xlsx', sheet_name="FCS")
    roster_links = df.iloc[:,2]
    return roster_links

# given all links iterate through the links and add each link to the same dataframe
def gather_data(links):
    # fitler out nan values from list
    links_filtered = links.dropna()
    # iterate through links and put each links data into the dataframe
    for index, link in links_filtered.iteritems():
        url_value = validators.url(link)
        # error getting every link to pull up as the right grid on a webpage
        if url_value==True:
            print(link)
            df = pd.read_html(link)
            print(df)
        else:
            print("Not a URL")

        

# main function 
def main():
    all_roster_links = scrape_links()
    final_data = gather_data(all_roster_links)
    print(final_data)

# execute main funciton
if __name__ == "__main__":
    main()