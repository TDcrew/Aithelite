import subprocess

# run this file if you want to execute all scripts from starting with just links from a excel file to gather data and scrub it into distinct csv's
# first script grabs all the data from fbs or fcs schools
#subprocess.run(["python", "Scripts\Scraper.py"])
# second script concatinates all the data together into one file
subprocess.run(["python", "Scripts\Concat_Rosters.py"])
# third script pulls all coaches from existing data into there own files for fbs and fcs
subprocess.run(["python", "Scripts\Pull_Coaches.py"])
# fourth script aggregate the data into new files to be used for vizualizations
subprocess.run(["python", "Scripts\Roster_Scruber.py"])