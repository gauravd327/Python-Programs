from selenium import webdriver
from selenium.webdriver.common.keys import Keys

item = input("Enter the url for the item: ")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(item)


# This function might not be required as
# logging in will mostly require manual work

def login(email, key):
    check_login = driver.find_element_by_id("nav-link-accountList")
    check_login.click()

    # Enter username/email
    search_email = driver.find_element_by_name("email")
    search_email.send_keys(email)
    search_email.send_keys(Keys.RETURN)

    # Enter password
    search_email = driver.find_element_by_name("password")
    search_email.send_keys(key)
    search_email.send_keys(Keys.RETURN)

    # OTP
    otp_button = driver.find_element_by_id("continue")
    otp_button.click()

    x = input("Enter the OTP: ")
    answer = driver.find_element_by_name("code")
    answer.send_keys(x)
    answer.send_keys(Keys.RETURN)


def addToCart():
    # Adding the item to the cart
    cart = driver.find_element_by_id("add-to-cart-button")
    cart.click()

    # Checking the item out
    go_to_cart = driver.find_element_by_id("nav-cart")
    go_to_cart.click()

    go_to_checkout = driver.find_element_by_class_name("a-button-input")
    go_to_checkout.click()


def checkout():
    deliver = driver.find_element_by_class_name("a-button-inner")
    deliver.click()


username = "gauravdharmadhikari2@gmail.com"
password = "pokemongames101"

login(username, password)

addToCart()

checkout()
