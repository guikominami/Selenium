# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import functions as Fc

if __name__ == '__main__':
    TIME_TO_WAIT = 5

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    chrome_browser = Fc.make_chrome_browser(*options)
    chrome_browser.maximize_window()
    chrome_browser.get('https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus')

    # wait for button cookies
    button_submit = Fc.wait_for_object(chrome_browser, By.ID, "submit", TIME_TO_WAIT)

    #click refuse
    if button_submit != 0:
        button_submit.click() 

    select_provincias = Fc.wait_for_object(chrome_browser, By.ID, "form", TIME_TO_WAIT)  

    select = Select(chrome_browser.find_element(By.ID, "form"))

    select.select_by_visible_text("Albacete")

    # # select by visible text
    # select.select_by_index(0)

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)