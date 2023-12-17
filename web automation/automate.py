import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
def login_to_mojo(driver, username, password):
    driver.get("https://lb11.mojosells.com/login/")

    try:
        # Wait for the email input to be present
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )

        # Wait for the password input to be present
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )

        # Wait for the submit button to be present and clickable
        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )

        # Login
        email_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

        # Wait for the login to complete
        WebDriverWait(driver, 20).until(
            EC.url_changes("https://app1051.mojosells.com/home/")
        )

    except TimeoutException:
        print("Timed out during login. Page structure might have changed.")
        print("Current URL:", driver.current_url)
        print("Page Source:", driver.page_source)

    except (WebDriverException, Exception) as e:
        print(f"An error occurred during login: {e}")
        print("Current URL:", driver.current_url)
        print("Page Source:", driver.page_source)

from selenium.webdriver.common.action_chains import ActionChains

def navigate_to_data_dialer(driver):
    try:
        # Assuming the URL directly leads to the Data & Dialer page
        data_dialer_url = "https://app1051.mojosells.com/data-and-dialer"  # Update with the correct URL
        driver.get(data_dialer_url)

        # Add a delay to allow the page to stabilize
        time.sleep(2)

        # Wait for the "Data & Dialer" link to be present
        data_dialer_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Data & Dialer"))
        )

        # Use ActionChains to move to the element and click it
        actions = ActionChains(driver)
        actions.move_to_element(data_dialer_link).click().perform()

        # Wait for the navigation to complete
        WebDriverWait(driver, 20).until(
            EC.url_contains("https://app1051.mojosells.com/data-and-dialer")
        )

    except TimeoutException:
        print("Timed out while navigating to Data & Dialer. Page structure might have changed.")
        print("Current URL:", driver.current_url)
        print("Page Source:", driver.page_source)

def navigate_to_calling_list(driver):
    try:
        # Wait for the "Calling List" button to be clickable
        calling_list_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "calling_list"))
        )

        # Click on the "Calling List" button
        calling_list_button.click()

        # Wait for the search input to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='search-input']"))
        )

        # Wait for the search results to load (you may need to adjust this wait condition)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='search-results']"))
        )

    except TimeoutException:
        print("Timed out while navigating to Calling List. Page structure might have changed.")
        print("Current URL:", driver.current_url)
        print("Page Source:", driver.page_source)

def search_in_calling_list(driver, search_query):
    try:
        # Wait for the search input to be present and clickable
        search_input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='SelectField_searchContainer__1f5Y-']//input[@class='SelectField_searchBarSide__1MlwY']"))
        )

        # Set the value of the search input
        search_input.clear()
        search_input.send_keys(search_query)
        # time.sleep(600)
        # Wait for the search results to load dynamically
        # WebDriverWait(driver, 20).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//*[@id='1-main-97']/div/div[1]/div[3]"))
        # )

        # Assuming the first search result is the desired one, you can adjust as needed
        first_result_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='1-main-97']/div/div[1]/div[3]"))
        )

        # Use ActionChains to click on the element
        actions = ActionChains(driver)
        actions.move_to_element(first_result_element).click().perform()

        # Wait for the details to load (you may need to adjust this wait condition)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='SelectFieldElement_contents__1224f']"))
        )

        print("Clicked on the first search result:", search_query)

    except TimeoutException as te:
        print("Timed out while searching in Calling List. Page structure might have changed.")
        print("Current URL:", driver.current_url)
        print("Page Source:", driver.page_source)
        raise te  # Re-raise the exception to terminate the script



# Create a webdriver instance
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

# Replace 'your_username' and 'your_password' with the actual credentials
username = "admin@nitrohouses.com"
password = "testfiver"

try:
    # Log in to Mojo
    login_to_mojo(driver, username, password)

    # Navigate to the Data & Dialer page
    navigate_to_data_dialer(driver)

    # Navigate to the Calling List page
    navigate_to_calling_list(driver)

    # Search in the Calling List
    search_query = "JAMES 5.4.23 SA Expired"
    search_in_calling_list(driver, search_query)
finally:
    # Close the browser window
    driver.quit()
