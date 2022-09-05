from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (presence_of_element_located)
from selenium.webdriver.support.ui #import (Select)

class Base:
    navegador = webdriver.Chrome('chromedriver.exe')
    wait_d = WebDriverWait(navegador, 10)

    def navigate( url):
        Base.navegador.get(url)

    def find( locator):
        Base.wait_d.until(presence_of_element_located((By.XPATH, locator)))

    def write_input( locator, texto):
        Base.wait_d.until(presence_of_element_located((By.XPATH, locator))).clear()
        Base.wait_d.until(presence_of_element_located((By.XPATH, locator))).send_keys(texto)

    def click( locator):
        Base.wait_d.until(presence_of_element_located((By.XPATH, locator))).click()

    def cerrar_navegador():
        Base.navegador.quit()

    def switch_frame(frame):
        Base.wait_d.until(presence_of_element_located((By.XPATH, frame)))
        Base.navegador.switch_to_frame(frame)

    ##generador random de caracteres en inputs
    ##contador de caracteres en inputs