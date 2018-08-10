from driver import driver
from datetime import datetime

def debug_screenshot(function_name):
    folder = '/Users/dovvakkin/github/screenshot_logs/'
    screenshot_path = folder+function_name+str(datetime.now().strftime('%Y_%m_%d_%H:%M:%S'))+".png"
    driver.save_screenshot(screenshot_path)
