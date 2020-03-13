# -*- coding: utf-8 -*-
import scrapy


class IpproxyjobSpider(scrapy.Spider):
    name = 'ipproxyjob'
    allowed_domains = ['http://www.atool9.com/ip.php']
    start_urls = ['http://www.atool9.com/ip.php']

    def parse(self, response):
        ip = response.xpath('/html/body/div[5]/ul[1]/li/span/text()').extract_first()
        print(ip)
        yield scrapy.Request(self.start_urls[0],dont_filter=True)
        pass
