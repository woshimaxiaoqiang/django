# -*- coding: utf-8 -*-
import scrapy


class UseragentjobSpider(scrapy.Spider):
    name = 'useragentjob'
    allowed_domains = ['www.qq.com/']
    start_urls = ['https://www.qq.com/']

    def parse(self, response):
        print(response.request.headers['User-Agent'])
        #print(response.xpath('//*[@id="uas_textfeld"]//text()').extract_first())
        yield scrapy.Request(self.start_urls[0],dont_filter=True)
        pass
