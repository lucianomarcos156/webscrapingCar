from bs4 import BeautifulSoup as bs
import random
import cfscrape
import time

class ParsePage:

    def main_page(self, uf): # Página do site da Olx específica de carros "particulares"
        self.url_main_page = f'https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/estado-{uf}?f=p' 

    def content_page(self, url_page):
        self.url_page = url_page
        user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36']
        user_agent = random.choice(user_agent)
        headers = {'User-Agent': user_agent}   
        scrape = cfscrape.create_scraper()
        self.get_page = scrape.get(self.url_page, headers=headers)
        self.soup_page = bs(self.get_page.content, 'html.parser')
        time.sleep(10) 