import datetime
import selenium
import random
from time import sleep

from selenium.webdriver import ActionChains

from driver import driver
from Log_in import general_login
import vk_handler
from selenium.webdriver.common.keys import Keys

from my_logging import *
from zenja_down import debug_screenshot
from datetime import datetime


def hitroClick(self):
    link_presser = ActionChains(driver)
    link_presser.move_to_element_with_offset(self, 2, 2).click().perform()


def scan_tasks():  # parse target for all tasks
    sleep(3)
    task_list = driver.find_elements_by_xpath("//div[@class='join-group']")
    scroll = driver.find_element_by_tag_name("html")
    scroll.send_keys(Keys.END)
    sleep(3)

    for task in reversed(task_list):
        if str(task.find_element_by_xpath(".//span").text).startswith("Вступить в сообщество"):

            link = task.find_element_by_xpath(".//a[1]")
            for i in range(20):
                try:
                    sleep(2)
                    link.hitroClick()
                    break
                except selenium.common.exceptions.MoveTargetOutOfBoundsException:
                    scroll.send_keys(Keys.UP)

            driver.switch_to.window(driver.window_handles[-1])
            vk_handler.join_group(driver)
            sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            link = task.find_element_by_xpath(".//a[2]")
            link.hitroClick()
            sleep(3)

            #TODO:


        if str(task.find_element_by_xpath(".//span").text).startswith("Добавить в друзья"):
            link = task.find_element_by_xpath(".//a[1]")
            for i in range(20):
                try:
                    sleep(2)
                    link.hitroClick()
                    break
                except selenium.common.exceptions.MoveTargetOutOfBoundsException:
                    scroll.send_keys(Keys.UP)

            driver.switch_to.window(driver.window_handles[-1])
            vk_handler.add_to_friends(driver)
            sleep(3)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            link = task.find_element_by_xpath(".//a[2]")
            link.hitroClick()
            sleep(3)



# webdriverTUNING
selenium.webdriver.firefox.webelement.FirefoxWebElement.hitroClick = hitroClick
# end of webdriverTUNING

counter = 0
while True:
    if counter < 10:
        try:
            general_login()
            scan_tasks()
            logging.info('выход на охоту: '+str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S')))
        except Exception:
            error = str('!!!выход провален: ' + str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S'))+'\n'+str(Exception))
            logging.error(error)
    counter = (counter + 1) % 14 # burnaya noch' simulation
    sleep(60 * random.uniform(61, 75))  # чтоб типа как человек
