import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular#D[A:celular]"]

    def parse(self, response):
        products = response.css('div.ui-search-result__wrapper')

        for product in products:
            yield {
                'categoria' : product.css('span.poly-component__seller::text').get()
            }

