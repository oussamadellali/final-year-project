import scrapy


class ElectroSpider(scrapy.Spider):
    name = "electro"
    allowed_domains = ["numedia.tn"]
    start_urls = ["https://numedia.tn/promotion-smartphone"]

    def parse(self, response):
      for item in response.css('div.product-thumb.product-equa'):
        try:
          yield{
           'name': item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[*]/h4/a/text()').get(),
           'regular-price':item.css('span.regular-price::text').get().replace('\xa0',' '),
            'price' :item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[2]/p[1]/text()').get().replace('\n',''),
            'link':item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[1]/a/@href').get(),
            'imageurl':item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[1]/a/img/@src').get()
           

        }
        except:
         yield{
           'name': item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[2]/h4/a/text()').get(),
            'price' :'sold out',
           'link':item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[1]/a/@href').get(),

            'imageurl':item.xpath('//*[@id="content"]/div[*]/div/div[*]/div/div[1]/a/img/@src').get()
        }
      next_page = response.xpath('//*[@id="content"]/div[3]/div[2]/ul/li[10]/a/@href').get()
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)