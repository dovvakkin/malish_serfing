import datetime
import re
import selenium
import random
from time import sleep

from selenium.webdriver import ActionChains

from driver import driver
from vk_handler import vk_task_manager
from Log_in import general_login
from my_logging import *
from zenja_down import debug_screenshot
from datetime import datetime


def check_profit():
    i = 1
    driver.get("https://vktarget.ru/list/")
    while True:
        try:
            xpath = str("/html/body/div[22]/div/div[3]/div[7]/div[" + str(i) + "]/div[6]")
            button = driver.find_element_by_xpath(xpath)
            sleep(random.uniform(2, 10))  # pause for stop yorzat'
            button.click()
            i += 1
        except selenium.common.exceptions.NoSuchElementException:
            break


def hitroClick(task):
    link_presser = ActionChains(driver)
    link_presser.move_to_element_with_offset(task, 5, 5).click().perform()


def get_task_list():  # parse target for all tasks
    task_list = driver.find_elements_by_xpath("//div[@class='join-group']")
    for task in task_list:
        link = task.find_element_by_xpath(".//a[1]")
        hitroClick(link)
        driver.switch_to.window(driver.window_handles[1]) # serfing - 0, vk -1
        driver.get("https://www.apple.com/ru/")
        break


general_login()
get_task_list()
# while True:
#     try:
#         general_login()
#         find_tasks(get_task_list())
#         sleep(5)
#         check_profit()
#         logging.info('выход на охоту: '+str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S')))
#     except Exception:
#         error = str('!!!выход провален: ' + str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S'))+'\n'+str(Exception))
#         logging.error(error)
#         sleep(60 * random.uniform(15, 60))  # чтоб типа как человек
