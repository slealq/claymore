from selenium import webdriver
from pyvirtualdispaly import Display
from bs4 import BeautifulSoup

def available_curses(carne, passw):
    """
    Enters ematricula.ucr.ac.cr and then
    goes to the section that has the information
    about available careers.

    This should also download the color, since
    this is how in the page you now which curses
    are available to you.
    """

    # Should use RoboBrowser or requests, but for now using Selenium
    driver = webdriver.Firefox()
    # Go to ematricula 
    driver.get('https://ematricula.ucr.ac.cr/ematricula/login.do')
    # Search for the boxes by the name and the fill them
    carne_box = driver.find_element_by_name('carne')
    pass_box = driver.find_element_by_name('pin')
    carne_box.send_keys(carne)
    pass_box.send_keys(passw)
    
    


