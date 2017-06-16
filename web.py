from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xvfbwrapper import Xvfb
from bs4 import BeautifulSoup

def available_curses(carne, passw, visible=False, close=True):
    """
    Enters ematricula.ucr.ac.cr and then
    goes to the section that has the information
    about available careers.

    Example usage:

    Launch a invisible browser and get the curses.
    -> available_curses('b53777', 'mypassword')
    
    Launch a visible browser to see step by step what is done.
    -> available_curses('b53777', 'mypassword', visible=True)

    Launch a visible browser and don't close when finished.
    -> available_curses('b53777', 'mypassword', visible=True, close=False)
    """

    # Create and start a virtualdisplay
    vdisplay = Xvfb()

    # Launch the display if visible is false
    if not visible:
        vdisplay.start()
    
    # Open the browser and do the magic
    driver = webdriver.Firefox() 
    driver.get('https://ematricula.ucr.ac.cr/ematricula/login.do')
    carne_box = driver.find_element_by_name('carne')
    pass_box = driver.find_element_by_name('pin')
    carne_box.send_keys(carne)
    pass_box.send_keys(passw)
    driver.find_element_by_name('crudMethod').click()
    wait_until_title_contains(driver, 'Sistema eMatricula')
    driver.find_element_by_link_text('Cursos Pendientes del Plan').click()
    wait_until_title_contains(driver, 'proyectoMatriculaConsulta.do')
    
    # Quit the browser
    if close:
        driver.quit()

    # If not visible, stop display
    if not visible:
        vdisplay.stop()

def wait_until_title_contains(driver, piece, timeout=10):
    """
    Helper function of available curses. 

    
    """
    try:
        # Wait until title contains...                                         
        element = WebDriverWait(driver, timeout).until(
            EC.title_contains(piece)
        )
    finally:
        # Log succesfully                                                      
        print("Loaded page that contains '"+piece+"' succesfully...")

    
