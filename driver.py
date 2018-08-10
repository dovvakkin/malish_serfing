from pyvirtualdisplay import Display
from selenium import webdriver


def driver_init():  # setup webdriver and login to target
    local_driver = webdriver.Firefox()
    display = Display(visible=1, size=[800, 800])
    display.start()
    return local_driver


driver = driver_init()


