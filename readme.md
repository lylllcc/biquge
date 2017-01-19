# Biquge  

## 简介  
基于python(3.5) [scrapy](https://scrapy.org/)(1.3)框架的一个爬虫。
抓取[笔趣阁](http://www.qu.la/)(链接可能失效)网站上的所有小说的名字，作者，id，章节内容等基本信息。并存在mysql数据库中。

### 安装  
1. 安装[python3](https://www.python.org/)
2. 安装[scrapy](https://scrapy.org/)   
3. 安装[mysql](https://www.mysql.com/)  
4. 克隆 ``` git clone https://github.com/lylllcc/biquge ```  

### 配置
在 biquge/setting.py 中写入mysql的基本信息
```
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = '3306'
MYSQL_DB = 'novel'
```  

### 建立数据库表
```
CREATE TABLE `novel`.`biquge_information` ( `id` INT NOT NULL AUTO_INCREMENT , `novel_id` VARCHAR(255) NOT NULL , `author` VARCHAR(255) NOT NULL , `url` VARCHAR(255) NOT NULL , `novel_name` VARCHAR(255) NOT NULL , `content` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

```

```
CREATE TABLE `novel`.`biquge_chapter` ( `id` INT NOT NULL AUTO_INCREMENT , `novle_id` VARCHAR(255) NOT NULL , `num` VARCHAR(255) NOT NULL , `chapter_content` TEXT NOT NULL , `chapter_name` VARCHAR(255) NOT NULL , `chapter_url` VARCHAR(255) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
```

### 启动项目  

```
python start.py
```

## LICENSE  
[MIT](/LICENSE)



