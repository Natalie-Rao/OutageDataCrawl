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

# open the page
driver.get("https://outagemap.coned.com/external/default.html")

# get the legend Xpath
imagesInViewPortXPath = '/html/body/div[7]/div[3]/div/div/div[1]/div[3]/div/div[3]'
# get the address
addressXPath = '/html/body/div[7]/section[1]/div/div[2]/div[2]/div[2]/span[2]/span[2]'

# wait for 4 seconds until the icons show up --- get the intial stage
WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[3]/div/div/div[1]/div[3]/div/div[3]/div[1]/img')))

# return to the intial stage
restoreElemment = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/ul/li[4]/button/span')))

outageImages = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, imagesInViewPortXPath)))

# get the HTML structure of icons 
print(outageImages.get_attribute("innerHTML"))

#CrawlStatus = {}
#print(type(outageImages))

# find the image button to click 
outageImages = outageImages.find_elements_by_tag_name('img');
print(len(outageImages))
for ele in outageImages:
    print(ele.get_attribute('src')) # print the URL of each image for debug 
    

# click the image until the the expected image shows up
url = outageImages[0].get_attribute('src')
while 'premise/premises_rep' not in url:
    outageImages[0].click()
    zoomEle = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="info-box-zoom"]')))
    zoomEle.click()
    time.sleep(3)
    outageImages = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, imagesInViewPortXPath))).find_elements_by_tag_name('img');
    url = outageImages[0].get_attribute('src')


# Extract address
outageImages[0].click()
print(WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, addressXPath))).get_attribute('innerHTML'))



    '''
    Challenge: The problem complexity will be how to mimic human behavior with selenium to wait the address show up, 
    I have extracted successfully one address with selenium library. The next step for me is to loop each cluster outage area to extract address.
    We need to created a hashtable to store the image Xpath from multiple laywers. However, the HTML changes from lawyers to lawyers. 
    
    '''


#recover to origina page state
#restoreElemment = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/ul/li[4]/button/span')))
#restoreElemment.click()



# f = open('results-final.csv', 'w')

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