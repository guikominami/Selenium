# -------------------------------------------------------------------------------------------------------
# This script books an appointment (cita) in a spanish government website to receive the foreigners card
# -------------------------------------------------------------------------------------------------------
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import functions as Fc
from DATA_CITAS import citas

def submit_process():
    # wait for button cookies
    button_submit = Fc.wait_for_object(chrome_browser, By.ID, "submit", TIME_TO_WAIT)

    #click refuse
    if button_submit != 0:
        button_submit.click() 
    else:
        return False

    return True        

def select_province(province):

    div_provincias = Fc.wait_for_object(chrome_browser, By.ID, "divProvincias", TIME_TO_WAIT)
    select = Select(div_provincias.find_element(By.NAME, "form"))
    select.select_by_visible_text(province)

    button_accept = Fc.wait_for_object(chrome_browser, By.ID, "btnAceptar", TIME_TO_WAIT)    
    
    if button_accept != 0:
        button_accept.click()
    else:
        return False
    
    return True

def select_place(place):

    form_main = Fc.wait_for_object(chrome_browser, By.ID, "portadaForm", TIME_TO_WAIT)

    div_oficinas = Fc.wait_for_object(form_main, By.ID, "divSedes", TIME_TO_WAIT)

    if div_oficinas != 0:
        select = Select(div_oficinas.find_element(By.NAME, "sede"))
        select.select_by_visible_text(place)    
    else:
        return False
    
    return True    

def select_task(task):

    #wait for div because variables according with the local selected before
    div_tramites = Fc.wait_for_object(chrome_browser, By.ID, "divGrupoTramites", TIME_TO_WAIT)

    if div_tramites != 0:
        select_tramite = Select(div_tramites.find_element(By.NAME, "tramiteGrupo[0]"))    
        select_tramite.select_by_visible_text(task)  
    else:
        print("ERROR: tramite nao encontrado")        
        return False        

    link_cookies = Fc.wait_for_object(chrome_browser, By.ID, "cookie_action_close_header", TIME_TO_WAIT)   
    if link_cookies != 0:    
        link_cookies.click()       

    div_form = Fc.wait_for_object(chrome_browser, By.ID, "portadaForm", TIME_TO_WAIT)
    button_accept = Fc.wait_for_object(div_form, By.ID, "btnAceptar", TIME_TO_WAIT)    
    button_accept = div_form.find_element(By.ID, "btnAceptar")
    if button_accept != 0:
        button_accept.click()
    else:
        print("ERROR: botão aceitar nao encontrado")        
        return False  
    
    return True      

def select_key_type():    

    button_no_key = Fc.wait_for_object(chrome_browser, By.ID, "btnEntrar", TIME_TO_WAIT)    

    if button_no_key != 0:
        #the button is not ckickable. We have to find links (p) inside the component "btnEntrar"
        link_no_key = button_no_key.find_elements(By.XPATH, ".//p")        
        link_no_key[0].click()
    else:
        print("ERROR: botão aceitar nao encontrado")        
        return False       

    return True          
            

def type_personal_data(nie, name, country):
    div_master = Fc.wait_for_object(chrome_browser, By.ID, "divIdCitado", TIME_TO_WAIT)   
    input_nie = Fc.wait_for_object(div_master, By.ID, "txtIdCitado", TIME_TO_WAIT)     
    
    if input_nie != 0:        
        Fc.type_simple_input_clear(input_nie, nie)    

    div_master = Fc.wait_for_object(chrome_browser, By.ID, "divDesCitado", TIME_TO_WAIT)   
    input_name = Fc.wait_for_object(div_master, By.ID, "txtDesCitado", TIME_TO_WAIT)         

    if input_name != 0:
        Fc.type_simple_input_clear(input_name, name)             

    div_master = Fc.wait_for_object(chrome_browser, By.ID, "divPaisNac", TIME_TO_WAIT)     
    if div_master != 0:
        select_country = Select(div_master.find_element(By.NAME, "txtPaisNac"))           
        select_country.select_by_visible_text(country)   

        button_send = Fc.wait_for_object(chrome_browser, By.ID, "btnEnviar", TIME_TO_WAIT)        
        if button_send != 0:
            button_send.click()

    return True                 

def book_quote():
    div_master = Fc.wait_for_object(chrome_browser, By.ID, "btn", TIME_TO_WAIT)   
    if div_master != 0:      
        button_send = Fc.wait_for_object(div_master, By.ID, "btnEnviar", TIME_TO_WAIT)  
        button_send.click()   
    else:
        print("ERROR: There isn't quotes available!")
        div_master = Fc.wait_for_object(chrome_browser, By.NAME, "info", TIME_TO_WAIT)        
        button_accept = Fc.wait_for_object(div_master, By.ID, "btnSubmit", TIME_TO_WAIT)  
        if button_accept != 0:   
            button_accept.click()

    return True                 

if __name__ == '__main__':
    TIME_TO_WAIT = 15
    TIME_SLEEP = 10

    link = 'https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus'

    for data_item in citas:       
        # Example
        # options = '--headless', '--disable-gpu',
        chrome_browser = Fc.make_chrome_browser(link)

        test_result = submit_process() 

        if test_result == False:
            print('TEST FAILED: Submit process failed.')
            quit()               

        test_result = select_province(data_item['provincia'])

        if test_result == False:
            print('TEST FAILED: Select province failed.')          
            quit()                

        test_result = select_place(data_item['oficina'])               

        if test_result == False:
            print('TEST FAILED: Select place failed.')          
            quit()                                   

        test_result = select_task(data_item['tramite_policia'])

        if test_result == False:
            print('TEST FAILED: Select task failed.')          
            quit()                                

        if test_result == False:
            print('TEST FAILED: Select key type failed.')          
            quit()      

        test_result = select_key_type()                                    

        if test_result == False:
            print('TEST FAILED: Select oficinas failed.')         
            quit()                

        test_result = type_personal_data(data_item['nie'], data_item['name'], data_item['country'])

        if test_result == False:
            print('TEST FAILED: Type personal data failed.')     
            quit()     

        test_result = book_quote()                                  

        if test_result == False:                    
            print('TEST FAILED: Book quote failed.')      
            quit()                  

        # Dorme por 10 segundos
        sleep(TIME_TO_WAIT)