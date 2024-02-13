import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(3)
shop = driver.find_element_by_css_selector("#main-nav li:nth-child(1) > a")
shop.click()
HTML5_WebApp_add = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5_WebApp_add.click()
time.sleep(5)
item_number = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
item_number_text = item_number.text
assert item_number_text == "1 Item"
total = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
total_text = total.text
assert total_text == "₹180.00"
cart_btn = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart_btn.click()
subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal"),
"₹180.00"))
total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total"),
                                                                        "₹183.60"))
driver.quit()










