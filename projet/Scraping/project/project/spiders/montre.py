import scrapy


class MontreSpider(scrapy.Spider):
    name = "montre"
    allowed_domains = ["www.timestory.tn"]
    start_urls = ["https://www.timestory.tn/10-hommes"]

    def parse(self, response):
      for items in response.css('div.thumbnail-inner'):
        try:
          yield{
           #'name':items.xpath('//div/h1/a/text()').getall(),
           #'regular-price':items.css('span.regular-price::text').get().replace('\xa0',' '),
           #'price' :items.css('span.price::text').get().replace('\xa0',' '),
           #'link':items.xpath('//*[@id="js-product-list"]/div[1]/article[*]/div/div/div[2]/h1/a/@href').get(),

        }
        except:
         yield{
            'name':items.xpath('//div/h1/a/text()').get(),
            'price' :'sold out',
           'link':items.xpath('//*[@id="js-product-list"]/div[1]/article[*]/div/div/div[2]/h1/a/@href').get(),

        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)