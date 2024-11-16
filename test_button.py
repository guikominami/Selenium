# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import functions as Fc

if __name__ == '__main__':
    TIME_TO_WAIT = 5

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    chrome_browser = Fc.make_chrome_browser(*options)
    chrome_browser.maximize_window()
    chrome_browser.get('https://www.google.com/travel/flights')

    #find input element 
    div_master = chrome_browser.find_element(By.CLASS_NAME, "lssxud")    
    button_reject = div_master.find_elements(By.XPATH, ".//button")    

    #Fc.print_list_elements(button_reject)

    button_reject[0].click()
   
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)