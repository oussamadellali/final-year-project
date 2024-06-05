import scrapy


class PeaksSpider(scrapy.Spider):
    name = "cosmetica"
    
    start_urls = ["https://cosmetica.tn/vente-flash"]

    def parse(self, response):
      for item in response.css('div.product.details.product-item-details'):
        try:
          yield{
           'name':item.xpath('//*[@id="layer-product-list"]/div[*]/ol/li[*]/div/div[2]/strong/a/text()').get(),
           'regular-price':item.css('span.regular-price::text').get().replace('\xa0',' '),
           'price' :item.css('span.price.price_sale::text').get().replace('\xa0',' '),
           'link':item.xpath('//*[@id="layer-product-list"]/div[*]/ol/li[*]/div/div[2]/strong/a/@href').get(),
           'imageurl':item.xpath('/html/body/main/section/div/div/div[2]/section/section/div[3]/div/div/div[*]/article/div[*]/a/img/@src').get()

        }
        except:
         yield{
            'name':item.css('a.product_name::text').get(),
            'price' :'sold out',
            'link':item.css('a.product_name').attrib['href'],
            'imageurl':item.xpath('/html/body/main/section/div/div/div[2]/section/section/div[3]/div/div/div[*]/article/div[*]/a/img/@src').get()
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)