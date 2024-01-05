from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

# Keep Broswer open after program runs.
chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
user_agent = ua.random
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f'--user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org")
total_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(total_articles.text)
# Click on link
# total_articles.click()
# Find Element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()
# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
# Sending keyboard input to Selenium using Keys.Enter
search.send_keys("Python", Keys.ENTER)

# driver.quit()

