from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from book_scraper_tutorial_project.bookscraper.items import BookscraperItem


class BookScraper(CrawlSpider):
    name = 'book_scraper_tutorial_project'
    start_urls = ['http://books.toscrape.com']

    rules = [
        Rule(LinkExtractor(restrict_css='.nav-list > li > ul > li > a'), follow=True),
        Rule(LinkExtractor(restrict_css='.product_pod > h3 > a'), callback='parse_book')

    ]

    def parse_book(self, response):
        book_item = BookscraperItem()

        book_item['image_url'] = response.urljoin(response.css('.item.active > img::attr(src)').get())
        book_item['title'] = response.css('div.col-sm-6.product_main > h1::text').get()
        book_item['price'] = response.css('div.row div.col-sm-6.product_main p.price_color::text').get()
        book_item['upc'] = response.css('table.table-striped > tr:nth-child(1) > td::text').get()
        # html.no-js.alxmeajbo.idc0_344 body#default.default div.container-fluid.page div.page_inner div.content div#content_inner article.product_page table.table.table-striped tbody tr td
        # .table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)
        book_item['url'] = response.url

        return book_item

process = CrawlerProcess(settings={
    "FEEDS": {
        "scraped_items.json": {"format": "json"},
    },
})

process.crawl(BookScraper)
process.start()

