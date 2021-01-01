#scrappy startproject gundam_spider.py
import scrapy


class GundamSpider(scrapy.Spider):
    name = "gundam"
    start_urls = [
        'https://hobbyholics.com/model-kits/high-grade-1-144/?sort=featured&page=1',
    ]

    def parse(self, response):
        def is_availabile(availability):#if add to cart True else false
            if(availability == "Add To Cart"):
                return "Available"
            else:
                return "Unavailable"

        for product_list in response.css('ul.ProductList li'):
            yield {
                'name': product_list.css('a.pname::text').get(),
                'price': product_list.css('em.p-price::text').get(), 
                'availability': is_availabile(product_list.css('a.btn::text').get()),
                'link': product_list.css('a.pname::attr(href)').get()
            }
        
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

        #for a in response.css('ul.pager a'):
        # yield response.follow(a, callback=self.parse)

        next_page = response.css('a.nav-next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
########
#run: scrapy crawl quotes
#store: scrapy crawl quotes -O quotes.json
#view(response)
#response.css('title::text')[0].get()
#scrapy shell 'http://quotes.toscrape.com'
#response.css('li.next a').attrib['href']