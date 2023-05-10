from treat_data import ConvertValue
from datetime import datetime
import re
import time
import json

class DataAdverts:

    feature_dic = {}

    def collect_feature(self, soup_page, get_page, url_page, inconsistency):
        self.soup_page = soup_page 
        self.get_page = get_page
        self.url_page = url_page
        self.inconsistency = inconsistency
        try:
            data_json = self.soup_page.find(id='initial-data').get('data-json') 
            self.data = json.loads(data_json)
            self.brandmodel_car = self.soup_page.find_all('a',class_='sc-gPWkxV dsTsUE')[2].text
            self.municipality_car = self.data['ad']['locationProperties'][1]['value']
            condition_year = self.data['ad']['properties'][4]['value']
            ano_atual = datetime.now().year
            if not re.findall(r'[^0-9]*', str(condition_year)) or len(condition_year) != 4 or int(condition_year) > ano_atual:
                self.year_car = self.data['ad']['properties'][3]['value']
            else:
                self.year_car = self.data['ad']['properties'][4]['value']
            try:
                self.priceadvert = self.data['ad']['priceValue']
                if self.priceadvert == None or self.priceadvert == []: self.priceadvert = '0'
            except:
                self.priceadvert = '0'
            try:
                self.pricefipe = str(self.data['ad']['abuyFipePrice']['fipePrice'])
                if self.pricefipe == None or self.pricefipe == []: self.pricefipe = '0'
            except:
                self.pricefipe = '0' 
            try:
                self.priceaverage = str(self.data['ad']['abuyPriceRef']['price_p50'])
                if self.priceaverage == None or self.priceaverage == []: self.priceaverage = '0'
            except:
                self.priceaverage = '0'
            self.feature_save()
            self.inconsistency = False
        except:
            self.inconsistency = True
        time.sleep(2)
        self.get_page.close()

    def feature_save(self): # Relaciona as características de cada anúncio
        treat = ConvertValue()
        treat.format_decimal(self.priceadvert)
        priceadvert_car = treat.value
        treat.format_decimal(self.pricefipe)
        pricefipe_car = treat.value
        treat.format_decimal(self.priceaverage)
        priceaverage_car = treat.value
        self.feature_dic = {
            'brandmodel_car': self.brandmodel_car,
            'municipality_car':self.municipality_car,
            'year_car':self.year_car,
            'priceadvert_car':priceadvert_car,
            'pricefipe_car':pricefipe_car,
            'priceaverage_car':priceaverage_car,
            'url_car': self.url_page
        }