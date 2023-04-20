import pandas as pd
import numpy as np

#function to return a more clear python panda DataFrame of a given dataframe function needs to be unique for each FCS and FBS 
#due to column names being different
def fbs_roster_cleaner():
        # read raw data from file to use dataframe to grab specifc data
        data = pd.read_csv("FBS_raw_data.csv")
        #grab all position for players
        df_pos = data[["Pos","Pos.", "Position", "POS", "POSITION"]]
        df_pos = df_pos[df_pos.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab all names of players and coaches
        df_name = data[["Name","Full Name", "NAME"]]
        df_name = df_name[df_name.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab all heights of players
        df_height = data[["Ht.", "Height", "HT", "HT.", "Ht"]]
        df_height = df_height[df_height.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab all weights of players
        df_weight = data[["Wt.", "WT", "WT.", "Weight", "Wt"]]
        df_weight = df_weight[df_weight.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab year of player
        df_year = data[["Academic Year", "Yr.","Eligibility", "Year", "Cl.", "Years/Eligibility", "Years", "YEAR", "Class", "Cl./Exp.", "Exp.", "Experience", "Cl-Exp"]]
        df_year = df_year[df_year.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab each player number
        df_number = data[["Number", "#", "No.", "NO"]]
        df_number = df_number[df_number.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab player current school
        df_school = data[["Current School Name"]]
        df_school = df_school[df_school.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab player hometown and/or highschool
        df_home_highschool = data[["Hometown / High School", "Hometown", "Hometown / Prev School", "HOMETOWN", "Hometown / Previous School", "Hometown/High School", "Hometown (Prev School)", "Hometown/Previous School", "High School", "LAST SCHOOL", "Hometown / High School ( Previous School)", "High School / Previous School", "High School / Previous Schools", "Hometown / High school", "Hometown / High School (Previous School)", "Hometown/High School/Previous School"]]
        df_home_highschool = df_home_highschool[df_home_highschool.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab player academic major
        df_major = data[["Major", "Academic Major"]]
        df_major = df_major[df_major.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)

        #concat all the individual dataframes together into one dataframe
        df_player_test = pd.concat([df_name, df_pos, df_weight, df_height, df_year, df_number, df_school, df_home_highschool, df_major], axis=1)
        
        #name each column in the dataframe
        column_names = {df_player_test.columns[0]: 'Name', df_player_test.columns[1]: 'Position', df_player_test.columns[2]: 'Weight', df_player_test.columns[3]: 'Height', df_player_test.columns[4]: "Year", df_player_test.columns[5]: "Number", df_player_test.columns[6]: "Current School", df_player_test.columns[7]: "Hometown/High School", df_player_test.columns[8]: "Academic Major"}
        df_player_test = df_player_test.rename(columns=column_names)

        #pull coaches from dataframe, so only players are inside of the new dataframe
        df_player_test['Weight'].replace('', np.nan, inplace=True)
        df_player_test.dropna(subset=['Weight'], inplace=True)

        #code to send dataframe to the csv file
        df_player_test.to_csv("FBS_player_data.csv")
        print("FBS raw data has been cleaned and put into FBS_player_data.csv.")

#function to return a scrubbed python panda DataFrame of a given dataframe of FCS teams
def fcs_roster_cleaner():
        # read raw data from file to use dataframe to grab specifc data
        data = pd.read_csv("FCS_raw_data.csv")
        #grab all position for players
        df_pos = data[["Pos","Pos.", "Position", "POS", "POS."]]
        df_pos = df_pos[df_pos.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab all names of players and coaches
        df_name = data[["Name","Full Name", "NAME", "Name.1", "FULL NAME"]]
        df_name = df_name[df_name.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab all heights of players
        df_height = data[["Ht.", "Height", "HT", "HT."]]
        df_height = df_height[df_height.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab all weights of players
        df_weight = data[["Wt.", "WT", "WT.", "Weight"]]
        df_weight = df_weight[df_weight.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab year of player
        df_year = data[["Academic Year", "Yr.","Eligibility", "Year", "Cl.", "Yr.-Exp.", "Class", "CL."]]
        df_year = df_year[df_year.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab each player number
        df_number = data[["Number", "#", "No."]]
        df_number = df_number[df_number.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab player current school
        df_school = data[["Current School Name"]]
        df_school = df_school[df_school.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab player hometown and/or highschool
        df_home_highschool = data[["Hometown", "Hometown/Previous School", "Hometown (Prev School)", "Hometown / High School", "Hometown/High School", "Hometown(Prev School)", "Hometown / Last School", "Hometown / High School / Prep (Previous College)", "HOMETOWN", "Hometown / High School (Last School)", "High School", "HIGH SCHOOL", "High School / Prev. School", "HIgh School", "High School (Prev. School)"]]
        df_home_highschool = df_home_highschool[df_home_highschool.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
        #grab player academic major
        df_major = data[["Major", "MAJOR"]]
        df_major = df_major[df_major.columns[0:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)

        #concat all the individual dataframes together into one dataframe
        df_player_test = pd.concat([df_name, df_pos, df_weight, df_height, df_year, df_number, df_school, df_home_highschool, df_major], axis=1)

        #name each column in the dataframe
        column_names = {df_player_test.columns[0]: 'Name', df_player_test.columns[1]: 'Position', df_player_test.columns[2]: 'Weight', df_player_test.columns[3]: 'Height', df_player_test.columns[4]: "Year", df_player_test.columns[5]: "Number", df_player_test.columns[6]: "Current School", df_player_test.columns[7]: "Hometown/High School", df_player_test.columns[8]: "Academic Major"}
        df_player_test = df_player_test.rename(columns=column_names)

        #pull coaches from dataframe, so only players are inside of the new dataframe
        df_player_test['Weight'].replace('', np.nan, inplace=True)
        df_player_test.dropna(subset=['Weight'], inplace=True)
        
        #put fcs cleaned data into a csv
        df_player_test.to_csv("FCS_player_data.csv")
        print("FCS raw data has been cleaned and put into FCS_player_data.csv.")

#define main function
def main():
        fcs_roster_cleaner()
        fbs_roster_cleaner()
        print("FBS and FCS schools both succesfully cleaned.")

if __name__ == "__main__":
    main()