from select import select
from time import time
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from faker import Faker
import time


# path URL for chromedriver
driver = webdriver.Chrome(
    executable_path="/Users/officemacmini/Documents/testing automation/chromedriver")

# launch URL
driver.get("https://www.psegameshop.com/")

# Click button for login or register menu
loginbtn = driver.find_element_by_xpath(
    '/html/body/div[2]/header/div/div[2]/div[1]/div[4]/ul/li[3]/a/i')
loginbtn.click()

# Field favorite Genre
Element = driver.find_element_by_id("acf-field_5e758bca4e8cc")
drpd = Select(Element)
drpd.select_by_index(1)
time.sleep(1)

# Field favorite console
Element = driver.find_element_by_id("acf-field_5e75905014c81")
drpd1 = Select(Element)
drpd1.select_by_value("Playstation")
time.sleep(1)

# Field hobbies & Interest
Element = driver.find_element_by_id("acf-field_5ea976d054e4e")
drpd2 = Select(Element)
drpd2.select_by_visible_text("Culinary")
time.sleep(1)

# Radio button to select gender
driver.find_element_by_id("acf-field_5ea3be750efb3-female").click()
status = driver.find_element_by_id(
    "acf-field_5ea3be750efb3-female").is_selected()
print(status)

# Field to input data email
fake = Faker()
driver.find_element_by_id("reg_email").send_keys(fake.email())

# Field to input data password
driver.find_element_by_id("reg_password").send_keys("Hanyasebatastesting123!")

# Field to input data confirm password
driver.find_element_by_id("reg_confirm_password").send_keys(
    "Hanyasebatastesting123!")

# Field for click button register
driver.find_element_by_name("register").click()

# tes result
act_title = driver.title
exp_title = "Home - PS Enterprise Gameshop"

# Validation for test result
if act_title == exp_title:
    print("search test passed")
else:
    print("search test failed")

time.sleep(10)
