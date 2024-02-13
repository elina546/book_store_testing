import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_css_selector("#main-nav li:nth-child(2) > a")
my_account.click()
time.sleep(5)
username = driver.find_element_by_id("username")
username.send_keys("test_16@mail.ru")
password = driver.find_element_by_id("password")
time.sleep(5)
password.send_keys("kdM5j&fDz54gd")
login_btn = driver.find_element_by_css_selector("[name='login']")
login_btn.click()
logout = driver.find_element_by_link_text("Logout")
logout_get_text = logout.text
assert 'Logout' in logout_get_text
driver.quit()

