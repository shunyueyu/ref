import scrapy
from ..items import NoveldownloadItem

class NovelSpider(scrapy.Spider):
    name = "novel"
    # allowed_domains = ["wap.bqbwx.cc"]
    # start_urls = ["https://wap.bqbwx.cc/53/53190/488294265.html"]
    allowed_domains = ["www.26ks.cc"]
    start_urls = ["http://www.26ks.cc/book/24023/"]


    def parse(self, response):
        chapters = response.xpath('//*[@id="list"]/dl/dd/a/@href').getall()
        #print("http://www.26ks.cc" +chapters[192])
        for chapter_url in chapters[192:300]:
            yield response.follow("http://www.26ks.cc" + chapter_url, self.parse_chapter)

    def parse_chapter(self, response):
        novel_item = NoveldownloadItem()
        novel_item['title'] = response.xpath('/html/head/title/text()').get().replace('_玄幻小说_爱豆看书网',"").replace(' ','').replace("\r\n",'')
        novel_item['content'] = response.xpath('//*[@id="content"]/p/text()').getall()
        novel_item['detail'] = " ".join(novel_item['content'][1:]).replace(' ','').replace("\r",'')

        yield {
               "base_path": "aaa/",
               "title":novel_item['title'],
               "content":novel_item['detail']
               }
