from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.ca")

# Optional: Close the browser after a few seconds
import time
time.sleep(5)
driver.quit()




