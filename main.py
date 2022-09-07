import time
import Base
import variables
'''
#Base.Base.navigate('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#Base.Base.write_input('//input[contains(@name,"username")]','Admin')
#Base.Base.write_input('//input[contains(@name,"password")]','admin123')
#Base.Base.click('//button[contains(@class,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")]')
#time.sleep(5)

'''

'''
Base.Base.navigate('https://demoqa.com/text-box')
Base.Base.write_input('//input[@id="userName"]', 'Jhon Quisperson')
Base.Base.write_input('//input[@id="userEmail"]', 'jquisperson@gmail.com')
Base.Base.write_input("//textarea[@id='currentAddress']",'Jiron Junin 1001, Lima - Peru')
Base.Base.write_input("//textarea[@id='permanentAddress']"," CAgua-Aragua, Venezuela")
Base.Base.click("//button[@id='submit']")

'''
'''checkbox'''
Base.navigate(variables.direccion)
Base.click("//span[contains(text(),'Home')]")
Base.click("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/ol[1]/li[1]/span[1]/button[1]/*[1]") # click en flecha de expandir

'''END'''
time.sleep(5)
Base.cerrar_nav()
'''
Base.Base.Base.cerrar_navegador()

driver.switch_to.frame("packageListFrame")

driver.find_element_by_link_text("org.openqa.selenium.opera").click()

driver.switch_to.default_content()

'''


