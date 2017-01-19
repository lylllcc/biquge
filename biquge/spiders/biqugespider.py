import scrapy
from scrapy.http import Request
from biquge.items import BiqugeItem, ChapterContentItem
import re
from biquge.mysqlpipelines.sql import Sql

class BiqugeSpider(scrapy.Spider):
    # 爬虫的名字，和start.py中相对应。
    name = 'biquge'

    base_url = 'http://www.qu.la'

    # 爬虫入口
    def start_requests(self):
        start_url = self.base_url + '/xiaoshuodaquan/'
        yield Request(start_url, callback=self.get_novel_url)

    # 获取小说url
    def get_novel_url(self, response):
        base_a = response.xpath('//div[@class="novellist"]/ul/li/a/@href').extract()
        for a in base_a:
            novel_a = self.base_url + a
            yield Request(novel_a, callback=self.get_information_and_chapter, meta={"novel_a": novel_a})

    # 获取基本信息
    def get_information_and_chapter(self, response):
        item = BiqugeItem()
        item['content'] = ''.join(response.xpath('//meta[@property="og:description"]/@content').extract()). \
            replace(' ', ''). \
            replace('\n', '')

        # 保存小说链接
        novel_url = response.meta['novel_a']
        item['url'] = novel_url

        # 提取小说名字
        novel_name = ''.join(response.xpath('//meta[@property="og:novel:book_name"]/@content').extract())
        item['name'] = novel_name

        # 提取小说作者
        item['author'] = ''.join(response.xpath('//meta[@property="og:novel:author"]/@content').extract())

        # 从url中提取小说id
        novel_id = ''.join(re.findall('\d', novel_url))
        item['novel_id'] = novel_id
        yield item


        urls = re.findall('<dd><a href="(.*?)">(.*?)</a>', response.text)
        num = 0
        for url in urls:
            num += 1
            chapter_url = self.base_url + '/book/' + novel_id + '/' + url[0]
            chapter_name = url[1]
            if Sql.select_chapter_name(chapter_name) == 1:
                print('章节已经存在')
                pass
            else:
                yield Request(chapter_url, self.get_chapter_content, meta={'num': num,
                                                                           'chapter_url': chapter_url,
                                                                           'chapter_name': chapter_name,
                                                                           'novel_id': novel_id})

    def get_chapter_content(self, response):
        item = ChapterContentItem()
        content = response.xpath('//div[@id="content"]/text()').extract()
        chapter_content = ''.join(content).replace('\xa0', '')

        item['chapter_content'] = chapter_content
        item['novel_id'] = response.meta['novel_id']
        item['num'] = response.meta['num']
        item['chapter_name'] = response.meta['chapter_name']
        item['chapter_url'] = response.meta['chapter_url']
        return item
