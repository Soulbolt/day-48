from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Minutes to run and intervals to check
GAME_TIME_MIN = 1*60
INTERVAL_IN_SEC = time.time() +5
# Keep Broswer open after program runs.
chrome_options = webdriver.ChromeOptions()

# Create and configure the Chrome webdriver
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Find cookie and click on it
cookie = driver.find_element(By.ID, value="cookie")


# # Find the money
# money = driver.find_element(By.XPATH, value="//*[@id='money']").text
# print(money)

# Create Loop to auto click cookie and check money value against Grandma's value, click on Grandma if money >=
start_time = time.time()
while (time.time() - start_time) < GAME_TIME_MIN:
    money = driver.find_element(By.XPATH, value="//*[@id='money']").text
    # Find Grandma and get the value
    grandma = driver.find_element(By.ID, value="buyGrandma").text.split()[2]
    # print(grandma)
    click_buy_grandma = driver.find_element(By.ID, value="buyGrandma")
    score = driver.find_element(By.ID, value="cps").text
    # Click on cookie`
    cookie.click()
    # time_check = (time.time() - start_time)
    # print(time_check)
    # print(f"money: {int(money)}\nGrandma: {int(grandma)}")
    if time.time() > INTERVAL_IN_SEC:
        if int(money) > int(grandma):
            click_buy_grandma.click()
            time.sleep(.05)
    else:
        pass
print(score)
driver.quit()
