import scrapy


class AutoSpider(scrapy.Spider):
    name = "auto"
    allowed_domains = ["karhabtk.tn"]
    start_urls = ["https://www.karhabtk.tn/promotions"]

    def parse(self, response):
      for item in response.css('article.product-miniature.js-product-miniature'):
        try:
          yield{
           'name':item.css('a.h3.product-title::text').get(),
           'regular-price':item.css('span.regular-price::text').get().replace('\xa0',' '),
           'price' :item.css('span.price::text').get().replace('\xa0',' '),
           'link':item.css('a.product_name').attrib['href'],

        }
        except:
         yield{
            'name':item.css('a.product_name::text').get(),
            'price' :'sold out',
            'link':item.css('a.product_name').attrib['href'],
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
