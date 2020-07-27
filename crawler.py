from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
from pprint import pprint
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")



driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://outagemap.coned.com/external/default.html")

imagesInViewPortXPath = '/html/body/div[7]/div[3]/div/div/div[1]/div[3]/div/div[3]'
addressXPath = '/html/body/div[7]/section[1]/div/div[2]/div[2]/div[2]/span[2]/span[2]'

WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div/div/div[1]/div[3]/div/div[3]/div[1]/img')))

restoreElemment = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/ul/li[4]/button/span')))

outrageImages = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, imagesInViewPortXPath)))


#for ele in outrageImages:
    #print(ele.get_attribute('innerHTML'))
print(outrageImages.get_attribute("innerHTML"))

CrawlStatus = {}

print(type(outrageImages))

#print(outrageImages[0].get_attribute('innerHTML'))

outrageImages = outrageImages.find_elements_by_tag_name('img');
print(len(outrageImages))
for ele in outrageImages:
    print(ele.get_attribute('src'))
    #below are extract for each image, but we have flaws:
    # 1. Cond map is interactive map, the data will change as user action changes, for example, if we continue magnify the elements on the page, other data will removed from the page
    #so at an edge case, we may not be able to catch all addresses.
    # 2. the html is pretty complicated, we are working days and nights to do experiments and testing  
    

url = outrageImages[0].get_attribute('src')
while 'premise/premises_rep' not in url:
    outrageImages[0].click()
    zoomEle = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="info-box-zoom"]')))
    zoomEle.click()
    time.sleep(3)
    outrageImages = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, imagesInViewPortXPath))).find_elements_by_tag_name('img');
    url = outrageImages[0].get_attribute('src')
	



# show right slide and extract address
outrageImages[0].click()
print(WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, addressXPath))).get_attribute('innerHTML'))


#recover to origina page state
#restoreElemment = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/ul/li[4]/button/span')))
#restoreElemment.click()


# inputElement.send_keys('New York City')
# inputElement.send_keys(Keys.ENTER)
# #driver.find_element_by_id("address_submit").submit()


# element_present = EC.presence_of_element_located((By.ID, 'load_more_facilities'))
# WebDriverWait(driver, 10000).until(element_present)

# #python_button = driver.find_elements_by_id("load_more_facilities")
# #python_button.click()

# for i in range(10):
#     driver.execute_script("document.getElementsByClassName('facility_wrapper')[" + str(i) + "].style.display = 'block';")
    
# list_of_elements = driver.find_elements_by_css_selector('p.p-b-5')

# print("len is :" + str(len(list_of_elements)))
# result = []
# for i in list_of_elements:
#     if ('NY' in  i.text.strip()):
#         site={}
#         site['address'] = i.text.strip()
#         print(site['address'])
#         result.append(site)

# f = open('results-final.csv', 'wb')

# with f:
#     fnames = ['address']
#     writer = csv.DictWriter(f, fieldnames=fnames) 
#     writer.writeheader()
#     for row in result:
# 	    writer.writerow(row)


# for i in range(3):
# 	#driver.execute_script("window.scrollTo(0, Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight));")
#     element = driver.find_element_by_id("load_more_facilities")
#     driver.execute_script("arguments[0].scrollIntoView();", element)
#     time.sleep(4)
#     driver.find_element_by_id("load_more_facilities").click()
#     print("clicked " + str(i + 1) + " time")
#     #element.click()
#     time.sleep(4)
#     #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
#     driver.execute_script("scrollBy(0,250);")



driver.close()