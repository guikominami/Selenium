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
from test_data import Citas as Data_Citas
 
def select_province(province):

    # wait for button cookies
    button_submit = Fc.wait_for_object(chrome_browser, By.ID, "submit", TIME_TO_WAIT)

    #click refuse
    if button_submit != 0:
        button_submit.click() 

    div_provincias = Fc.wait_for_object(chrome_browser, By.ID, "divProvincias", TIME_TO_WAIT)
    select = Select(div_provincias.find_element(By.NAME, "form"))
    select.select_by_visible_text(province)

    button_accept = Fc.wait_for_object(chrome_browser, By.ID, "btnAceptar", TIME_TO_WAIT)    
    
    if button_accept != 0:
        button_accept.click()

def select_oficinas(oficina, tramite):

    form_main = Fc.wait_for_object(chrome_browser, By.ID, "portadaForm", TIME_TO_WAIT)

    div_oficinas = Fc.wait_for_object(form_main, By.ID, "divSedes", TIME_TO_WAIT)
    select = Select(div_oficinas.find_element(By.NAME, "sede"))
    select.select_by_visible_text(oficina)    

    #wait for div because variables according with the local selected before
    div_tramites = Fc.wait_for_object(chrome_browser, By.ID, "divGrupoTramites", TIME_TO_WAIT)

    if div_tramites != 0:
        select = Select(div_tramites.find_element(By.NAME, "tramiteGrupo[0]"))    
        select.select_by_visible_text(tramite)  
    else:
        print("tramite nao encontrado")

    select.send_keys(Keys.TAB)    
    sleep(10)

   # button_accept = Fc.wait_for_object(chrome_browser, By.ID, "btnAceptar", TIME_TO_WAIT)    
    button_accept = chrome_browser.find_element(By.ID, "btnAceptar")
    #if button_accept != 0:
    #    button_accept.click()
    Fc.print_list_elements(button_accept)    

    button_no_key = Fc.wait_for_object(chrome_browser, By.ID, "btnEntrar", TIME_TO_WAIT)    
    Fc.print_list_elements(button_no_key)
    # if button_no_key != 0:
        

if __name__ == '__main__':
    TIME_TO_WAIT = 55

    link = 'https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus'


    for data_item in Data_Citas[0]:
        print (data_item['oficina'])
        
        # Example
        # options = '--headless', '--disable-gpu',
        options = ()
        chrome_browser = Fc.make_chrome_browser(link, *options)

        select_province(data_item['provincia'])

        select_oficinas(data_item['oficina'], data_item['tramite_policia'])

        # Dorme por 10 segundos
        sleep(TIME_TO_WAIT)