# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Scrapy1Pipeline:
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            db = 'scrapymysql',
            user = 'root',
            passwd = 'root',
            charset = 'utf8',
            use_unicode = True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        self.cursor.execute(
            '''insert into movie(title,up_image,introduces,intros,low_image,cili) value (%s,%s,%s,%s,%s,%s)
            ''',# python 操作SQL的语句
            (item['title'],
             item['up_image'],
             item['introduces'],
             item['intros'],
             item['low_image'],
             item['cili'],
             ))
        self.connect.commit()
        return item
