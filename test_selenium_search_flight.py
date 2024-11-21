# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By

import functions as Fc
from DATA_FLIGHTS import Flights

from datetime import date, timedelta

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

def select_destination(origin_city, destination_city):

     #wait for the div master of the page
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "vg4Z0e", TIME_TO_WAIT)

    if div_master != 0:
        #find input element 
        div_fields = div_master.find_element(By.CLASS_NAME, "rIZzse")
        list_input_elements = div_fields.find_elements(By.XPATH, ".//input")

        #discard invalid inputs
        list_filtered_elements = list(filter(lambda element: element.accessible_name != "", list_input_elements))  

        #type city
        Fc.type_simple_input_clear(list_filtered_elements[0], origin_city)

        #click in the first result in list
        input_from = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "zsRT0d", TIME_TO_WAIT)    

        if input_from != 0:
            input_from.click()
        else:
            print("ERROR: error in select departure")
            return False

        #type city
        Fc.type_simple_input_clear(list_filtered_elements[1], destination_city)

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

def select_dates(date_departure_days, date_return_days):

    #wait for the div master of the page
    div_master = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "vg4Z0e", TIME_TO_WAIT)

    if div_master != 0:
        date_departure_input = div_master.find_element(By.XPATH, "//div[@jscontroller='slZO9d']")    
        date_departure_input.click()  

    else:
        print("error to wait div master")
        return False           

    #calendar opened
    div_calendar_master = Fc.wait_for_object(div_master, By.CLASS_NAME, "SJyhnc", TIME_TO_WAIT)
    if div_calendar_master != 0:
        div_calendar = div_calendar_master.find_element(By.XPATH, "//div[@jscontroller='XTf4dd']")  
        div_actual_month = div_calendar.find_element(By.XPATH, "//div[@role='rowgroup']")        
    else:
        print("ERROR: Can't open the calendar.")
        return False    

    date_departure = (date.today() + timedelta(days=date_departure_days))
    date_return = (date.today() + timedelta(days=date_return_days))
    print("date_departure:", date_departure)
    print("date_return:", date_return)        

    #date departure
    day = div_actual_month.find_element(By.XPATH, "//div[@data-iso='" + str(date_departure) + "']")
    day.click()

    #date destination
    day = div_actual_month.find_element(By.XPATH, "//div[@data-iso='" + str(date_return) + "']")
    day.click()        

    #identify button done
    div_button = Fc.wait_for_object(chrome_browser, By.XPATH, "//div[@jsname='WCieBd']", TIME_TO_WAIT)
    if div_button != 0:        
        button_done = div_button.find_elements(By.XPATH, ".//button")        
        button_done[0].click() 
    else:
        print("ERROR: Can't click the button open.")
        return False                

    return True       

def select_cheap_dates():
        date_departure = div_master.find_element(By.XPATH, "//div[@jscontroller='slZO9d']")    
        date_departure.click()  

        div_calendar = div_master.find_element(By.XPATH, "//div[@jscontroller='XTf4dd']")  
        
        #a partir de duas datas, procurar as datas maiss barata de inicio e fim com 1 gap de 1 semana pra frente e uma pra tras 

         #calendar = div_calendar.find_elements(By.XPATH, "//div[@role='rowgroup']")        

        #actual_month = calendar[0].find_element(By.XPATH, "//div[@jsname='Mgvhmd']")   

        #days = actual_month.find_elements(By.XPATH, "//div[@jsname='nEWxA']")             
        

def click_search_flights():

    #identify button serach
    div_button = Fc.wait_for_object(chrome_browser, By.CLASS_NAME, "xFFcie", TIME_TO_WAIT)
    if div_button != 0:        
        button_search = div_button.find_elements(By.XPATH, ".//button")        
        button_search[0].click() 
    else:
        print("ERROR: Can't click the button search.")
        return False       

    return True    

if __name__ == '__main__':
    TIME_TO_WAIT = 2

    link = 'https://www.google.com/travel/flights'

    for data_item in Flights[0]:        

        options = ()
        chrome_browser = Fc.make_chrome_browser(link, *options)

        test = reject_cookies()

        if test == False:
            print('TEST FAILED: Reject cookies failed.')
            quit()    

        test = select_destination(data_item['departure_city'], data_item['destination_city'])             

        if test == False:
            print('TEST FAILED: Select destination failed.')
            quit()     

        test = select_dates(data_item['date_departure'], data_item['date_return'])    

        if test == False:
            print('TEST FAILED: Select dates failed.')
            quit()    

        test = click_search_flights()

        if test == False:
            print('TEST FAILED: Click search flights failed.')
            quit()    

        # Dorme por 10 segundos
        sleep(TIME_TO_WAIT)

        chrome_browser.quit()