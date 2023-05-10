import re

class DefinedParameters:

    def __init__(self, uf, option_sapp, option_start, contato_sapp):
        self.uf = uf
        self.option_sapp = option_sapp
        self.option_start = option_start
        self.contato_sapp = contato_sapp
          
    def data_viableCar(self):

        print('\nCollectData_car é uma ótima ferramenta para captar anúncios de veículos na Web') # Neste momento o código está configurado para coletar anúncios de veículos na Olx
        print('________________________________________________________________________________')
        print('\n>>>>>>>> O código deste aplicativo está configurado para realizar buscas no site da Olx podendo ser modificado para um outro site')
        while not re.findall(r'^[a-zA-Z]{2}$', self.uf):
            self.uf = input('\n>>>>>>>> Informe em que estado da federação deve ser realizado a pesquisa digitando apenas duas letras(UF): ').lower()  
        while not re.findall(r'^[S|N]{1}$', self.option_start):
            self.option_start = input('\n>>>>>>>> Deseja modificar os parâmetros que define a viabilidade de compra do veículo (S/N)? ').upper()  

    def data_msnSapp(self):
        while not re.findall(r'^[S|N]{1}$', self.option_sapp):
            self.option_sapp = input('\n>>>>>>>> Os dados ora coletados devem ser enviados para o seu Whatsapp e/ou um outro contato de sua agenda (S/N)? ').upper() # Defini se as informações coletadas serão enviadas pelo Whatsapp
        if self.option_sapp == 'S': 
            option_contact = ' '
            while option_contact != 'N':
                contact = ' '
                option_contact = ' '
                while not re.match(r'^\+55\d{2}\d{4}\d{4}$', contact):
                    contact = input('\n>>>>>>>> Digite o número do DDD(XX) e depois o celular(XXXX-XXXX) sem o 9: ') # 
                    contact = ('+55'+ contact)
                if contact not in self.contato_sapp:
                    self.contato_sapp.append(contact)
                else:
                    print('\n>>>>>>>> Contato já cadastrado!')
                while not re.findall(r'^[S|N]{1}$', option_contact):
                    option_contact = input('\nDeseja incluir outro número(S/N)? ').upper()  
        else:
            return

