from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (presence_of_element_located)

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