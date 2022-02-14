# Dependencies
from splinter import Browser
from bs4 import Beautifulsoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

def scrape_all():

    # Connecting to database
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_db

    # Setting up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

   
   
    ## Scraping news title and paragrapgh ##
    url_news = "https://redplanetscience.com/"
    browser.visit(url_news)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title_1 = soup.find_all('div', class_='content_title')
    news_p_1 = soup.find_all('div', class_='article_teaser_body')

    title = news_title_1[0].text
    paragraph = news_p_1[0].text

    
    
    ## Scraping featured Image ##
    url_image = "https://spaceimages-mars.com/"
    browser.visit(url_image)

    html = browser.html
    soup = bs(html, "html.parser")

    image_url = soup.find('img', class_='fancybox-image').get('src')
    featured_image_url=f"https://spaceimages-mars.com/{image_url}"

    
    
    ## Mars Facts DataFrame ##
    import pandas as pd

    url_facts = "https://galaxyfacts-mars.com/"
    browser.visit(url_facts)

    table_df = pd.read_html(url_facts)[0]
    table_df = table_df.columns=["Description","Mars","Earth"]
    facts_df = table_df.set_index("Description", inplace=True)  

    
    
    ## Scraping Hemispheres ##
    hemispheres_image_url=[]

    url_hemi = "https://marshemispheres.com/"
    browser.visit(url_hemi)

    html = browser.html
    soup = bs(html, "html.parser")


    titles = soup.find_all('h3')
    
    for title in titles: 
        browser.links.find_by_partial_text("Hemisphere")

    hemispheres = soup.find_all("div", class_="item")
    hemi_image = []
    hemi_url = []

    for hemisphere in hemispheres:
        link = hemisphere.find("a")
        href = link["href"]
        title = link.text.strip()

        image = hemisphere.find("img", class_="thumb")
        hemi_image.append(url_hemi + image["src"])

    hemi_url.append({"title": title, "image url": hemi_image})

    
    ## Dictionary of information ## 
    mars_data={
        'news_title': title,
        'news_paragraph': paragraph,
        'featured image': featured_image_url,
        'facts': facts_df.to_html(classes = "table table-striped"),
        'hemispheres': hemi_url
    }


    browser.quit()
    
    return mars_data


