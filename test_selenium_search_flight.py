# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import functions as Fc
from test_data_flights import Flights as Data_Flights

def reject_cookies():
    # wait for button cookies  
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "lssxud", TIME_TO_WAIT)

    #identify button reject
    button_reject_cookies = div_master.find_elements(By.XPATH, ".//button")    

    #click refuse
    if button_reject_cookies != 0:
        button_reject_cookies[0].click() 
    else:
        return False

    return True

def select_departure_destination():

    #wait for field FROM and TO
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "vg4Z0e", TIME_TO_WAIT)

    if div_master != 0:
        #find input element 
        div_fields = div_master.find_element(By.CLASS_NAME, "rIZzse")
        list_input_elements = div_fields.find_elements(By.XPATH, ".//input")

        #discard invalid inputs
        list_filtered_elements = list(filter(lambda element: element.accessible_name != "", list_input_elements))  

        #print the list filtered
        Fc.print_list_elements(list_filtered_elements)

        #type city
        Fc.type_simple_input_clear(list_filtered_elements[0], "São Paulo")

        #click in the first result in list
        input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)    

        if input_from != 0:
            input_from.click()
        else:
            print("error in select departure")
            return False

        #type city
        Fc.type_simple_input_clear(list_filtered_elements[1], "Santiago")

        #click in the first result in list
        input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
        if input_from != 0:        
            input_from.click()            
        else:
            print("error in select return")
            return False       
         
    else:
        print("error in select departure")
        return False

    return True

def click_find():

    #find button
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "MXvFbd", TIME_TO_WAIT)    
    if div_button != 0:   
        #div_button = div_master.find_element(By.CLASS_NAME, "MXvFbd")
        button_search = div_master.find_elements(By.XPATH, ".//button")    
        button_search[0].click()    
    else:
        print("error to wait button find")
        return False
    
    return True    

if __name__ == '__main__':
    TIME_TO_WAIT = 5

    link = 'https://www.google.com/travel/flights'

    for data_item in Data_Flights[0]:        

        options = ()
        chrome_browser = Fc.make_chrome_browser(link, *options)

        test_passed = reject_cookies()

        if test_passed == True:
            test_passed = select_departure_destination()
        else:
            print('Reject cookies failed')
            quit()     

        if test_passed == True:
            test_passed = click_find()
        else:
            print('select return failed')
            quit()   

        if test_passed == False:
            print('Click failed')                   
        
        # Dorme por 10 segundos
        sleep(TIME_TO_WAIT)