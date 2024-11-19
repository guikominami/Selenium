# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By

import functions as Fc
from DATA_FLIGHTS import Flights

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

def select_destination():

     #wait for the div master of the page
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "vg4Z0e", TIME_TO_WAIT)

    if div_master != 0:
        #find input element 
        div_fields = div_master.find_element(By.CLASS_NAME, "rIZzse")
        list_input_elements = div_fields.find_elements(By.XPATH, ".//input")

        #discard invalid inputs
        list_filtered_elements = list(filter(lambda element: element.accessible_name != "", list_input_elements))  

        #print the list filtered
        #Fc.print_list_elements(list_filtered_elements)

        #type city
        Fc.type_simple_input_clear(list_filtered_elements[0], "São Paulo")

        #click in the first result in list
        input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)    

        if input_from != 0:
            input_from.click()
        else:
            print("ERROR: error in select departure")
            return False

        #type city
        Fc.type_simple_input_clear(list_filtered_elements[1], "Santiago")

        #click in the first result in list
        input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)
        if input_from != 0:        
            input_from.click()            
        else:
            print("ERROR: error in select return")
            return False       
         
    else:
        print("ERROR: error in select departure")
        return False

    return True

def select_dates():

    #wait for the div master of the page
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "vg4Z0e", TIME_TO_WAIT)

    if div_master != 0:
        date_departure = div_master.find_element(By.XPATH, "//div[@jscontroller='slZO9d']")    
        date_departure.click()  

        div_calendar = div_master.find_element(By.XPATH, "//div[@jscontroller='XTf4dd']")  

        calendar = div_calendar.find_elements(By.XPATH, "//div[@role='rowgroup']")           
        Fc.print_element(calendar[0]) 

    else:
        print("error to wait div master")
        return False        
        

def click_find():

    #find button
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "MXvFbd", TIME_TO_WAIT)    
    if div_master != 0:   
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

    for data_item in Flights[0]:        

        options = ()
        chrome_browser = Fc.make_chrome_browser(link, *options)

        test = reject_cookies()

        if test == False:
            print('TEST FAILED: Reject cookies failed')
            quit()    

        test = select_destination()             

        if test == False:
            print('TEST FAILED: Select destination failed')
            quit()     

        test = select_dates()    

        if test == False:
            print('TEST FAILED: Select dates failed')
            quit()    

        # test = click_find()                       

        # if test == False:
        #     print('TEST FAILED: Click find flights failed')                   
        #     quit()   

        # Dorme por 10 segundos
        sleep(TIME_TO_WAIT)