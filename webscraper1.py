from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# Set up ChromeDriver
driver_path = r'C:\Users\Simran\Desktop\University\6510 - CS and Defense\Project\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Update this path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Function to scrape paragraphs and divs
def scrape_wikipedia(url):
    try:
        print(f"Scraping: {url}")
        driver.get(url)
        time.sleep(3)  # Wait for the page to load

        # Parse page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract <p> and <div> content
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        divs = [div.get_text(strip=True) for div in soup.find_all('div')]

        # Print and return extracted data
        print("Extracted Paragraphs:")
        print(paragraphs[:5])  # Preview first 5 paragraphs
        print("Extracted Divs:")
        print(divs[:5])  # Preview first 5 divs

        return {"paragraphs": paragraphs, "divs": divs}

    except Exception as e:
        print(f"Error while scraping: {e}")
        return {"paragraphs": [], "divs": []}

# Save scraped data to CSV
def save_to_csv(data, filename_prefix):
    # Save paragraphs to a separate file
    pd.DataFrame({"Paragraphs": data["paragraphs"]}).to_csv(f"{filename_prefix}_paragraphs.csv", index=False)
    print(f"Paragraphs saved to {filename_prefix}_paragraphs.csv")

    # Save divs to a separate file
    pd.DataFrame({"Divs": data["divs"]}).to_csv(f"{filename_prefix}_divs.csv", index=False)
    print(f"Divs saved to {filename_prefix}_divs.csv")

# Main script
if __name__ == "__main__":
    try:
        url = 'https://en.wikipedia.org/wiki/Computer_security'  # Replace with your target URL
        scraped_data = scrape_wikipedia(url)
        save_to_csv(scraped_data, "wikipedia_content")
    finally:
        driver.quit()
        print("Web driver closed.")
# Code Sources: https://brightdata.com/blog/how-tos/web-scraping-with-python and https://medium.com/@spaw.co/how-to-extract-content-from-a-div-tag-using-beautifulsoup-in-python-45c4acedd727
