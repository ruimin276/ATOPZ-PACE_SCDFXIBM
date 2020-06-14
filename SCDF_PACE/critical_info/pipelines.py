# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import MySQLdb
import psycopg2
from scrapy import Request


class CriticalInfoPipeline:

    def __init__(self):
        self.file = open('data.json', 'w')  # write the information into a json file

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"  # dumps the json file into a dictionary
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()


class ItemMysqlPipeline(object):
    # information depends on actual database used
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="",
            user="",
            passwd="",
            db="",
            port=0000,
            use_unicode=True,
            charset="")

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        param = []
        param.append([item.get('id'),
                      item.get('time'),
                      item.get('temperature'),
                      item.get('blood_pressure'),
                      item.get('breath_rate'),
                      item.get('heart_rate'),
                      item.get('sweat_rate'),
                      item.get('status')]
                     )
        try:
            sql = 'INSERT INTO database_name(id,time,temperature,blood_pressure,breath_rate,heart_rate,sweat_rate,status) values(%d,,%d,%d,%d,%d,%d,%d,%s)'
            # insert into database
            self.cur.executemany(sql, param)
            self.conn.commit()
        except Exception as e:
            print(e)
            print("Error: unable to fetch data")

        return item

    def close_spider(self, spider):
        self.cur.close()
