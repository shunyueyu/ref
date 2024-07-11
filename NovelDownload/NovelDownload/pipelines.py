# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class NoveldownloadPipeline:
    def process_item(self, item, spider):
        curPath = item['base_path']
        if not os.path.exists(curPath):
            os.makedirs(curPath)

        filename_path = curPath + 'aa.txt'
        with open(filename_path, 'a+', encoding='utf-8') as f:
            f.write(item['title'] + "\n")
            f.write(item['content'] + "\n")
        return item

