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
time.sleep(3)
sign_out = driver.find_element_by_link_text("Sign out")
sign_out.click()
driver.execute_script("window.open();")
window_2 = driver.window_handles[1]
driver.switch_to.window(window_2)
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

# коммент
