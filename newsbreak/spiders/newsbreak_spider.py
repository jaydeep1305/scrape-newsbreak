import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class NewsbreakSpiderSpider(CrawlSpider):
    name = "newsbreak_spider"
    allowed_domains = ["newsbreak.com"]
    start_urls = ["https://newsbreak.com"]

    rules = (
        Rule(LinkExtractor(allow="https://www.newsbreak.com/", unique=True), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.css('title::text').get()
        domain = response.css('body').re('articleDomain":"(.*?)"')
        yield {'domain': domain, 'url': response.url}

