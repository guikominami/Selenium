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

    # wait for button cookies
    button_cookies = Fc.wait_for_object(chrome_browser, By.XPATH, "//button[@aria-label='Rechazar todo']", TIME_TO_WAIT)

    #click refuse
    if button_cookies != 0:
        button_cookies.click() 

    #wait for field FROM and TO
    button_cookies = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "rIZzse", TIME_TO_WAIT)

    #find input element 
    div_master = chrome_browser.find_element(By.CLASS_NAME, "vg4Z0e")    
    div_fields = div_master.find_element(By.CLASS_NAME, "rIZzse")
    list_input_elements = div_master.find_elements(By.XPATH, ".//input")

    #discard invalid inputs
    list_filtered_elements = list(filter(lambda element: element.accessible_name != "", list_input_elements))  

    #print the list filtered
    #Fc.print_list_elements(list_filtered_elements)

    #type city
    Fc.type_simple_input(list_filtered_elements[0], "São Paulo")

    #click in the first result in list
    input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
    input_from.click()

    #type city
    Fc.type_simple_input(list_filtered_elements[1], "Santiago")

    #click in the first result in list
    input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
    input_from.click()    

    #find button
    div_button = div_master.find_element(By.CLASS_NAME, "MXvFbd")
    button_search = div_button.find_elements(By.XPATH, ".//button")    
    Fc.print_list_elements(button_search)
    button_search[0].click()
    
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)