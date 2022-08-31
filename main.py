import time
import Base

Base.Base.navigate('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
Base.Base.write_input('//input[contains(@name,"username")]','Admin')
Base.Base.write_input('//input[contains(@name,"password")]','admin123')
Base.Base.click('//button[contains(@class,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")]')
time.sleep(5)
Base.Base.cerrar_navegador()



