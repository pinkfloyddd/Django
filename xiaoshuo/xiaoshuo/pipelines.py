# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class XiaoshuoPipeline(object):
    def __init__(self):
        self.dbcon = pymysql.connect(host='192.168.138.134',user='django',passwd='zhaoye861227',port=3306,db='douban',use_unicode=True,charset='utf8')
        self.cursor = self.dbcon.cursor()
    def process_item(self, item, spider):
        if spider.name == 'qidian':
            print('现在执行qidian的pipeline')
            novel_name_list = item['novel_name']
            novel_writter_list = item['novel_writter']
            novel_main_type_list =  item['novel_main_type']
            novel_sub_type_list = item['novel_sub_type']
            novel_status_list = item['novel_status']
            novel_real_url_list = item['novel_real_url']
            novel_img_url_list = item['novel_img_url']
            basic_info_sql = 'insert into qidian_qidian_xiaoshuo(novel_name,novel_writter,novel_main_type,novel_sub_type,novel_status,novel_real_url,novel_img_url) value(%s,%s,%s,%s,%s,%s,%s)'
            for novel_name,novel_writter,novel_main_type,novel_sub_type,novel_status,novel_real_url,novel_img_url in zip(novel_name_list,novel_writter_list,novel_main_type_list,novel_sub_type_list,novel_status_list,novel_real_url_list,novel_img_url_list):
                if self.cursor.execute('select * from qidian_qidian_xiaoshuo where novel_name=%s',novel_name):
                    print(novel_name + '已在小说信息基表中')
                else:
                    try:
                        self.cursor.execute(basic_info_sql,(novel_name,novel_writter,novel_main_type,novel_sub_type,novel_status,'https:'+novel_real_url,'https:'+novel_img_url))
                        self.dbcon.commit()
                    except Exception as e:
                        print(e)
                        print(novel_name + '小说信息基表插入失败')
                    else:
                        print(novel_name + '小说信息基表插入成功')
            return item
            self.dbcon.close()
        elif spider.name == 'chapter_spider1' or 'chapter_spider2':
            chapter_context = item['chapter_context']
            chapter_name = item['chapter_name']
            novel_name = item['novel_name']
            chapter_url = item['chapter_url']
            sql = 'insert into qidian_chapter_detail_table(novel_name,novel_chapter_name,novel_chapter_url,novel_chapter_context) value(%s,%s,%s,%s)'
            try:
                self.cursor.execute(sql,(novel_name,chapter_name,chapter_url,chapter_context))
                self.dbcon.commit()
            except Exception as e:
                print(e)
            else:
                print(novel_name + chapter_name + '插入数据库成功')
            return item
            self.dbcon.close()



            # print('执行'+spider.name+'的pipelines')
            # novel_chapter_name = item['chapter_name']
            # novel_chapter_url = item['chapter_url']
            # novel_name = item['novel_name']
            # print(novel_name)
            # print(novel_chapter_name)


            # for novel_name_with_chapter in novel_name:
            #     chapter_detail_table_insert_sql = 'insert into qidian_chapter_deatil_table(NOVEL_NAME,NOVEL_CHAPTER_NAME,NOVEL_CHAPTER_URL,NOVEL_CHAPTER_PATH,NOVEL_CHAPTER_ID) VALUE(%S,%S,%S,%S,%S)'
            #     chapter_name_exists_sql = self.cursor.exectue('select NOVEL_CHAPTER_NAME from qidian_chapter_detail_table where NOVEL_NAME=' + novel_name_with_chapter)
            #     chapter_name_exists_resut = self.cursor.fetchall()
            #     chapter_name_exists_list = list(chapter_name_exists_resut)
            #     print(chapter_name_exists_list)




        #     for novel_name_table_name in novel_name:
        #         chapter_detail_table_create_sql = 'create table ' + novel_name_table_name + '(CHAPTER_NAME varchar(100),CHAPTER_CONTEXT_PATH varchar(100))'
        #         chapter_update_sql = 'insert into ' + novel_name_table_name + '(CHAPTER_NAME,CHAPTER_CONTEXT_PATH) value(%s,%s)'
        #         if self.cursor.exectue('desc' + novel_name_table_name):
        #             print(novel_name_table_name + '的详细章节表已创建')
        #             chapter_count_in_db = self.cursor.exectue('select count(*) from ' + novel_name_table_name)
        #             chapter_count_in_item_list = len(novel_chapter_name)
        #             chapter_diff = chapter_count_in_db - chapter_count_in_item_list
        #             if chapter_diff == 0:
        #                 print(novel_name + '无新的章节要更新')
        #             else:
        #                 novle_chapter_update_name = novel_chapter_name[chapter_diff:0]
        #                 for i in novle_chapter_update_name:
        #                     self.cursor.exectue(chapter_update_sql,(i,'D:\spider_data\\' + novel_name + i))
        #                     self.cursor.commit()
        #         else:
        #             print('新创建' + novel_name_table_name + '的章节表')
        #             self.cursor.exectue(chapter_detail_table_create_sql)
        #             self.cursor.exectue(chapter_update_sql,(novel_chapter_name,'D:\spider_data\\'+novel_name+novel_chapter_name))
        #             self.cursor.commit()
        #     self.dbcon.close()
        # else:
        #     print('没有执行pipelines')