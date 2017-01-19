import mysql.connector
from biquge import settings

cnx = mysql.connector.connect(user=settings.MYSQL_USER, password=settings.MYSQL_PASSWORD,
                              host=settings.MYSQL_HOST, database=settings.MYSQL_DB)
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def insert_infor(cls, novel_id, author, name, url, content):
        sql = 'INSERT INTO `biquge_information` (`novel_id`, `novel_name`, `author`, `url`, `content`) ' \
              'VALUES (%(novel_id)s, %(novel_name)s, %(author)s, %(url)s, %(content)s)'
        value = {
            'novel_id': novel_id,
            'novel_name': name,
            'author': author,
            'url': url,
            'content': content
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_novel_id(cls, novel_id):
        sql = 'SELECT EXISTS(SELECT 1 FROM biquge_information WHERE novel_id=%(novel_id)s)'
        value = {
            'novel_id': novel_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]

    @classmethod
    def insert_chapter(cls, novel_id, num, chapter_content, chapter_url, chapter_name):
        sql = 'INSERT INTO `biquge_chapter` (`novel_id`, `num`, `chapter_content`, `chapter_url`, `chapter_name` ) ' \
              'VALUES (%(novel_id)s, %(num)s, %(chapter_content)s,  %(chapter_url)s, %(chapter_name)s) '
        value = {
            'novel_id': novel_id,
            'num': num,
            'chapter_content': chapter_content,
            'chapter_url': chapter_url,
            'chapter_name': chapter_name
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_chapter_name(cls, chapter_name):
        sql = 'SELECT EXISTS(SELECT 1 FROM biquge_chapter WHERE chapter_name=%(chapter_name)s)'
        value = {
            'chapter_name': chapter_name
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]
