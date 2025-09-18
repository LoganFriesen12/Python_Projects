from selenium import webdriver
import re
from bs4 import BeautifulSoup
import time
import os
import requests

# Opens browser to website to download images
browser = webdriver.Edge() 
browser.get("https://www.flickr.com/")

# Asks for a image to search for and how many to download
imageSearch = input('What would images would you like to find? ')
imgNum = int(input('How many images would you like to download? '))
save_folder = r"C:\Users\logan\OneDrive\Documents\Python Text"

# Clicks on search field and searches the type of images you want
searchElem = browser.find_element('css selector', '''body > div.page-wrapper > div.nav_fixed >
div.navigation.w-nav > div.navigation-container > div.navigation-right > div > a.search.w-inline-block >
div > svg''')
searchElem.click()
searchField = browser.find_element('css selector', '#text-2')
searchField.send_keys(imageSearch)
searchField.submit()
time.sleep(2)


# Finds the right class in the source code of webpage to iterate over
# and download the images
soup = BeautifulSoup(browser.page_source, "html.parser")
top_image_element = soup.find("div", class_="view photo-list-view requiredToShowOnServer")
print(top_image_element) # Debugging step

if top_image_element is None:
    print('Error: Could not image container.') 
else:    
    for i, child in zip(range(imgNum), top_image_element.children):
        img_tag = child.find("img")
        if img_tag:
            img_url = img_tag.get("src")
            # Checks URL to make sure it has full path (Https:)
            if img_url and img_url.startswith("//"):
                img_url = "https:" + img_url
            # If it finds URL it makes the proper folder and downloads the image in chunks
            if img_url:
                img_name = f"image_{i}.jpg"
                img_path = os.path.join(save_folder, img_name)
                response = requests.get(img_url, stream=True)
                if response.status_code == 200:
                    with open(img_path, "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                            print(f"Downloaded: {img_path}")
                else:
                    print('Error: Image not downloaded.')
            else:
                print('Error: No image url found.')
        else:
            print('Error: No image tag found.')
    
