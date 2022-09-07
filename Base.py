import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (presence_of_element_located)
#from selenium.webdriver.support.ui import (Select)


# class Base(unittest.TestCase):
navegador = webdriver.Chrome('chromedriver.exe')
wait_d = WebDriverWait(navegador, 10)


def navigate(url):
    navegador.get(url)


def find(locator):
    wait_d.until(presence_of_element_located((By.XPATH, locator)))


def write_input(locator, texto):
    wait_d.until(presence_of_element_located((By.XPATH, locator))).clear()
    wait_d.until(presence_of_element_located((By.XPATH, locator))).send_keys(texto)


def click(locator):
    wait_d.until(presence_of_element_located((By.XPATH, locator))).click()


def cerrar_nav():
    navegador.quit()


def switch_frame(frame):
    wait_d.until(presence_of_element_located((By.XPATH, frame)))
    navegador.switch_to_frame(frame)

##generador random de caracteres en inputs
##contador de caracteres en inputs
