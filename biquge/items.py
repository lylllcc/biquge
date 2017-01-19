# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):

    # id
    novel_id = scrapy.Field()
    # 小说名字
    name = scrapy.Field()
    # 小说作者
    author = scrapy.Field()
    # 小说url
    url = scrapy.Field()

    # 小说简介
    content = scrapy.Field()

class ChapterContentItem(scrapy.Item):

    novel_id = scrapy.Field()

    num = scrapy.Field()

    chapter_content = scrapy.Field()

    chapter_name = scrapy.Field()

    chapter_url = scrapy.Field()



