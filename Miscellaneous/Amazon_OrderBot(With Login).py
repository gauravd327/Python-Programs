from selenium import webdriver
from selenium.webdriver.common.keys import Keys

item = input("Enter the url for the item: ")
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(item)

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


def addToCart():
    # Adding the item to the cart
    cart = driver.find_element_by_id("add-to-cart-button")
    cart.click()

    driver.implicitly_wait(1)

    # Checking the item out
    go_to_cart = driver.find_element_by_id("nav-cart-count")
    go_to_cart.click()

    driver.implicitly_wait(1)

    go_to_checkout = driver.find_element_by_class_name("a-button-input")
    go_to_checkout.click()


def checkout():
    place_order = driver.find_element_by_name("placeYourOrder1")
    place_order.click()


username = "Whatever your username is"
password = "Whatever you password is"

login(username, password)
addToCart()
checkout()
