from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re
import pymysql.cursors
import os.path


def get_list():
	try:
		connection = pymysql.connect(host= "108.167.172.175",
			user="dockonef_jashg",
			passwd="gC=wRXPdhUsP",
			db="dockonef_scrape",
			charset='utf8mb4',
			cursorclass=pymysql.cursors.DictCursor)
		try:
			with connection.cursor() as cursor:
				cursor.execute("SELECT * FROM adi_category")
				connection.commit()


				for row in cursor:
					try:
						data = row
						print (data)
					except Exception as e:
						print ("Loop3")
						print (e)
						continue

		except Exception as e:
			print ('Failed Query')
			print ("Loop2")
			print (e)
	except pymysql.Error as e:
		print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
		print ("Loop1")
		time.sleep(2)
		print("Was a nice sleep, now let me continue...")
		

if __name__ == '__main__':
	get_list()