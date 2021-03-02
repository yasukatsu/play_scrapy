# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import csv
from datetime import datetime


class LevtechCsvWriterPipeline:

    def open_spider(self, spider):
        f = open(f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv', 'w')
        fieldnames = [
            'fee',
            'job_content'
        ]
        self.f = f
        self.writer = csv.DictWriter(f, fieldnames=fieldnames)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.writer.writerow(ItemAdapter(item).asdict())
