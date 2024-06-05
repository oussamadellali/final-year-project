import scrapy
import re
from urllib.parse import urlparse, parse_qs
class CategorySpider(scrapy.Spider):
    name = "mongodb"
    allowed_domains = ["peaksports.tn"]
    start_urls = ["https://www.peaksports.tn/promotions"]

    
    def parse(self, response):
        for item in response.css('article.js-product-miniature'):
            try:
                # Extract URL from response
                url = item.css('a.product_name').attrib['href']
                
                # Extract category from path
                path_components = urlparse(url).path.split('/')
                if len(path_components) > 1:
                    category = path_components[1]
                else:
                    category = None

                # Extract size and color from fragment
                fragment_components = urlparse(url).fragment.split('/')
                size = None
                Ssize= None
                color = None
                for component in fragment_components:
                    if re.search(r'\d+-pointure-([\w-]+)', url):
                        Ssize = component.split('-')[-1]
                    elif re.match(r'^\d*-couleur', component):
                        color = component.split('-')[-1]
                    elif re.search(r'\d*-taille-([\w-]+)',component):
                        size = component.split('-')[-1]

                yield {
                    'title': item.css('a.product_name::text').get(),
                    'discount_price': item.css('span.regular-price::text').get().replace('\xa0', '').replace(',', '.'),
                    'price': item.css('span.price.price_sale::text').get().replace('\xa0', '').replace(',', '.'),
                    'price' :item.css('span.price.price_sale::text').get().replace('\xa0',' '),
                    'link': url,
                    'imageurl': item.xpath('/html/body/main/section/div/div/div[2]/section/section/div[3]/div/div/div[*]/article/div[*]/a/img/@src').get(),
                    'category': category,
                    'size': size,
                    'shoesize':Ssize,
                    'color': color
                }
            except:
                yield {
                    'title': item.css('a.product_name::text').get(),
                    'price': None,
                    'link': item.css('a.product_name').attrib['href'],
                    'imageurl': item.xpath('/html/body/main/section/div/div/div[2]/section/section/div[3]/div/div/div[*]/article/div[*]/a/img/@src').get()
                }
        next_page = response.css('a.next.js-search-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)