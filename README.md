# ReadMe Tableau Documentation:
## Version: Tableau Desktop 2020.4
## Data Source: Position Based Data


### How to import the data to Tableau:

1. Go into Position Based Data Folder and select the desired files. You should select the ourlads and ncaa versions of the data. For example, if I am interested in the data of offensive players I would download the ourlads_offense.xlsx and ncaa_offense.xlsx files.

2. Open Tableau Desktop and click Microsoft Excel under the Connect tab on the left hand side. Select one of the two files you want. 

3. Add the other file by clicking the 'Add' button by the connections tab. 

4. Once the second file is added, drag Sheet1 to the top environment space. This should create a new table called Sheet11. 

5. Click on the red dashed line between Sheet1 and Sheet11 to open the 'Edit Relationship' tab. Choose the common field ('Player' or 'Playerguid'). Now your data sources are linked via this common field.

6. Click on Sheet 1 on the tool bar at the bottom of the window and add the attributes you are interested in.  




Recreate Wide Receiver (WR) Catchers per Game vs. Height visualization:

1. Follow steps 1-6 above and import the ourlads_offense.xlsx and ncaa_offense.xlsx files.

2. Add the HT (height) attribute to the columns and modify the measure to Average (to do this click on the attribute cell and scroll down to measure).

3. Add Receptions_perc (percentage of receptions per game per season) to the rows and modify the measure to Average. 

4. Add the Pos (position) attribute to filters and choose WR as the only included field. Add AVG(HT) and AVG(Receptions_perc) to the filters, as well. Click on the dropdown arrow in the cell for each of these filters and click 'Show Filter'

5. Add Player as a detail in the Marks section. 




Actionable Insights for above visualization: 

Based on the volume of players at a given height, we can see that wide receivers that range from 70-76 inches in height have the highest reception percentage per season. Players above or below this height threshold have less receptions per season. 
