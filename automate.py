from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
username = 'Your username'
password = 'Your password'

url = 'https://twitter.com/login'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
time.sleep(5) # decrease or increase as per your convenience
driver.find_element_by_name('session[username_or_email]').send_keys(username)
driver.find_element_by_name('session[password]').send_keys(password)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div').click()
