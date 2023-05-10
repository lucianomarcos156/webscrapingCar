from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from parameter_startSystem import DefinedParameters
from parameter_validCar import FactorReference
from request_page import ParsePage
from scrape_advertPost import CollectAdvert
from scrape_advertFeature import DataAdverts
from select_advertViable import ClassificationAdvert
from send_message import MessageWhatsapp
import time

while True:
    uf=''
    option_sapp=''
    option_start=''
    contato_sapp=[]
    start = DefinedParameters(uf, option_sapp, option_start, contato_sapp)
    start.data_viableCar()
    uf = start.uf
    option_start = start.option_start
    percentages = [0.25, 0.23, 0.21, 0.19, 0.17, 0.15, 0.14, 0.13, 0.13, 0.15]
    values = [8000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 150000] 
    index_dic = {
        'percentages': percentages,
        'values': values
        }  
    if option_start == 'S':     
        set = FactorReference(index_dic, option_start) 
        set.option_value()
        index_dic = set.index_dic 
    else:
        print('\n>>>>>>>> Parâmetros inalterados!')
    start.data_msnSapp()
    option_sapp = start.option_sapp
    contato_sapp = start.contato_sapp
    if option_sapp == 'S':
        print('\n>>>>>>>> Realize a leitura do QRCode para ativar o Whatsapp Web\n') 
        global page_global 
        page_global = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=Options())
        page_global.get('https://web.whatsapp.com')
        while len(page_global.find_elements(By.ID, 'pane-side')) < 1:
            time.sleep(2)
    else:
        print('\n>>>>>>>> As informações coletadas serão exibidas apenas na tela do seu desktop')
    oferta = 0
    try:
        message_set = []
        while True:
            item = 1 
            page = ParsePage()
            page.main_page(uf)
            url_page = page.url_main_page
            page.content_page(url_page)
            get_page = page.get_page
            soup_page = page.soup_page
            select = CollectAdvert()
            print('\n>>>>>>>> Captando endereços de anúncios recém postados...')
            select.url_advertPost(soup_page, get_page)
            url_advert = select.url_advert
            for url_page in url_advert:
                if url_page != []:
                    page.content_page(url_page)
                    get_page = page.get_page
                    soup_page = page.soup_page
                    inconsistency = False
                    scrape = DataAdverts()
                    scrape.collect_feature(soup_page, get_page, url_page, inconsistency)  
                    feature_dic = scrape.feature_dic 
                    inconsistency = scrape.inconsistency
                    print('\nItem:', item)
                    print('Url: ', url_page)
                    item += 1
                    if (inconsistency == False and feature_dic['priceadvert_car'] > 0) and (feature_dic['pricefipe_car'] > 0 or feature_dic['priceaverage_car'] > 0):   
                        check = ClassificationAdvert() 
                        check.filter_advert(index_dic, feature_dic) 
                        msn = check.msn
                        check.viable_advert(access=False)
                        viableads_dic = check.viableads_dic
                        sapp = MessageWhatsapp() # Envio das informações via Whatsapp(opcional)
                        if option_sapp == 'S' and msn == True: 
                            if url_page not in message_set:
                                oferta += 1
                                sapp.send_message(oferta, contato_sapp, feature_dic, viableads_dic, page_global)
                                message_set.append(viableads_dic['url_car'])
                            else:
                                print('\n>>>>>>>> Item já captado...')
                        else: 
                            continue
                    else:
                        print('>>>>>>>> Avaliação impossibilitada devido a ausência de informações fundamentais como Preço de venda / Preço Fipe / Preço médio) ')
                else:
                    break
    except:
        print('\n>>>>>>>> O APLICATIVO ESTÁ SENDO REINICIADO DEVIDO A PROBLEMAS NA CONEXÃO COM A INTERNET OU CONFIGURAÇÃO DO NAVEGADOR')
        time.sleep(10)  



