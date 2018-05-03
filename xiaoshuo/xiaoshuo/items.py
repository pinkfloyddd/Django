# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    novel_name = scrapy.Field()
    novel_writter = scrapy.Field()
    novel_main_type = scrapy.Field()
    novel_sub_type = scrapy.Field()
    novel_status = scrapy.Field()
    novel_real_url = scrapy.Field()
    novel_img_url = scrapy.Field()
class ChapterSpider1Item(scrapy.Item):
    chapter_name = scrapy.Field()
    chapter_url = scrapy.Field()
    novel_name = scrapy.Field()
    chapter_context = scrapy.Field()
class ChapterSpider2Item(scrapy.Item):
    chapter_name = scrapy.Field()
    chapter_url = scrapy.Field()
    novel_name = scrapy.Field()
    chapter_context = scrapy.Field()