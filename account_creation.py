from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Fake data
experience = {
    "title": "Software Engineer",
    "company": "TechWave Solutions",
    "duration": "Jan 2020 - Present",
    "description": "Developed and maintained web applications, collaborated with cross-functional teams, and implemented scalable solutions."
}

education = {
    "school": "University of Example",
    "degree": "Bachelor of Science",
    "field_of_study": "Computer Science",
    "duration": "2015 - 2019"
}

# Set up ChromeDriver
driver_path = r'C:\Users\Simran\Desktop\University\6510 - CS and Defense\Project\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Update this path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Login to LinkedIn
def linkedin_login(email, password):
    try:
        driver.get("https://www.linkedin.com/login")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, '//button[text()="Sign in"]').click()
        print("Logged into LinkedIn!")
    except Exception as e:
        print(f"Error during login: {e}")

# Add Experience
def add_experience():
    try:
        driver.get("https://www.linkedin.com/in/your-profile-url/edit/experience/")  # Replace with your profile URL
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "experience-add"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "title"))).send_keys(experience["title"])
        driver.find_element(By.NAME, "companyName").send_keys(experience["company"])
        driver.find_element(By.NAME, "dateRange").send_keys(experience["duration"])
        driver.find_element(By.NAME, "description").send_keys(experience["description"])
        driver.find_element(By.XPATH, '//button[text()="Save"]').click()
        print("Experience added!")
    except Exception as e:
        print(f"Error while adding experience: {e}")

# Add Education
def add_education():
    try:
        driver.get("https://www.linkedin.com/in/your-profile-url/edit/education/")  # Replace with your profile URL
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "education-add"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "schoolName"))).send_keys(education["school"])
        driver.find_element(By.NAME, "degree").send_keys(education["degree"])
        driver.find_element(By.NAME, "fieldOfStudy").send_keys(education["field_of_study"])
        driver.find_element(By.NAME, "dateRange").send_keys(education["duration"])
        driver.find_element(By.XPATH, '//button[text()="Save"]').click()
        print("Education added!")
    except Exception as e:
        print(f"Error while adding education: {e}")

# Main script
if __name__ == "__main__":
    email = "your-email@example.com"  # Replace with LinkedIn email
    password = "your-password"  # Replace with LinkedIn password

    try:
        linkedin_login(email, password)
        add_experience()
        add_education()
    finally:
        driver.quit()
        print("Web driver closed.")
