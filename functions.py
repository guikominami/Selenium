from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    browser = webdriver.Chrome(
        options=chrome_options
    )

    return browser

def wait_for_object(browser, type, description, time):
    try:
        element = WebDriverWait(browser, time).until(
            EC.presence_of_element_located(
                (type, description)
            )
        )    
        return element    
    except RuntimeError:
        print("element not found")
        return 0
    
def print_list_elements(list_of_elements):
    for element in list_of_elements:
        print("ELEMENT:")   
        print("role: " + element.aria_role)
        print("accessible name: " + element.accessible_name)
        print("ID: " + element.id)
        print("tag name: " + element.tag_name)
        print("text: " + element.text)        
        print("")
        print("")           

def type_simple_input(input_field, value):
    input_field.send_keys(Keys.CONTROL + 'A')
    input_field.send_keys(Keys.DELETE)
    input_field.send_keys(value)
    input_field.send_keys(Keys.TAB)    