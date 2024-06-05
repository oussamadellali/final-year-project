import scrapy


class CosmeticSpider(scrapy.Spider):
    name = "cosmetic"
    allowed_domains = ["www.fatales.tn"]
    start_urls = ["https://www.fatales.tn/promotions"]

    def parse(self, response):
      for items in response.css('article.product-miniature.js-product-miniature.col-sp-12.col-xs-6.col-sm-4.col-md-3'):
        try:
          yield{
           'name':items.css('a.product-name::text').get(),
           'regular-price':items.css('span.regular-price::text').get().replace('\xa0',' '),
           'price' :items.css('span.price.product-price::text').get().replace('\xa0',' '),
           'link':items.css('a.product-name').attrib['href'],

        }
        except:
         yield{
            'name':items.css('a.product-name::text').get(),
            'price' :'sold out',
            'link':items.css('a.product-name').attrib['href'],
        }
      next_page=response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)