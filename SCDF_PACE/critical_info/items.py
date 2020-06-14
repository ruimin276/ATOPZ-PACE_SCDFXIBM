# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CriticalInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CriticalItem(scrapy.Item):
    person_id = scrapy.Field()  # the id of the person
    location = scrapy.Field()  # current location of the person
    age = scrapy.Field()
    gender = scrapy.Field()
    # above are personal particulars

    temperature = scrapy.Field()
    blood_pressure = scrapy.Field()
    heart_rate = scrapy.Field()
    respiratory_rate = scrapy.Field()
    sweat_rate = scrapy.Field()
    #  more information can be added into this field if hardware allows. e.g. blood sugar, blood lipids

    time = scrapy.Field()
    status = scrapy.Field()
