import scrapy


class CosmeqSpider(scrapy.Spider):
    name = "cosmeq"
    allowed_domains = ["www.pointm.tn"]
    start_urls = ["https://www.pointm.tn/promotions"]

    def parse(self, response):
      for item in response.css('div.product-container'):
        try:
          yield{
           'name':item.css('span.product-manufacturer-name::text').get(),
           'regular-price':item.css('span.old-price.product-price::text').get().replace('\xa0',' '),
           'price' :item.css('span.price.product-price::text').get().replace('\xa0',' '),
           'link':item.css('a.product-name').attrib['href'],

        }
        except:
         yield{
            'name':item.css('a.product_name::text').get(),
            'price' :'sold out',
            'link':item.css('a.product-name').attrib['href'],
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)