import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


browser_options = webdriver.ChromeOptions()
browser_options.add_argument('--user-data-dir=/Users/Extramarks_Indonesia/AppData/Local/Google/Chrome/User Data/Default')

driver = webdriver.Chrome('C:/Users/Extramarks_Indonesia/Documents/UnreadChatWAbot/chromedriver',
                          options = browser_options) #change chromedriver path
driver.get("http://web.whatsapp.com/")
wait = WebDriverWait(driver, 50)
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[1]/div')))
driver.maximize_window()
reply = ['Hai kami sedang sibuk saat ini , tunggu beberapa saat lagi']
while True:
    try:
        content = driver.find_element_by_xpath("//span[@class ='_38M1B']")
        content.click()  # find the unread chat
        input_form = driver.find_element_by_xpath('//div[@class="_2A8P4"]')
        time.sleep(1)
        input_form.send_keys(reply)
        time.sleep(1)
        input_form.send_keys(Keys.ENTER)
        time.sleep(2)
    except Exception as e:
        pass
