from time import sleep
from driver import driver


VK_LOGIN = '89258396534'
VK_PASSWORD = 'k0zhepnin@'

TARGET_LOGIN = "MariaKozevnikov@gmail.com"
TARGET_PASSWORD = "k0zhepnin@"


def vk_login():
    driver.get("https://m.vk.com/")
    text_area = driver.find_element_by_name('email')
    text_area.send_keys(VK_LOGIN)

    text_area = driver.find_element_by_name('pass')
    text_area.send_keys(VK_PASSWORD)

    submit = driver.find_element_by_class_name("fi_row_new")
    submit.click()


def serfing_login():
    driver.get("https://vkserfing.ru")
    login = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/a[1]")
    login.click()
    sleep(3)
    try:
        driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr/td/div/div").click()
    except:
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr/td/div/div").click()


def general_login():
    try:
        vk_login()
    except:
        pass
    try:
        serfing_login()
    except:
        pass


if __name__ == "__main__":
    general_login()
