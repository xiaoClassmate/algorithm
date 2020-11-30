import os
import time

brands = ['mizuno']
for b in brands:
	cmd = 'scrapy crawl ' + b + ' -o goodsMenu.json'
	print(cmd)
	os.system(cmd)


