from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Broswer open after program runs.
chrome_options = webdriver.ChromeOptions()

# Create and configure the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Find cookie and click on it
cookie = driver.find_element(By.ID, value="cookie").click()

# Find the money
money = driver.find_element(By.ID, value="money").text
print(money)

# Find Grandma and get the value
grandma = driver.find_element(By.ID, value="buyGrandma").text.split()[2]
print(grandma)
