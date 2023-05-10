import re
import time

class CollectAdvert:

    def url_advertPost(self, soup_page, get_page):
        self.soup_page = soup_page
        self.get_page = get_page
        self.url_advert = []
        url = ' '
        for url in self.soup_page.find_all('a', attrs={'data-ds-component':'DS-AdCardHorizontal'}):
            url = url.get('href')
            if 'autos-e-pecas/carros-vans-e-utilitarios' in url and not re.findall(r'repasse|troco|aluguel|repasso|leilao', url):
                self.url_advert.append(url)
            else:
                print('\n>>>>>>>> Endereço descartado trata-se de anúncio relacionado a repasse / troca / aluguel / leilao')
            time.sleep(2)
        self.get_page.close()