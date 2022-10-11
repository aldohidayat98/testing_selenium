# Import Plugin Selenium =============================================
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #Di Gunakan untuk By.CSS_SELECTOR/XPATH
from selenium import webdriver
import time

# Deklarasi webdriver & Tampilan Windows Maksimal ====================
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://10.38.3.25/login/login.jsp')
driver.find_element('name','j_username').send_keys('ald')
driver.find_element('name','j_password').send_keys('ald' + Keys.ENTER)


driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&length=3600000&device=10.68.68.2&if=10.68.68.2%2F19&format=ajax&reload=60&chartTitle=Traffic+Rate'+'&stime=1665014400000&etime=1665057600000&sample_nunits=1&sample_unit=minute')
driver.set_window_size(782, 768)
time.sleep(1)

element = driver.find_element('name','rep_form')
element.screenshot('7-OKTOBER-2022_WBCA-WAN-IPSEC2_traffic.png') 


time.sleep(2)
driver.quit()   



# Delay 5 Detik ======================================================
# -------------------------------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# driver.find_element('name','q').send_keys('Aldo Hidayat' + Keys.ENTER)
# assert 'Aldo Hidayat','Aldo' in driver.find_element(By.CSS_SELECTOR,'h3').text
# assert 'Aldo Hidayat' in driver.title