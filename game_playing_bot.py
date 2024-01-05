from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Broswer open after program runs.
chrome_options = webdriver.ChromeOptions()

# Create and configure the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")