import scrapy
from scrapy.crawler import CrawlerProcess


class BookScraper2(scrapy.Spider):
    name = 'BookScraper'

    start_urls = ['http://books.toscrape.com/', ]

    def parse(self, response, **kwargs):
        for item_url in response.css('ul.nav.nav-list > li > ul > li > a::attr(href)'):
            url = response.urljoin(item_url.get())
            yield response.follow(url=url, callback=self.parse_category)

    def parse_category(self, response):
        for item_url in response.css('article.product_pod > h3 > a::attr(href)'):
            url = response.urljoin(item_url.get())
            yield scrapy.Request(url=url, callback=self.parse_book)

    def parse_book(self, response):
        book_category = response.css('.breadcrumb > li:nth-child(3) > a:nth-child(1)::text').get()
        book_title = response.css('div.col-sm-6.product_main > h1::text').get()
        book_url = response.url
        book_price = response.css('div.col-sm-6.product_main > p.price_color::text').get()
        book_upc = response.css('table.table-striped > tr:nth-child(1) > td::text').get()
        book_img_url = response.urljoin(response.css('div.item.active > img::attr(src)').get())

        yield {
            'Book category': book_category,
            'Book title': book_title,
            'Book URL': book_url,
            'Book price': book_price,
            'Book UPC': book_upc,
            'Book image URL': book_img_url,
        }


process = CrawlerProcess(settings={
    "FEEDS": {
        "scraped_items.json": {"format": "json"},
    },
})

process.crawl(BookScraper2)
process.start()
