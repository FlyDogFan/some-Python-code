#-*- coding:utf-8 -*-

import scrapy

from mySpider.items import ItcastItem

class ItcastSpider(scrapy.spiders.Spider):
    name="itcast"
    allowd_domains = ["http://www.itcast.cn"]
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#ac"
    ]


    def parse(self, response):

        # 全部老师的集合
        items = []

        #file_name = "teacher.html"
        #open(file_name, "w").write(response.body)
        for site in response.xpath('//div[@class="li_txt"]'):

            #一个老师的数据
            item = ItcastItem()
            
            teacher_name = site.xpath('h3/text()').extract()
            teacher_level = site.xpath('h4/text()').extract()
            teacher_info = site.xpath('p/text()').extract()

            print teacher_name[0]
            print teacher_level[0]
            print teacher_info[0]
            print "====================="
        
            item['name'] = teacher_name[0]
            item['level'] = teacher_level[0]
            item['info'] = teacher_info[0]

            items.append(item)

        return items
            

    
