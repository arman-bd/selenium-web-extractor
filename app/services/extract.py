import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

async def youtube_metadata(driver: uc.Chrome, id: str):
    # Open the page
    driver.get(f"https://www.youtube.com/watch?v={id}")

    # Wait for the page to load
    time.sleep(5)

    # Get the Title
    title = driver.find_element(By.CSS_SELECTOR, "h1.title yt-formatted-string").text
    
    # Get the Description
    description = driver.find_element(By.CSS_SELECTOR, "#description > yt-formatted-string").text
    
    # Get the Thumbnail
    thumbnail = driver.find_element(By.CSS_SELECTOR, "#img").get_attribute("src")
    
    # Get the Channel Name
    channel_name = driver.find_element(By.CSS_SELECTOR, "#text > a").text
    
    # Get Views
    view_count = driver.find_element(By.CSS_SELECTOR, "#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer").text
    
    # Get Likes
    like_count = driver.find_element(By.CSS_SELECTOR, "#top-level-buttons > ytd-toggle-button-renderer:nth-child(1) > a > yt-formatted-string").text
    
    # Return Data
    return {
        "title": title,
        "description": description,
        "thumbnail": thumbnail,
        "channel_name": channel_name,
        "view_count": view_count,
        "like_count": like_count
    }
    
    
    
