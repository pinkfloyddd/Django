# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem,ChapterSpider1Item
from fake_useragent import UserAgent
import requests
import os
from time import sleep
class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/free/all?page='+str(page_num) for page_num in range(1,4)]
    ua = UserAgent(use_cache_server = False)
    UserAgent = ua.chrome
    headers = {'User-Agent': UserAgent}
    def parse(self, response):
        item = XiaoshuoItem()
        item['novel_name'] = response.xpath('//ul[@class="all-img-list cf"]//li[re:match(@data-rid,"\d")]/div[@class="book-mid-info"]/h4/a/text()').extract()
        item['novel_writter'] = response.xpath('//ul[@class="all-img-list cf"]//li/div[2]/p[@class="author"]/a[@class="name"]/text()').extract()
        item['novel_main_type'] = response.xpath('//ul[@class="all-img-list cf"]//li/div[2]/p[@class="author"]/a[2]/text()').extract()
        item['novel_sub_type'] = response.xpath('//ul[@class="all-img-list cf"]//li/div[2]/p[@class="author"]/a[3]/text()').extract()
        item['novel_status'] = response.xpath('//ul[@class="all-img-list cf"]//li/div[2]/p[@class="author"]/span/text()').extract()
        item['novel_img_url'] = response.xpath('//ul[@class="all-img-list cf"]//li/div[1]//img/@src').extract()
        item['novel_real_url'] = response.xpath('//ul[@class="all-img-list cf"]//li/div[2]/h4/a/@href').extract()
        for novel_dir,img_url in zip(item['novel_name'],item['novel_img_url']):
            if os.path.exists('D:\spider_data\\'+novel_dir):
                pass
            else:
                os.mkdir('D:\spider_data\\'+novel_dir)
                os.chdir('D:\spider_data\\'+novel_dir)
                img_resp = requests.get('https:'+img_url, headers=self.headers)
                with open(novel_dir+'.jpg','wb') as fp:
                    fp.write(img_resp.content)
                    fp.close()
                    sleep(1)
        yield item