import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(3)
my_account = driver.find_element_by_css_selector("#main-nav li:nth-child(2) > a")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("test_16@mail.ru")
password = driver.find_element_by_id("password")
time.sleep(5)
password.send_keys("kdM5j&fDz54gd")
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
shop = driver.find_element_by_css_selector("#main-nav li:nth-child(1) > a")
shop.click()
html_5_preview = driver.find_element_by_css_selector(".products.masonry-done .post-181 > a")
html_5_preview.click()
title = driver.find_element_by_tag_name("h1")
title_get_text = title.text
assert 'HTML5 Forms' in title_get_text
driver.quit()

