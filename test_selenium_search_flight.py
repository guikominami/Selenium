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

    chrome_browser.get('https://www.google.com/travel/flights')

    # wait for button cookies
    button_cookies = Fc.wait_for_object(chrome_browser, By.XPATH, "//button[@aria-label='Rechazar todo']", TIME_TO_WAIT)

    #click refuse
    if button_cookies != 0:
        button_cookies.click() 

    #wait for field FROM and TO
    button_cookies = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "rIZzse", TIME_TO_WAIT)

    #find input element 
    div_master = chrome_browser.find_element(By.CLASS_NAME, "rIZzse")
    list_input_elements = div_master.find_elements(By.XPATH, ".//input")

    #discard invalid inputs
    list_filtered_elements = list(filter(lambda element: element.accessible_name != "", list_input_elements))  

    #print the list filtered
    Fc.print_list_elements(list_filtered_elements)

    #type city
    Fc.type_simple_input(list_filtered_elements[0], "São Paulo")

    input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
    input_from.click()

    #type city
    Fc.type_simple_input(list_filtered_elements[1], "Santiago")

    input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
    input_from.click()    

    sleep(50)

    # input_element[1].send_keys(Keys.CONTROL + 'A')
    # input_element[1].send_keys(Keys.DELETE)
    # input_element[1].send_keys('Santiago')

    # input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
    # input_from.click()    

    #input_element[1].send_keys(Keys.CONTROL + 'A')    

    # div_element = div_master.find_element(By.XPATH, "//div[@jsname='iOyk4d']")
    # input_element = div_element.find_element(By.XPATH, "//input[@jsname='yrriRe']")    

    # input_element.send_keys(Keys.CONTROL + 'A')
    # input_element.send_keys(Keys.DELETE)
    # input_element.send_keys('Santiago')
    # input_element.send_keys(Keys.ENTER)

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)