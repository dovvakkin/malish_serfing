import datetime
import selenium
import random
from time import sleep

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import ActionChains
from Log_in import general_login
import vk_handler
from selenium.webdriver.common.keys import Keys
from my_logging import *
from datetime import datetime


def driver_init():  # setup webdriver and login to target
    local_driver = webdriver.Firefox()
    display = Display(visible=1, size=[800, 800])
    display.start()
    return local_driver


def hitroClick(self, driver):
    link_presser = ActionChains(driver)
    link_presser.move_to_element_with_offset(self, 2, 2).click().perform()


def task_performer(driver, task, handler_function):
    link = task.find_element_by_xpath(".//a[1]")
    for i in range(20):
        try:
            sleep(2)
            link.hitroClick(driver)
            break
        except selenium.common.exceptions.MoveTargetOutOfBoundsException:
            driver.triple_scroll()

    driver.switch_to.window(driver.window_handles[-1])
    handler_function(driver)
    sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    link = task.find_element_by_xpath(".//a[2]")
    link.hitroClick(driver)
    sleep(2)


def triple_scroll(self):
    scroll_action = ActionChains(self)
    scroll_action.key_down(Keys.UP).key_up(Keys.UP).key_down(Keys.UP).key_up(Keys.UP).key_down(Keys.UP).key_up(
        Keys.UP).perform()


def scan_tasks(driver):  # parse target for all tasks
    driver.get("https://vkserfing.ru/assignments")
    sleep(3)  # wait for page loaded
    task_list = driver.find_elements_by_xpath("//div[@class='join-group']")
    scroll = driver.find_element_by_tag_name("html")
    scroll.send_keys(Keys.END)
    sleep(1)

    for task in reversed(task_list):
        if str(task.find_element_by_xpath(".//span").text).startswith("Вступить в сообщество"):
            task_performer(driver, task, vk_handler.join_group)
        elif str(task.find_element_by_xpath(".//span").text).startswith("Добавить в друзья"):
            task_performer(driver, task, vk_handler.add_to_friends)
        elif str(task.find_element_by_xpath(".//span").text).startswith("Рассказать друзьям"):
            task_performer(driver, task, vk_handler.make_repost)


def bot_life(login, password):
    # webdriverTUNING
    selenium.webdriver.firefox.webelement.FirefoxWebElement.hitroClick = hitroClick
    selenium.webdriver.firefox.webdriver.WebDriver.triple_scroll = triple_scroll
    # end of webdriverTUNING

    driver = driver_init()
    counter = 0
    while True:
        if counter < 10:
            try:
                general_login(driver, login, password)
                scan_tasks(driver)
                logging.info('выход на охоту: ' + str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S')))
            except Exception as e:
                error = str('!!!выход провален: ' + str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S')) + '\n' + str(e))
                logging.error(error)
        counter = (counter + 1) % 14  # burnaya noch' simulation
        sleep(60 * random.uniform(61, 75))  # чтоб типа как человек
