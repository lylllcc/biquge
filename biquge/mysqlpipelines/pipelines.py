from .sql import Sql
from biquge.items import BiqugeItem
from biquge.items import ChapterContentItem


class BiqugePipeline(object):

    def process_item(self, item, spider):

        if isinstance(item, BiqugeItem):
            novel_id = item['novel_id']
            ret = Sql.select_novel_id(novel_id)
            if ret[0] == 1:
                print('小说已经存在')
                pass
            else:
                name = item['name']
                author = item['author']
                content = item['content']
                url = item['url']
                print('小说不存在')
                Sql.insert_infor(novel_id, author, name, url, content)

        if isinstance(item, ChapterContentItem):
            novel_id = item['novel_id']
            num = item['num']
            chapter_content = item['chapter_content']
            chapter_url = item['chapter_url']
            chapter_name = item['chapter_name']
            Sql.insert_chapter(novel_id, num, chapter_content, chapter_url, chapter_name)
            print("储存章节")
            return item
