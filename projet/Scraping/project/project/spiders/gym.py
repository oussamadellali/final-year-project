import scrapy


class GymSpider(scrapy.Spider):
    name = "gym"
    allowed_domains = ["https://www.syphax-trade.com/"]
    start_urls = ["https://www.syphax-trade.com/special?limit=100"]

    def parse(self, response):
      for item in response.css('div.js-product-miniature-wrapper.col-12'):
        try:
          yield{
           'name':item.css('div.description::text').get(),
           'regular-price':item.css('span.price-old::text').get().replace('\xa0',' '),
           'price' :item.css('span.price-new::text').get().replace('\xa0',' '),
          # 'link':item.xpath('//*[@id="js-product-list"]/div[*]/div[1]/article/div/div[2]/h2/a/@href').get(),

        }
        except:
         yield{
            'name':item.css('div.description::text').get(),            'price' :'sold out',
          # 'link':item.xpath('//*[@id="js-product-list"]/div[*]/div[1]/article/div/div[2]/h2/a/@href').get(),
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)