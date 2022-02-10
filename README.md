# **Web Scraping Challenge: Mission to Mars**

![](Missions_to_Mars/images/mission_to_mars.png)

**Task 1: Scraping** 
<hr>

Jupyter Notebook, BeautifulSoup, Pandas and Requests/Splinter is used to scrape the following:

* NASA Mars News: latest News Title and Paragraph Text
* JPL Mars Space Image: the Image URL for the current Featured Mars Image
* Mars Facts: Table containing facts about the planet including Diameter, Mass etc
* Mars Hemispheres: Hemisphere Title and Hemisphere URL for each hemisphere.
<br>

**Task 2: MongoDB and Flask Application** 
<hr>

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

* Created a route called /scrape that will import your scrape_mars.py script and call your scrape function.

* Store the return value in Mongo as a Python dictionary.
Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.
<br>





