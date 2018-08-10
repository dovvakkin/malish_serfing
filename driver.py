from pyvirtualdisplay import Display
from selenium import webdriver


def driver_init():  # setup webdriver and login to target
    _browser_profile = webdriver.FirefoxProfile()
    _browser_profile.set_preference("dom.webnotifications.enabled", False)
    local_driver = webdriver.Firefox(firefox_profile=_browser_profile)
    display = Display(visible=1, size=[800, 800])
    display.start()
    return local_driver


driver = driver_init()


