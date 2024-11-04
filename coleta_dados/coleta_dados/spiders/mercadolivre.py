import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular#D[A:celular]"]

    def parse(self, response):
        produtos = response.css('li.ui-search-layout__item.shops__layout-item')

        for product in produtos:
            precos  = product.css('span.andes-money-amount__fraction::text').getall()


            yield {'Marca' : product.css('span.poly-component__brand::text').get()
                ,'Nome'             : product.css('h2.poly-box.poly-component__title::text').get()
                ,'Vendedor'         : product.css('span.poly-component__seller::text').get()
                ,'Preco_Antigo'     : precos[0] if len(precos) > 0 else None
                ,'Preco_Novo'       : precos[1] if len(precos) > 0 else None
                ,'Perc_Off'         : product.css('span.andes-money-amount__discount::text').get()}
        