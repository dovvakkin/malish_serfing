from time import sleep


def vk_login(driver, login, password):
    driver.get("https://m.vk.com/")
    text_area = driver.find_element_by_name('email')
    text_area.send_keys(login)

    text_area = driver.find_element_by_name('pass')
    text_area.send_keys(password)

    submit = driver.find_element_by_class_name("fi_row_new")
    submit.click()


def serfing_login(driver):
    driver.get("https://vkserfing.ru")
    login = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/a[1]")
    login.click()
    sleep(3)
    try:
        driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr/td/div/div").click()
    except:
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[6]/table/tbody/tr/td/div/div").click()


def general_login(driver, login, password):
    try:
        vk_login(driver, login, password)
    except:
        pass
    try:
        serfing_login(driver)
    except:
        pass
