import os
import time

brands = ['mizuno']
for b in brands:
	cmd = 'scrapy crawl ' + b + ' -o /home/xiao/gitReadWrite/algorithm/goodsMenu/goodsMenu/json/goodsMenu.json'
	print(cmd)
	os.system(cmd)


