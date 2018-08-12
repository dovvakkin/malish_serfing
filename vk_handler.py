from datetime import datetime
import selenium
from time import sleep


def redirect_to_mvk(driver):
    sleep(2)
    driver.execute_script(
        'alert(window.location.href);')  # FUCKING AWESOME FUCKING BEST FUCKING KING OF FUCKING KOSTILI
    alert = driver.switch_to_alert()  # ^^^
    link = str(alert.text).replace("https://vk.com/", "https://m.vk.com/")  # ^^^
    driver.switch_to_alert().accept()  # ^^^
    driver.get(link)  # ^^^

    # right solve:
    # sleep(2)
    # link = str(driver.current_url).replace("https://vk.com/","https://m.vk.com/")
    # driver.get(link)


def like_on_page(driver):
    try:
        redirect_to_mvk(driver)
        sleep(5)
        like = driver.find_element_by_xpath("//a[@onclick='return ajax.click(this, Like);']")
        like.click()
    except:
        pass
        # debug_screenshot("VK_like_on_page_")


def join_group(driver):
    try:
        redirect_to_mvk(driver)
        sleep(5)
        join = driver.find_element_by_xpath("//a[@class='button wide_button']")
        join.click()
    except selenium.common.exceptions.NoSuchElementException:
        pass
        # debug_screenshot("VK_join_group_")


def add_to_friends(driver):
    try:
        redirect_to_mvk(driver)
        sleep(5)
        try:
            add = driver.find_element_by_xpath("//a[@class='button wide_button acceptFriendBtn']")
        except:
            add = driver.find_element_by_xpath("//a[@class='button wide_button']")
        add.click()
    except:
        pass
        # debug_screenshot("VK_add_to_friends_")


def make_repost(driver):
    driver.get("https://vk.com/wall-153733218_56")
    try:
        redirect_to_mvk(driver)
        sleep(5)
        add = driver.find_element_by_xpath(
            "//html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div[4]/div/span[1]/a[2]/i")
        add.click()
        add = driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/form/div[4]/input")
        add.click()
    except:
        pass
        # debug_screenshot("VK_add_to_friends_")