import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector("#main-nav li:nth-child(2) > a")
my_account.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("test_16@mail.ru")
password = driver.find_element_by_id("reg_password")
time.sleep(5)
password.send_keys("kdM5j&fDz54gd")
submit_btn = driver.find_element_by_css_selector("[name='register']")
submit_btn.click()
driver.quit()


