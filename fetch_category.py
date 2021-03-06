import requests
import re
import time
import pymysql.cursors
from bs4 import BeautifulSoup

def get_list():
	try:
		url = "https://www.anixter.com/en_us/products/Products/c/ROOT"
		headers = {
		'cache-control': "no-cache",
		'User-Agent': 'Mozilla/5.0',
		}

		dbCategory = ''
		dbSubcategory = ''
		dbPageURL = ''
		dbPageNumber = ''

	
		response = requests.request("GET", url, headers=headers)

		soup = BeautifulSoup(response.content, 'html.parser')
		all_data = soup.find_all('div',{'class':'facet R'})

		for data in all_data:
			facetHead = data.find('div',{'class':'facetHead'})
			if facetHead:
				dbCategory = facetHead.text.strip()

				ul_class = data.find('ul',{'class':'facet_block indent'})
				if ul_class:
					lis = ul_class.find_all('li')
					for li in lis:
						dbSubcategory = li.text.strip()
						a_tag = li.find('a')
						p_url = "https://www.anixter.com" + a_tag.get('href')
						try:
							response1 = requests.request("GET", p_url, headers=headers)
							soup1 = BeautifulSoup(response1.content, 'html.parser')
							page = soup1.find('div',{'class':'paginationBar top clearfix'})
							if page:
								count = page.find('div',{'class':'result-count col-xs-5 col-sm-3 col-sm-push-4 text-right'})
								if count:
									count = count.text.strip()
									count = count.split('of')
									if len(count) >=2:
										number = re.findall('\d+', count[1])
										page_number = int(number[0])
										page_number = page_number/20

										page = 0
										while page <= page_number:
											dbPageURL = p_url + '?q=%3Arelevance&page=' + str(page) + '&op='
											dbPageNumber = page
											page = page+1
											print (dbPageURL)
											try:
												connection = pymysql.connect(host= "108.167.172.175",
													user="dockonef_jashg",
													passwd="gC=wRXPdhUsP",
													db="dockonef_scrape",
													charset='utf8mb4',
													cursorclass=pymysql.cursors.DictCursor)
												try:
													with connection.cursor() as cursor:
														cursor.execute("INSERT INTO anixter_category (category,subcategory,pageurl,pagenumber) VALUES (%s,%s,%s,%s)", (dbCategory,dbSubcategory,dbPageURL,dbPageNumber))
														connection.commit()
														print ("Inserted")
												except Exception as e:
													print ('Failed Query')
													print (e)
												finally:
													connection.close()
											except pymysql.Error as e:
												print("Connection refused by the server..")
												print("Let me sleep for 2 seconds")
												print ("Loop5")
												print ("ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1]))
												time.sleep(2)
												print("Was a nice sleep, now let me continue...")
												continue															
						except Exception as e:
							print(e)
							print("Loop2...")
							time.sleep(2)
							print("Was a nice sleep, now let me continue...")
	except Exception as e:
		print(e)
		print("Loop1...")
		time.sleep(2)
		print("Was a nice sleep, now let me continue...")
		

if __name__ == '__main__':
	get_list()
