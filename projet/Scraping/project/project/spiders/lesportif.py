import scrapy


class LesportifSpider(scrapy.Spider):
    name = "lesportif"
    allowed_domains = ["lesportif.com.tn"]
    start_urls = ["https://lesportif.com.tn/10-homme-tunisie"]


    def parse(self, response):
      for item in response.css('article.product-miniature.js-product-miniature'):
        try:
          yield{
           'name':response.xpath('//*[@id="js-product-list"]/div[*]/div/div/div[*]/article/div/div[*]/h3/a/text()').extract(),
           'regular-price':item.xpath('//*[@id="js-product-list"]/div[*]/div/div/div[*]/article/div/div[*]/div[*]/span[*]/text()').extract(),
           'price' :item.css('span.regular-price::text').get(),
           'link':item.css('a.next.js-search-link').attrib['href'],

        }
        except:
         yield{
            'name':item.xpath('//*[@id="js-product-list"]/div[*]/div/div/div[*]/article/div/div[*]/h3/a/text()').extract(),
            'price' :'sold out',
            'link':item.css('a.next.js-search-link').attrib['href'],
        }
      next_page = response.css('a.next.js-search-link').attrib['href']
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
        