import scrapy


class CosmetiqueSpider(scrapy.Spider):
    name = "cosmetique"
    allowed_domains = ["cosmetica.tn"]
    start_urls = ["https://cosmetica.tn/vente-flash"]

    def parse(self, response):
      for item in response.css('li.item.product.product-item.nth-child-2np1.nth-child-3np1.nth-child-4np1.nth-child-5np1.nth-child-6np1.nth-child-7np1.nth-child-8np1'):
        try:
          yield{
           'name':item.css('a.product-item-link::text').get(),
           'regular-price':item.css('span.price::text').get().replace('\xa0',' '),
           'price' :item.css('span.price.price_sale::text').get().replace('\xa0',' '),
           'link':item.css('a.action.next').attrib['href'],

        }
        except:
         yield{
            'name':item.css('a.product-item-link::text').get(),
            'price' :'sold out',
            'link':item.css('a.action.next').attrib['href'],
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)