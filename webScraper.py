from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up the web driver (ensure you have ChromeDriver installed)
driver_path = '/path/to/chromedriver'  # Replace with your driver path
driver = webdriver.Chrome(driver_path)

# Function to scrape data
def selenium_scrape(url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load (adjust as needed)

    # Get the page source and parse it
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Extract data you need
    for item in soup.select('h2'):  # Example: Scraping all h2 headers
        print(item.get_text(strip=True))

# Example usage
url = 'https://example.com'  # Replace with your target URL
selenium_scrape(url)

# Close the driver
driver.quit()
