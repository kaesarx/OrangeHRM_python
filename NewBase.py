from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (presence_of_element_located)

    AAA: WebDriver = webdriver.Chrome('chromedriver.exe')
    wait_d = WebDriverWait(AAA, 10)

    def navigate(url):
        AAA.get(url)

    def find(locatorN):
        return  wait_d.until(presence_of_element_located((By.XPATH, locatorN)))

    def write_input(locatorNN, texto):
        wait_d.until(presence_of_element_located((By.XPATH, locatorNN))).clear()
        wait_d.until(presence_of_element_located((By.XPATH, locatorNN))).send_keys(texto)

    def click(locatorNNN):
        wait_d.until(presence_of_element_located((By.XPATH, locatorNNN))).click()