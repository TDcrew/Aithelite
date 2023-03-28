import pandas as pd
import os


# function to concat all school rosters data
def concat_school_rosters():
    fbs_file_path = r"C:\Users\stdav\Documents\AIthelite\FBS_files"
    fcs_file_path = r"C:\Users\stdav\Documents\AIthelite\FCS_files"
    fbs_list = os.listdir(fbs_file_path)
    fcs_list = os.listdir(fcs_file_path)

    df_fbs = pd.DataFrame()
    #append all FBS files together
    for file in fbs_list:
        file_name = str(fbs_file_path + "\\" + file)   
        df_temp_fbs = pd.read_csv(file_name)
        df_fbs = df_fbs.append(df_temp_fbs, ignore_index=True)
    df_fbs.dropna()
    df_fbs.to_csv("FBS_data_all.csv")

    df_fcs = pd.DataFrame()
    #append all FCS files together
    for file in fcs_list:
        file_name = str(fcs_file_path + "\\" + file)   
        df_temp_fcs = pd.read_csv(file_name)
        df_fcs = df_fcs.append(df_temp_fcs, ignore_index=True)
    df_fcs.dropna()
    df_fcs.to_csv("FCS_data_all.csv")

    print("Finished concating rosters together")

# main function 
def main():
    concat_school_rosters()
    print("School rosters have been merged into one file")

# execute main funciton
if __name__ == "__main__":
    main()