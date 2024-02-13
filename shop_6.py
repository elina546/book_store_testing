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
driver.execute_script("window.scrollBy(0, 300);")
HTML5_WebApp_add = driver.find_element_by_css_selector("[data-product_id='182']")
HTML5_WebApp_add.click()
time.sleep(7)
JS_Data_Structures_add = driver.find_element_by_css_selector("[data-product_id='180']")
JS_Data_Structures_add.click()
cart_btn = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart_btn.click()
time.sleep(7)
element_remove = driver.find_element_by_css_selector("form tr.cart_item td:nth-child(1) > a")
element_remove.click()
undo_link = driver.find_element_by_link_text("Undo?")
undo_link.click()
qty_text = driver.find_element_by_xpath("//form//tr[2]//input[ @title = 'Qty']")
qty_text.clear()
qty_text.send_keys(3)
update_cart = driver.find_element_by_name("update_cart")
update_cart.click()
qty_text_value = qty_text.get_attribute("value")
assert qty_text_value == '3'
time.sleep(5)
apply_coupon = driver.find_element_by_name("apply_coupon")
apply_coupon.click()
warning_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"
                                                                                 ), "Please enter a coupon code."))
driver.quit()













