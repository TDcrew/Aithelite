import pandas as pd
import os

# function to concat all school rosters data
def concat_school_rosters():
    fbs_file_path = r"./FBS_files"
    fcs_file_path = r"./FCS_files"
    fbs_list = os.listdir(fbs_file_path)
    fcs_list = os.listdir(fcs_file_path)

    #append all FBS files together
    df_fbs = pd.DataFrame()
    for file in fbs_list:
        file_name = str(fbs_file_path + "\\" + file)   
        df_temp_fbs = pd.read_csv(file_name)
        df_fbs = pd.concat([df_fbs, df_temp_fbs])
    df_fbs.dropna()
    df_fbs.to_csv("FBS_raw_data.csv")

    #append all FCS files together
    df_fcs = pd.DataFrame()
    for file in fcs_list:
        file_name = str(fcs_file_path + "\\" + file)   
        df_temp_fcs = pd.read_csv(file_name)
        df_fcs = pd.concat([df_fcs, df_temp_fcs])
    df_fcs.dropna()
    df_fcs.to_csv("FCS_raw_data.csv")
    
    print("Finished concating rosters raw data together")



# main function 
def main():
    concat_school_rosters()
    print("School rosters for FCS and FBS have been merged into sepereate files.")

# execute main funciton
if __name__ == "__main__":
    main()