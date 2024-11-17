# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import functions as Fc

if __name__ == '__main__':
    TIME_TO_WAIT = 55

    # Example
    options = ()
    chrome_browser = Fc.make_chrome_browser('https://www.google.com', *options)

    #identify button reject
    button_reject_cookies = Fc.wait_for_object(chrome_browser, By.ID, "W0wltc", TIME_TO_WAIT)  

    #click refuse
    if button_reject_cookies != 0:    
        button_reject_cookies.click() 

    # wait for input
    input_search = Fc.wait_for_object(chrome_browser, By.NAME, "q", TIME_TO_WAIT)

    if input_search != 0:
        input_search.send_keys('Hello World!')
        input_search.send_keys(Keys.ENTER)

    results = chrome_browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    print(links[0])
    links[0].click()

    # Dorme por 10 segundos
    #sleep(TIME_TO_WAIT)