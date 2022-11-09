import scrapy
from scrapy.crawler import CrawlerProcess
from ast import literal_eval
import os


class PageScraper(scrapy.Spider):


    name = 'PageScraper'

    start_urls = ['https://abcnews.go.com/Health/Coronavirus']

    def parse(self, response, **kwargs):
        # Check if there is a file with saved urls, if not, create a new set
        url_file_exists = os.path.isfile('visited_urls.txt')
        if url_file_exists:
            with open('visited_urls.txt', 'r') as f:
                visited_articles_urls = literal_eval(f.read())
        else:
            visited_articles_urls = set()

        # Scrape articles
        for item_url in response.css('div.band__common a.AnchorLink::attr(href)'):
            url = response.urljoin(item_url.get())
            if url not in visited_articles_urls:
                visited_articles_urls.add(url)
                yield response.follow(url=url, callback=self.parse_articles)

        # Save visited url's in a file for later use
        with open('visited_urls.txt', 'w') as f:
            f.write(str(visited_articles_urls))

    def parse_articles(self, response):
        page = response.url.split("/")[-2]
        filename = f'article-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)


process = CrawlerProcess()
process.crawl(PageScraper)
process.start()