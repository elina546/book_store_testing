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
time.sleep(5)
cart_btn = driver.find_element_by_css_selector("a.wpmenucart-contents")
cart_btn.click()
proceed_to_checkout = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                                      "div.wc-proceed-to-checkout > "
                                                                                   "a"), "PROCEED TO CHECKOUT"))

proceed_to_checkout_btn = driver.find_element_by_css_selector("div.wc-proceed-to-checkout > a")
proceed_to_checkout_btn.click()
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("test")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("testtest")
email = driver.find_element_by_id("billing_email")
email.send_keys("test@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("12234455")
country = driver.find_element_by_css_selector(".select2-choice")
country.click()
option_input = driver.find_element_by_id("s2id_autogen1_search")
option_input.send_keys("Belgium")
option_selected = driver.find_element_by_css_selector(".select2-result-selectable")
option_selected.click()

address = driver.find_element_by_id("billing_address_1")
address.send_keys("testtesttest")
postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("1212121222")
city = driver.find_element_by_id("billing_city")
city.send_keys("Antwerpen")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
option_pay = driver.find_element_by_css_selector("[value='cheque']")
option_pay.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
confirm_message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                                    ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

Payment_method = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                                                    ".shop_table.order_details tfoot "
                                                                                    "tr:nth-child(3)"),
                                                                                  "Check Payments"))
driver.quit()






