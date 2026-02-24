# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class GovIfomaGetPipeline:
       # 豆包写法
    def __init__(self):
        # 初始化 CSV 文件（写入表头）
        self.file = open('car_ifo_42.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(
            self.file,
            fieldnames=['标题', '产品商标', '产品型号', '产品名称', '企业名称']
        )
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 写入每一行数据
        self.writer.writerow(dict(item))
        return item  # 继续传递给下一个管道（如果有的话）

    def close_spider(self, spider):
        # 关闭文件
        self.file.close()
