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
# driver.get("https://www.amazon.com/Logitech-G502-Performance-Gaming-Mouse/dp/B07GBZ4Q68")
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is: {price_dollar.text}.{price_cents.text}")

# ----------------------------------------------------------------------------------
# Ways to get different data
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")  # To get an anchor tab href link can look up class name where it lives.
# print(documentation_link.text)
# ----------------------------------------------------------------------------------
# Xpath works as a dictory tree ex. .root/folder1/folder_destination/file
# bug_link = driver.find_element(By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

#-----------------------------------------------------------------------------------
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_element(By.CSS_SELECTOR, value=".event-widget")  # Using .event-widget li a does not get any data instead produces error.
event_names = event_name.find_elements(By.TAG_NAME, value="a")
# event_name = driver.find_elements(By.XPATH, value="//*[@id='content']/div/section/div[3]/div[2]/div/ul/li[1]/a")
# times = [time.text for time in event_time]
names = [name.text for name in event_names[1:]]
events = {}
# key value pair formated on a nested dictioanry {0: {'time':date, 'name': event_name}}
# list_events = {time:name for (time,name) in zip(times[5:10], names[1:])}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": names[n],
    }

print(events)
# driver.close()  # Closes a tab
driver.quit()  # Closes all tabs(program)
