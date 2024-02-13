import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
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
select_orderby = driver.find_element_by_name("orderby")
# select_orderby_selected = select_orderby.get_attribute("selected")
# assert menu_order_checked is not None
select_orderby_value = select_orderby.get_attribute("value")
assert select_orderby_value == 'menu_order'
select = Select(select_orderby)
select.select_by_value("price-desc")
select_orderby = driver.find_element_by_name("orderby")
select_orderby_value = select_orderby.get_attribute("value")
assert select_orderby_value == 'price-desc'
driver.quit()
