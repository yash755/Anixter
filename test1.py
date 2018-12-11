from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import json
from bs4 import BeautifulSoup
import pymysql.cursors
import os.path


def get_list():
	try:
		# options = Options()
		# options.set_headless(headless=True)
		# driver = webdriver.Chrome(options=options, executable_path='/Users/yashgupta/Desktop/chromedriver')
		# driver.get("https://www.anixter.com/en_us/login.html")
		# time.sleep(2)
		# driver.save_screenshot('login.png')
		# name = driver.find_element_by_id('j_username')
		# name.send_keys('e733733@gmail.com')
		# password = driver.find_element_by_id('j_password')
		# password.send_keys('ProdSupp9737')
		# driver.find_element_by_xpath("//*[@class='positive button primary-large']").click()
		# time.sleep(2)
		# driver.get('https://www.anixter.com/en_us/products/Electrical-Wire-and-Cable/c/GROUP_EW?q=%3Arelevance&page=131&op=')
		# driver.save_screenshot('test.png')
		

		# html2 = driver.page_source
		# soup = BeautifulSoup(html2, "lxml", from_encoding="utf-8")

		headers = {
		'cache-control': "no-cache",
		'User-Agent': 'Mozilla/5.0',
		}

		response = requests.request("GET", 'https://www.anixter.com/en_us/products/Electrical-Wire-and-Cable/c/GROUP_EW?q=%3Arelevance&page=131&op=', headers=headers)

		soup = BeautifulSoup(response.content, 'html.parser')

		products = soup.find_all('div',{'class':'product-tile-tertiary row'})
		for product in products:
			para = product.find('p',{'class':'title-primary'})
			if para:
				a_link = para.find('a')
				a_link = a_link.get('href')
				# response1 = requests.request("GET", 'https://www.anixter.com' + str(a_link), headers=headers)
				# soup1 = BeautifulSoup(response1.content, 'html.parser')

				# fragment = soup1.find('div',{'id':'fragment-1'})
				# if fragment:
				# 	print (fragment)


			# title = product.find('p',{'class':'title-primary'})
			# if title:
			# 	print (title.text.strip())

	

	except Exception as e:
		print(e)
		print("Loop1...")
		time.sleep(2)
		print("Was a nice sleep, now let me continue...")
		

if __name__ == '__main__':
	get_list()