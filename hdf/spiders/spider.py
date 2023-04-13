# -*-coding:utf-8-*-
import sys
import scrapy
from scrapy.selector import Selector
import json
from hdf.items import CommonDoctorItem,FamousDoctorItem
 
 
class HaodfSpider(scrapy.Spider):
     # 爬虫名称
     name = "haodf"

     custom_settings = {
        'ITEM_PIPELINES': {
            'hdf.pipelines.HdfPipeline': 300
        }
     }

     hostname = "https://www.haodf.com"
     # 设置下载延时
     download_delay = 1
     # 允许域名
     allowed_domains = [hostname[8:]]
     print(allowed_domains)

     # 开始URL
     start_urls = [
        hostname
     ]
 
     # 解析内容函数
     def parse(self, response):
        result = response.selector.xpath('//ul[@class="visit-ul clearfix js-visit-ul"]')
        items = result.xpath('//a[@class="visit-li-left js-color-148cfa"]')
        print(len(items))
        for index,item in enumerate(items):
            name  = item.xpath('.//p[@class="doc-info"]/text()')[0].extract()
            name,title = name.split(" ")
            image = item.xpath(".//img/@src")[0].extract()
            hospital = item.xpath('.//p[@class="text-over"]/text()')[0].extract()
            status   = item.xpath('.//span[@class="doc-state color-FF8C28"]/text()')[0].extract()
            print(f"name:{name},title:{title},image:{image},hospital:{hospital},status:{status}")

            famous_doctor = FamousDoctorItem(name=name,title=title,image=image,hospital=hospital,status=status)
            yield famous_doctor



class DoctorSpider(scrapy.Spider):
    name = "doctor"
    hostname = "https://www.haodf.com/ndisease/ajaxLoadMoreDoctor"

    custom_settings = {
        'ITEM_PIPELINES': {
            'hdf.pipelines.CommonPipeline': 300
        }
     }

    start_urls = [hostname]



    def start_requests(self):
        data = {
            "nowPage": "3",
            "pageSize": "15",
            "placeId": "",
            "termId": "462"
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        data = result["data"]["list"]
        #print(data)
        bds = Selector(text = data).xpath('//a[@class="item-bd"]')
        for item in bds:
            image = item.xpath(".//img/@src")[0].extract()
            name  = item.xpath(".//span[@class='name']/text()")[0].extract()
            grade = item.xpath(".//span[@class='grade']/text()")[0].extract()
            hospital = item.xpath(".//p[@class='hos-faculty']/text()")[0].extract().strip()
            goodat   = item.xpath(".//p[@class='goodat']/text()")[0].extract().strip()
            print(f"image:{image},name:{name},grade:{grade},hospital:{hospital},goodat:{goodat}")

            common_doctor = CommonDoctorItem(name=name,image=image,grade=grade,hospital=hospital,goodat=goodat)
            yield common_doctor


