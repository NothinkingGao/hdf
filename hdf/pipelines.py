# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs

class HdfPipeline:
    def __init__(self):
        self.file_name = "famous.json"
        self.file = codecs.open(self.file_name, mode='wb', encoding='utf-8')
 
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        
        return item

    def close_spider(self,spider):
        if self.file:
            self.file.close()


class CommonPipeline:
    def __init__(self):
        self.file_name = "common.json"
        self.file = codecs.open(self.file_name, mode='wb', encoding='utf-8')
 
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        
        return item

    def close_spider(self,spider):
        if self.file:
            self.file.close()


