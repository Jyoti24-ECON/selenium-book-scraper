
# Importing required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


# Step 1: Starting the browser

print("Starting browser...")
driver = webdriver.Chrome()

print("Opening website...")
driver.get("https://books.toscrape.com/")


# Step 2: Creating wait object
# This ensures elements load before scraping
wait = WebDriverWait(driver, 10)



# Step 3: Preparing data storage
books_data = []



# Step 4: Looping through pages

while True:
    # Wait until book elements are present
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod")))

    # Find all book containers on the page
    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    print("Scraping page...")

    
    # Step 5: Extracting data for each book
  
    for book in books:
        # Extracting title
        h3 = book.find_element(By.TAG_NAME, "h3")
        link = h3.find_element(By.TAG_NAME, "a")
        title = link.get_attribute("title")

        # Extracting price
        price = book.find_element(By.CLASS_NAME, "price_color").text

        # Extracting rating
        rating_class = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
        rating = rating_class.split()[1]

        # Storing extracted data
        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

   
    # Step 6: Moving to next page
    
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(1)  # allowing  next page to load
    except:
        #  If no next page found,  stop looping
        break



# Step 7: Closing the  browser

driver.quit()



# Step 8: Saving data to CSV

df = pd.DataFrame(books_data)
df.to_csv("books_dataset.csv", index=False)

print("Scraping complete.")
print("Total books scraped:", len(df))

