import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
android_quick_preview = driver.find_element_by_css_selector(".products.masonry-done .post-169 > a")
android_quick_preview.click()
old_price = driver.find_element_by_css_selector(".price del span.amount")
old_price_text = old_price.text
assert "₹600.00" in old_price_text
new_price = driver.find_element_by_css_selector(".price ins span.amount")
new_price_text = new_price.text
assert "₹450.00" in new_price_text
wait = WebDriverWait(driver, 10)
image_book = driver.find_element_by_css_selector(".images > a")
image_book.click()
image_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
image_close.click()
driver.quit()









