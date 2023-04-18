import pandas as pd

# function to pull coaches from a specific school csv
def coach_pull():
    print("done")

# function to concat all school rosters data
def concat_coach_pulls():
    # pull all raw data and get coaches from the dataframe and put them into there own dataframe for both fcs and fbs
    df_fcs = pd.read_csv("FCS_raw_data.csv")
    # pull just the Name, Title, and Current School Name from table
    newdf_fcs = df_fcs[['Name', 'Title', 'Current School Name']]
    # remove players from table
    newdf_fcs = newdf_fcs[newdf_fcs.Title.notnull()]
    # put coaches in new csv file
    newdf_fcs.to_csv("FCS_coaches.csv")
    
    # do the same steps above just for FBS schools now
    df_fbs = pd.read_csv("FBS_raw_data.csv")
    newdf_fbs = df_fbs[['Name', 'Title', 'Current School Name']]
    newdf_fbs = newdf_fbs[newdf_fbs.Title.notnull()]
    newdf_fbs.to_csv("FBS_coaches.csv")
    

# main function 
def main():
    concat_coach_pulls()
    print("Coaches are taken out of file and put into new csv")

# execute main funciton
if __name__ == "__main__":
    main()