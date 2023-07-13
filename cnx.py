import requests
import sys

res = []

def test(url):
	try:
		resp = requests.get(url, timeout=1)
		if resp.status_code == 200:
			print(" \33[32mOK\033[0m")
		else:
			print(" \033[91mNo Response\033[0m")
	except:
		print(" \033[91mNo Response\033[0m")

urls = sys.argv[1]
with open(urls, 'r') as file:
	lines = file.readlines()
	for line in lines:
		line = line.strip()
		print(f"[-] \33[34m{line} :\033[0m", end='')
		test(line)
