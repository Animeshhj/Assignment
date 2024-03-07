from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

# Initialize Chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

# Load the Time.com homepage
driver.get("https://time.com/")

# Wait for the page to load
time.sleep(5)

# Attempt to close any pop-up ads
try:
    close_ad = driver.find_element(By.CLASS_NAME, 'animate-close')
    close_ad.click()
    time.sleep(2)  # Wait for the ad to close
    print("Pop-up ad closed successfully.")
except:
    print("No pop-up ad found or could not be closed.")

# Wait for the latest stories to load
try:
    latest_stories = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'latest-stories__item')))
    print("Latest stories found:")
    for story in latest_stories:
        print(story.text)
except:
    print("Could not find latest stories.")

# Quit the driver
driver.quit()