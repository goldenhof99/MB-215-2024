import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        """Setup the test environment before each test."""
        # Dynamically get the absolute path to chromedriver.exe
        chrome_driver_path = os.path.abspath("chromedriver.exe")
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def test_search_in_google(self):
        """Test searching for 'Python' on Google."""
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google", driver.title)

        # Find the search box, enter 'Python', and submit the form
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python")
        search_box.send_keys(Keys.RETURN)  # Simulate pressing Enter

        # Wait for results to load
        time.sleep(5)

        # Check if 'python.org' is in the search results
        self.assertIn("python.org", driver.page_source)

    def tearDown(self):
        """Cleanup after the test."""
        self.driver.quit()  # Close the browser after the test completes

if __name__ == "__main__":
    unittest.main()




