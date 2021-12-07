# Dependencies
from splinter import Browser
from bs4 import Beautifulsoup as bs
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    img_url=scrape_hemispheres(browser)

    # Dictionary of information
    mars_data={
        'news_title': title,
        'news_paragraph': paragraph,
        'featured image': scrape_featured_image(browser),
        'facts': scrape_facts(),
        'hemispheres': img_url
    }
    browser.quit()
    return mars_data


# Latest Mars News
def scrape_news(browser):
    url="https://redplanetscience.com/"
    browser.visit(url)
    
    html= browser.html
    soup=bs(html, 'html.parser')

    try:
        title=soup.find("div", class_="content_title").text
        paragraph=paragraph=soup.find("div", class_="article_teaser_body").get_text
    except AttributeError:
        return None
    return title, paragraph


# Featured Image
def scrape_featured_image(browser):
    url="https://spaceimages-mars.com/"
    browser.visit(url)

    image=browser.find_by_tag('button')[1]
    image.click()

    html= browser.html
    soup=bs(html, 'html.parser')

    try:
        image_url=img_soup.find('img', class_='fancybox-image').get('src')
    except AttributeError:
        return None
        
    full_url=url + image_url

    return full_url

# Mars Facts
def scrape_facts():
    url="https://galaxyfacts-mars.com/"
    try:
        table_df=pd.read_html(url)[0]
    except BaseException:
        return None
    
    table_df.columns=["Description","Mars","Earth"]
    table_df.set_index("Description", inplace=True) 

    return table_df.to_html()

# Mars Hemispheres
def scrape_hemispheres(browser):
    url="https://marshemispheres.com/"
    browser.visit(url)

    hemispheres_image_url=[]

    main_url='https://marshemispheres.com/'

    
    for x in range(4):
        browser.find_by_css('a.product-item img')[x].click()

        html = browser.html
        soup = bs(html, 'html.parser')

        title= soup.find('h2', class_='title').text
        url= main_url + soup.find('li').a.get('href')

        hemispheres_image_url.append({"title": title, "image url": url})

        browser.back()

    return hemispheres_image_url

if __name__=="__main__":
    print()

