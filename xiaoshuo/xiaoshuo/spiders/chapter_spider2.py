# -*- coding: utf-8 -*-
import scrapy
import pymysql
import os,re
import requests
from fake_useragent import UserAgent
from xiaoshuo.items import ChapterSpider2Item
from lxml import etree
class ChapterSpider2Spider(scrapy.Spider):
    name = 'chapter_spider2'
    allowed_domains = ['qidian.com']
    ua = UserAgent(use_cache_server=False)
    UserAgent = ua.chrome
    headers = {'User-Agent': UserAgent}
    def __init__(self):
        self.dbcon = pymysql.connect(host='192.168.138.134',user='django',passwd='zhaoye861227',port=3306,db='douban',use_unicode=True,charset='utf8')
        self.cursor = self.dbcon.cursor()
        self.cursor.execute('select novel_real_url from qidian_qidian_xiaoshuo')
        self.result = self.cursor.fetchall()
        self.result_list = list(self.result)
        self.cursor.close()
    def start_requests(self):
        for start_url in self.result_list:
            print(start_url[0])
            yield scrapy.Request(start_url[0],callback=self.parse,headers=self.headers)
    def parse(self, response):
        novel_name = response.xpath('//div[@class="book-info "]/h1/em/text()').extract()[0]
        li_judge = response.xpath('//*[@id="j-catalogWrap"]/div[2]/div[1]/ul[@class="cf"]/li/a/text()').extract()
        li_judge_count = len(li_judge)
        if li_judge_count == 2:
            print(novel_name + '有推荐')
            lis = response.xpath('//*[@id="j-catalogWrap"]/div[2]/div[2]/ul[@class="cf"]/li')
            for li in lis:
                item = ChapterSpider2Item()
                item['chapter_name'] = li.xpath('a/text()').extract()[0]
                item['chapter_url'] = li.xpath('a/@href').extract()[0]
                resp = requests.get('https:'+item['chapter_url'],headers=self.headers)
                context_selector = etree.HTML(resp.text)
                context = context_selector.xpath('//div[@class="read-content j_readContent"]/p/text()')
                item['chapter_context'] = ''.join(context)
                item['novel_name'] = context_selector.xpath('//a[@id="bookImg"]/text()')[0]
                yield item



'''将章节文本保存到本币的思路'''

        #     item = ChapterSpider2Item()
        #     item['novel_name'] = response.xpath('//div[@class="book-info "]/h1/em/text()').extract()
        #     item['chapter_name'] = response.xpath('//*[@id="j-catalogWrap"]/div[2]/div[2]/ul[@class="cf"]/li/a/text()').extract()
        #     item['chapter_url'] = response.xpath('//*[@id="j-catalogWrap"]/div[2]/div[2]/ul[@class="cf"]/li/a/@href').extract()
        #     if os.path.exists('D:\spider_data\\' + novel_name):
        #         print('进入' + novel_name + '小说主目录')
        #         os.chdir('D:\spider_data\\' + novel_name)
        #         for context_urls, context_names in zip(item['chapter_url'], item['chapter_name']):
        #             r1 = u'[#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
        #             context_name = re.sub(r1,'',context_names)
        #             if os.path.exists(context_name + '.txt'):
        #                 print("chapter" + context_name + " 已下载")
        #             else:
        #                 print('正在下载' + novel_name + context_name)
        #                 context_url = 'https:' + context_urls
        #                 resp = requests.get(context_url, headers=self.headers)
        #                 context_selector = etree.HTML(resp.text)
        #                 context = ''.join(context_selector.xpath('//div[@class="read-content j_readContent"]/p/text()'))
        #                 with open(context_name + '.txt', 'w') as cp:
        #                     cp.write(context)
        #                     cp.close()
        #     else:
        #         print('小说主目录不存在，请检查')
        #     yield item
        # else:
        #     print(novel_name + '有推荐，使用chapter_spider1爬虫')

