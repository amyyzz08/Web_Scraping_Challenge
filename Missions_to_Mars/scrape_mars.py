# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

def scrape_all():

    # Setting up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)


    # Scraping news title and paragrapgh ##
    url_news = "https://redplanetscience.com/"
    browser.visit(url_news)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title_1 = soup.find_all('div', class_='content_title')
    news_p_1 = soup.find_all('div', class_='article_teaser_body')

    title = news_title_1[0].text
    paragraph = news_p_1[0].text

    
    
    ## Scraping featured Image ##
    url_image = "https://spaceimages-mars.com/"
    browser.visit(url_image)

    full_image_button = browser.find_by_tag('button')[1]
    full_image_button.click()

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    image_url = soup.find('img', class_='fancybox-image').get('src')
    featured_image_url= url_image + image_url

    
    
    ## Mars Facts DataFrame ##
    import pandas as pd

    url_facts = "https://galaxyfacts-mars.com/"
    browser.visit(url_facts)

    table_df = pd.read_html(url_facts)[0]
    table_df.columns=["Description","Mars","Earth"]
    table_df.set_index("Description", inplace=True)  

    
    
    ## Scraping Hemispheres ##

    url_hemi = "https://marshemispheres.com/"
    browser.visit(url_hemi)
  
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    results = soup.find_all("div", class_="item")

    hemi_image = []

    for result in results:

        # scrapping
        link = result.find("a")
        href = link["href"]
        pic = result.find("img", class_="thumb")

        hemi_image.append(url_hemi + pic["scr"])
        print(hemi_image)

  
    ## Dictionary of information ## 
    mars_data={
        'news_title': title,
        'news_paragraph': paragraph,
        'featured_image': featured_image_url,
        'facts': table_df.to_html(classes = "table table-striped"),
        'hemispheres': hemi_image
    }


    browser.quit()
    
    return mars_data


