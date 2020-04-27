# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy1.items import Scrapy1Item

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['https://www.66e.cc/dongzuopian/']
    start_urls = ['https://www.66e.cc/dongzuopian/']

    def parse(self, response):
        post_urls = response.css('.listimg a::attr(href)').extract()
        for post_url in post_urls:
            yield Request(url=post_url,callback=self.parse_detail,dont_filter=True)
        next_url = response.css('div.pagebox:nth-child(1) > a:nth-child(12)::attr(href)').extract_first()
        if next_url:
            yield Request(url=next_url,callback=self.parse,dont_filter=True)

    def parse_detail(self,response):
        movieitem = Scrapy1Item()
        movieitem['title'] = response.xpath("/html/body/div[4]/div[1]/div[1]/h1/text()").extract_first()
        movieitem['up_image'] = response.xpath("//*[@id=\"text\"]/p[1]/img/@src").extract_first()
        movieitem['introduces'] = response.xpath('//*[@id="text"]/p[1]/text()').extract()
        movieitem['intros'] = response.xpath('//*[@id="text"]/p[3]/text()').extract_first()
        movieitem['low_image'] = response.xpath('//*[@id="text"]/p[4]/img/@src').extract_first()
        movieitem['cili'] = response.xpath('//*[@id="text"]/table/tbody/tr[2]/td/a/@href').extract_first()
        yield movieitem
