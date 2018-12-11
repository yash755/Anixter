from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import json
from bs4 import BeautifulSoup
import pymysql.cursors
import os.path


def get_list():
	# url = 'https://www.anixter.com/en_us/login.html'
	# 						driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
	# 						driver.maximize_window()
	# 						driver.get(url)
	# 						time.sleep(2)
	# 						name = driver.find_element_by_name('ctl00$PlaceHolderMain$ctl00$ctlLoginView$MainLoginView$MainLogin$UserName')
	# 						name.send_keys('KASE2046')
	# 						password = driver.find_element_by_name('ctl00$PlaceHolderMain$ctl00$ctlLoginView$MainLoginView$MainLogin$Password')
	# 						password.send_keys('Prodsupp17')
	# 						driver.find_element_by_id("ctl00_PlaceHolderMain_ctl00_ctlLoginView_MainLoginView_MainLogin_LoginButton").click()
	# 						time.sleep(2)
	# 						driver.get(pageURL)
	try:
		options = Options()
		options.set_headless(headless=True)
		driver = webdriver.Chrome(options=options, executable_path='/Users/yashgupta/Desktop/chromedriver')
		driver.get("https://www.anixter.com/en_us/login.html")
		driver.save_screenshot('login.png')
		name = driver.find_element_by_id('j_username')
		name.send_keys('e733733@gmail.com')
		password = driver.find_element_by_id('j_password')
		password.send_keys('ProdSupp9737')
		driver.find_element_by_xpath("//*[@class='positive button primary-large']").click()
		driver.get('https://www.anixter.com/en_us/products/Electrical-Wire-and-Cable/c/GROUP_EW?q=%3Arelevance&page=131&op=')
		driver.save_screenshot('test.png')

		print ("Hello")
		

		html2 = driver.page_source
		soup = BeautifulSoup(html2, "lxml", from_encoding="utf-8")

		products = soup.find_all('div',{'class':'product-tile-tertiary row'})
		for product in products:
			para = product.find('p',{'class':'title-primary'})
			print (para)
			if para:
				print (para.find('a'))

		driver.quit()

	

	except Exception as e:
		print(e)
		print("Loop1...")
		time.sleep(2)
		print("Was a nice sleep, now let me continue...")
		

if __name__ == '__main__':
	get_list()