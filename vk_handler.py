from datetime import datetime
import selenium
import Selenium2Library
from time import sleep

def like_on_page(driver):
    try:
        like = driver.find_element_by_xpath("//a[@onclick='return ajax.click(this, Like);']")
        like.click()
    except:
        pass
        # debug_screenshot("VK_like_on_page_")


def join_group(driver):
    try:
        sleep(2)
        driver.execute_script('alert(window.location.href);') # FUCKING AWESOME FUCKING BEST FUCKING KING OF FUCKING KOSTILI
        alert = driver.switch_to_alert() #^^^
        link = str(alert.text).replace("https://vk.com/","https://m.vk.com/") #^^^
        driver.switch_to_alert().accept() #^^^
        driver.get(link) #^^^

        # sleep(2)
        # link = str(driver.current_url).replace("https://vk.com/","https://m.vk.com/")
        # driver.get(link)

        sleep(5)
        join = driver.find_element_by_xpath("//a[@class='button wide_button']")
        join.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
        # debug_screenshot("VK_join_group_")


def add_to_friends(driver):
    try:
        sleep(2)
        driver.execute_script('alert(window.location.href);')
        alert = driver.switch_to_alert()
        link = str(alert.text).replace("https://vk.com/", "https://m.vk.com/")
        driver.switch_to_alert().accept()
        driver.get(link)

        sleep(5)
        add = driver.find_element_by_xpath("//a[@class='button wide_button acceptFriendBtn']")
        add.click()
    except:
        pass
        # debug_screenshot("VK_add_to_friends_")