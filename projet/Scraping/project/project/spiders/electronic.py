import scrapy


class ElectronicSpider(scrapy.Spider):
    name = "electronic"
    allowed_domains = ["phonestoretn.tn"]
    start_urls = ["https://phonestoretn.tn/promotions"]

    def parse(self, response):
      for item in response.css('article.product-miniature.js-product-miniature'):
        try:
          yield{
           'name':item.css('.product_name::text').get(default='not-found'),
           'regular-price':item.css('span.regular-price::text').get().replace('\xa0',' '),
           'price' :item.css('span.price::text').get().replace('\xa0',' '),
           'link':item.css('a.product_name').attrib['href'],

        }
        except:
         yield{
            'name':item.css('.product_name::text').get(default='not-found'),
            'price' :'sold out',
            'link':item.css('a.product_name').attrib['href'],
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
