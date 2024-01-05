from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Broswer open after program runs.
chrome_options = webdriver.ChromeOptions()

# Create and configure the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Find the first name, last name, and email fields.
name_field = driver.find_element(By.NAME, value="fName")
last_name_field = driver.find_element(By.NAME, value="lName")
email_field = driver.find_element(By.NAME, value="email")

# Fill out form fields
name_field.send_keys("John")
last_name_field.send_keys("Dough")
email_field.send_keys("anotheroneBites@theDust.com")

# Locate the Sing up button, then click on it
sign_up_button = driver.find_element(By.CLASS_NAME, value="btn")
sign_up_button.send_keys(Keys.ENTER)
