# Image Script

The purpose of this script is to extract images from a list of FCS and FBS schools.

The output of the script is 4 files: 2 files for the player images from each school, and 2 files for the links that could not be scraped from each.

### How to use:

Clone this repository and install the required dependencies. When within the same directory as image_scraper.py and 2023_roster_links.xlsx, type python3 imge_scraper.py. When prompted, enter which sheet you would like to scrape (FBS or FCS).

### Dependencies:

requests <br>
bs4 <br>
pandas <br>
csv <br>
urllib <br>
selenium

### Understanding the output:

Many links within FCS and FBS contained websites that did not have player images on the first page. Many of the player images were located on a second page, with a link to that page being stored on a link contained within their name in the table. In the output player image files, there is a column titled "Source Image?" that denotes whether the link for the player is the source image for the player (yes), or if it is a link to the page that contains the player image (no). The links that could not be scraped were either because: the website did not contain a table (containing the list of player names with the images attached), did not contain any images, or possibly other reasons such as not having a normal table format.
