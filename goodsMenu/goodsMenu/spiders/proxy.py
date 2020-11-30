import scrapy
from bs4 import BeautifulSoup
import json
class ProxySpider(scrapy.Spider):
    name = "proxy"
    allowed_domains = ["www.us-proxy.org"]
    start_urls = ['https://www.us-proxy.org']
    custom_settings = {
            'ITEM_PIPELINES': {    
                'goodsMenu.pipelines.GoodsmenuPipeline': 300
            }
        }

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.select("#proxylisttable tr")
        for tr in trs:
            tds = tr.select("td")
            if len(tds) > 6:
                ip = tds[0].text
                port = tds[1].text
                anonymity = tds[4].text
                ifScheme = tds[6].text
                if ifScheme == 'yes': 
                    scheme = 'https'
                else: scheme = 'http'
                proxy = "%s://%s:%s"%(scheme, ip, port)
                if scheme == 'https': 
                    meta = {
                        'scheme': scheme,
                        'proxy': proxy,
                        'port': port,
                    }
                # print(meta)
                    yield scrapy.Request('http://www.us-proxy.org', callback=self.proxy_check_available, meta=meta, dont_filter=True)

    # {"origin": "your ip"}

    def proxy_check_available(self, response):
        proxy = response.meta['proxy']
        if proxy == json.loads(response.text)['origin']:
            return {
                'scheme': response.meta['scheme'],
                'proxy': response.meta['proxy'],
                'port': response.meta['port']
            }
