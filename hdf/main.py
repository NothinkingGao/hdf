from scrapy import cmdline
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.spider import DoctorSpider,HaodfSpider

# 每页爬取量,这个最好不变
page_size=15
# 病名,需要从网页上看
term_id=462
# 总共多少医生,需要从网页上看
total_size = 60

settings = get_project_settings()
process = CrawlerProcess(settings)

for i in range(total_size//page_size):
    process.crawl(DoctorSpider,page_index=i,page_size=page_size,term_id=term_id)

process.start()
