from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class MessageWhatsapp:

    field_contact = ' '
    field_message = ' '
    navegador_sapp = ' '

    def send_message(self, oferta, contato_sapp, feature_dic, viableads_dic, page_global): # Envio de mensagem para o número previamente definido
        for contact_list in contato_sapp:
            self.field_contact = page_global.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
            self.field_contact.send_keys(contact_list, Keys.ENTER)
            time.sleep(2)                               
            self.field_message = page_global.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            self.field_message.send_keys('****** OFERTA:  ', oferta,'\nMunicípio: ', feature_dic['municipality_car'],'\n', feature_dic['brandmodel_car'], ' Ano: ', feature_dic['year_car'], '\nValor Anunciado: ', viableads_dic['valueadvert'], '\nVl Médio no Site: ', viableads_dic['valueaverage'], '\nTabela FIPE: ', viableads_dic['valuefipe'], '\nMargem Bruta: ', viableads_dic['grossmargin'], '\nLink: ', feature_dic['url_car'], Keys.ENTER) 
            time.sleep(2)



