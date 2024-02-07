import json
import requests
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class NewsbreakPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        domain_array = adapter.get("domain")
        if len(domain_array) > 0:
            adapter['domain'] = domain_array[0]
        return item
    