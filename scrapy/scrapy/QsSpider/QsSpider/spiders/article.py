# 0219, by Queenie

import scrapy

class ArticleSpider(scrapy.Spider):

    name = 'eggs' # module name instead of class name

    # req means request
    def start_requests(self):
        urls = [
            'https://www.tpex.org.tw/web/bond/tradeinfo/internationalbond/FormosaDaily.php?l=zh-tw',
            'https://www.tpex.org.tw/web/bond/tradeinfo/internationalbond/USDDIBCurve.php?l=zh-tw',
            'https://www.tpex.org.tw/web/bond/tradeinfo/internationalbond/TheoreticalValue.php?l=zh-tw'
        ]

        return [scrapy.Request(url=url, callback=self.parse) for url in urls] 

    def parse(self, response):
        target_url = response.url
        title = response.css('h1::text').extract_first()
        print(target_url, title)
        