# Import Plugin Selenium =============================================
from distutils.log import info
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #Di Gunakan untuk By.CSS_SELECTOR/XPATH
from selenium import webdriver
import json
import time

# Deklarasi webdriver & Tampilan Windows Maksimal ====================
driver = webdriver.Chrome()
driver.maximize_window()
file_json = open("info.json")
data =  json.loads(file_json.read())
epoc = data['epoc']
date = data['date']

# Login ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
driver.get('http://10.38.3.25/login/login.jsp')
driver.find_element('name','j_username').send_keys('ald')
driver.find_element('name','j_password').send_keys('ald' + Keys.ENTER)

# BCALC1 - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.68.68.2&if=10.68.68.2%2F19&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/BCALC1/2022/Oktober/'+str(date)+'-2022_BCALC1-WAN-IPSEC1_traffic.png') 

# BCALC1 - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.68.68.3&if=10.68.68.3%2F19&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/BCALC1/2022/Oktober/'+str(date)+'-2022_BCALC1-WAN-IPSEC2_traffic.png') 

# BSD - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.63.140.3&if=10.63.140.3%2F14&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/BSD/2022/Oktober/'+str(date)+'-2022_BSD-WAN-IPSEC1_traffic.png') 

# BSD - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.63.140.4&if=10.63.140.4%2F14&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/BSD/2022/Oktober/'+str(date)+'-2022_BSD-WAN-IPSEC2_traffic.png') 

# CPC - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.64.0.29&if=10.64.0.29%2F14&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/CPC/2022/Oktober/'+str(date)+'-2022_CPC-WAN-IPSEC1_traffic.png') 

# CPC - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.64.0.30&if=10.64.0.30%2F14&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/CPC/2022/Oktober/'+str(date)+'-2022_CPC-WAN-IPSEC2_traffic.png') 

# FOR - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.61.0.1&if=10.61.0.1%2F14&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/FOR/2022/Oktober/'+str(date)+'-2022_FOR-WAN-IPSEC1_traffic.png') 

# FOR - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.61.0.2&if=10.61.0.2%2F14&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/FOR/2022/Oktober/'+str(date)+'-2022_FOR-WAN-IPSEC2_traffic.png') 

# GSW - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.70.4.1&if=10.70.4.1%2F11&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/GSW/2022/Oktober/'+str(date)+'-2022_GSW-WAN-IPSEC1_traffic.png') 

# GSW - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.70.4.2&if=10.70.4.2%2F11&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/GSW/2022/Oktober/'+str(date)+'-2022_GSW-WAN-IPSEC2_traffic.png') 

# HSB - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.66.128.1&if=10.66.128.1%2F13&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/HSB/2022/Oktober/'+str(date)+'-2022_HSB-WAN-IPSEC1_traffic.png') 

# HSB - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.66.128.2&if=10.66.128.2%2F13&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/HSB/2022/Oktober/'+str(date)+'-2022_HSB-WAN-IPSEC2_traffic.png') 

# JDL - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.70.0.1&if=10.70.0.1%2F11&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/JDL/2022/Oktober/'+str(date)+'-2022_JDL-WAN-IPSEC1_traffic.png') 

# JDL - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.70.0.2&if=10.70.0.2%2F11&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/JDL/2022/Oktober/'+str(date)+'-2022_JDL-WAN-IPSEC2_traffic.png') 

# LMP - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.69.0.29&if=10.69.0.29%2F12&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/LMP/2022/Oktober/'+str(date)+'-2022_LMP-WAN-IPSEC1_traffic.png') 

# LMP - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.69.0.30&if=10.69.0.30%2F13&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/LMP/2022/Oktober/'+str(date)+'-2022_LMP-WAN-IPSEC2_traffic.png')

# TCM - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.70.8.1&if=10.70.8.1%2F9&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/TCM/2022/Oktober/'+str(date)+'-2022_TCM-WAN-IPSEC1_traffic.png') 

# TCM - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.70.8.2&if=10.70.8.2%2F9&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/TCM/2022/Oktober/'+str(date)+'-2022_TCM-WAN-IPSEC2_traffic.png') 

# WBCA - IPSEC1
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.60.31.29&if=10.60.31.29%2F12&chartTitle=Traffic+Rate'+str(epoc))
driver.set_window_size(782, 768)
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/WBCA-PI/2022/Oktober/'+str(date)+'-2022_WBCA-WAN-IPSEC1_traffic.png') 

# WBCA - IPSEC2
driver.get('http://10.38.3.25/report.jsp?templid=_if&output=chart&device=10.60.31.30&if=10.60.31.30%2F12&chartTitle=Traffic+Rate'+str(epoc))
time.sleep(1)
element = driver.find_element('name','rep_form')
element.screenshot('./Capture link IP Sec/WBCA-PI/2022/Oktober/'+str(date)+'-2022_WBCA-WAN-IPSEC2_traffic.png') 


time.sleep(2)
driver.quit()   


# -------------------------------------------------------------------------------------------
# from selenium.webdriver.common.by import By
# driver.find_element('name','q').send_keys('Aldo Hidayat' + Keys.ENTER)
# assert 'Aldo Hidayat','Aldo' in driver.find_element(By.CSS_SELECTOR,'h3').text
# assert 'Aldo Hidayat' in driver.title