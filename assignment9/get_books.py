from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

# Setup driver (headless)
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

# Open the page
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

# Wait for the page to load
time.sleep(3)

# Step 1: Find all li elements (book entries)
book_entries = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
print(f"Found {len(book_entries)} books")

# Step 2: Iterate and extract data
results = []

for entry in book_entries:
    # Title
    try:
        title_el = entry.find_element(By.CSS_SELECTOR, 'h2.cp-title a.title-content')
        title = title_el.text.strip()
    except Exception as e:
        title = ''
    
    # Authors
    try:
        author_elements = entry.find_elements(By.CSS_SELECTOR, 'a.author-link')
        authors = '; '.join([author.text.strip() for author in author_elements])
    except Exception as e:
        authors = ''
    
    # Format + Year
    try:
        format_el = entry.find_element(By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary')
        format_year = format_el.text.strip()
    except Exception as e:
        format_year = ''
    
    # Add to results
    book = {
        'Title': title,
        'Author': authors,
        'Format-Year': format_year
    }
    results.append(book)

# Close the driver
driver.quit()

# Step 3: Create DataFrame
df = pd.DataFrame(results)
print(df)

# Step 4: Save CSV
df.to_csv('get_books.csv', index=False)

# Step 5: Save JSON
with open('get_books.json', 'w') as f:
    json.dump(results, f, indent=4)

print("Data saved to get_books.csv and get_books.json")
