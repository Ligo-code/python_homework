from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Setup driver
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Open the OWASP Top 10 page
driver.get("https://owasp.org/www-project-top-ten/")

# Wait for page to load
time.sleep(3)

# Find all Top 10 risks
risk_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/Top10/A"]')

# Extract data
results = []

for link in risk_links:
    name = link.text.strip()
    url = link.get_attribute("href").strip()

    if name and url:
        print(f"{name} → {url}")
        results.append({"Name": name, "URL": url})

# Close driver
driver.quit()

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)

print("Data saved to owasp_top_10.csv")
