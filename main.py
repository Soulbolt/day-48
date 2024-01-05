from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# Keep Broswer open after program runs.
chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
user_agent = ua.random
chrome_options.add_argument(f'--user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is: {price_dollar.text}.{price_cents.text}")
# driver.close()  # Closes a tab
driver.quit()  # Closes all tabs(program)
