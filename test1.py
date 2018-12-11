import requests
from bs4 import BeautifulSoup


def get_list():
	try:
		headers = {
		'cache-control': "no-cache",
		'User-Agent': 'Mozilla/5.0',
		}

		response = requests.request("GET", 'https://www.anixter.com/en_us/products/Electrical-Wire-and-Cable/c/GROUP_EW?q=%3Arelevance&page=131&op=', headers=headers)

		soup = BeautifulSoup(response.content, 'html.parser')

		products = soup.find_all('div',{'class':'product-tile-tertiary row'})
		for product in products:
			# para = product.find('p',{'class':'title-primary'})
			# if para:
			# 	a_link = para.find('a')
			# 	a_link = a_link.get('href')
				# response1 = requests.request("GET", 'https://www.anixter.com' + str(a_link), headers=headers)
				# soup1 = BeautifulSoup(response1.content, 'html.parser')

				# fragment = soup1.find('div',{'id':'fragment-1'})
				# if fragment:
				# 	print (fragment)


			title = product.find('p',{'class':'title-primary'})
			if title:
				print (title.text.strip())

	

	except Exception as e:
		print(e)
		print("Loop1...")
		time.sleep(2)
		print("Was a nice sleep, now let me continue...")
		

if __name__ == '__main__':
	get_list()