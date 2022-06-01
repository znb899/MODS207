# This program saves the videos' links using selenium
# from a single channel in a channel_<channel's id>.csv file.
# The channel's id has to be provided as an argument

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import pandas as pd

import warnings
warnings.filterwarnings('ignore')

import sys

channelId = sys.argv[1]

def getVideos(channelId):
    # gets list of videos links from a channel
    # channelId : id if the videos' channel
    
    # open the browser
    driver = webdriver.Chrome('./chromedriver')
    link = 'https://www.youtube.com/channel/'+channelId
    driver.get(link)

    # accept terms of services
    button = driver.find_element_by_css_selector('button[aria-label="Accept all"]')
    driver.execute_script("arguments[0].click();", button)

    # go to video section of the channel
    videos = driver.find_elements_by_css_selector("div[style-target='tab-content']")[1]
    driver.execute_script("arguments[0].click();", videos)
    
    # keep scrolling enough (<<500) until at the bottom of the page (<<100000000)
    for i in range(500):
        driver.execute_script("window.scrollTo(0, 100000000);")

    # collect of the thumbnails
    links = driver.find_elements_by_css_selector('a[id="thumbnail"]')

    videos = []
    for l in links:
        # and keep only the videos's link
        videos.append(l.get_attribute("href"))
    
    driver.quit()
    
    return videos

videos = getVideos(channelId)
df = pd.DataFrame(videos, columns=["videoId"])

# save file
df.to_csv(f'channel_{channelId}.csv', index=False)
