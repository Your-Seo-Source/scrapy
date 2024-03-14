from itemadapter import ItemAdapter

# New file: livablproject/pipelines.py
import scrapy
from itemadapter import ItemAdapter
from .items import LivablprojectItem

class JsonOrganizerPipeline:
    def process_item(self, item, spider):
        organized_item = {key: item[key] for key in sorted(ItemAdapter(item).asdict().keys())}
        return organized_item