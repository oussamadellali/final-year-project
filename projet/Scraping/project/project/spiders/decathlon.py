import scrapy


class DecathlonSpider(scrapy.Spider):
    name = "decathlon"
    allowed_domains = ["decathlon.tn"]
    start_urls = ["https://www.decathlon.tn/6034-musculation-et-entrainement"]

    def parse(self, response):
      for item in response.css('li.ais-InfiniteHits-item'):
        try:
          yield{
           'name':item.css('div.col-md-12.text-center.font-weight-bold.brand-size::text').get(),
           'description':item.xpath('//*[@id="js-product-list"]/div[1]/div/ol/li[*]/div/div/div/div[*]/div[*]/div/h3/a/text()').get(),
           #'regular-price':item.css('span.regular-price::text').get().replace('\xa0',' '),
           'price' :item.css('span.price::text').get().replace('\xa0',' '),
           'link':item.xpath('//*[@id="js-product-list"]/div[1]/div/ol/li[*]/div/div/div/div[*]/div[*]/div/h3/a/@href').get(),

        }
        except:
         yield{
            'name':item.css('div.col-md-12.text-center.font-weight-bold.brand-size::text').get(),
            'price' :'sold out',
            'link':item.xpath('//*[@id="js-product-list"]/div[1]/div/ol/li[*]/div/div/div/div[*]/div[*]/div/h3/a/@href').get(),
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)