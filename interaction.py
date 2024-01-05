from selenium import webdriver
from selenium.webdriver.common.by import By
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

driver.quit()

