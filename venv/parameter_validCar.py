from treat_data import ConvertValue
import re

class FactorReference:

    def __init__(self, index_dic, option_start):
        self.index_dic = index_dic
        self.option_start = option_start
    
    def option_value(self): # Informa os parâmetros que servem de base para definir se o anúncio é viável
        print('\n>>>>>>>> Eis os parâmetros pré-definidos para avaliação dos anúncios')
        for i in range(len(self.index_dic['percentages'])):
            print('\nFaixa: ', i + 1)              
            treat = ConvertValue()
            value_start = self.index_dic['values'][i]
            treat.format_decimal(value_start)
            value_start = treat.value
            value_end = self.index_dic['values'][i + 1]
            treat.format_decimal(value_end)
            value_end = treat.value
            print(f'Valor do anúncio entre: {value_start} Até: {value_end}')
            print('Margem de lucro bruta estipulada entre o valor do anúncio e o preço da tabela Fipe ou o preço médio Olx (%): ', int((self.index_dic['percentages'][i])*100))
        option_1 = ' '
        while not re.findall(r'^[S|N]{1}$', option_1):
            option_1 = input('\nQuer realmente alterar estes valores (S/N)? ').upper()    
        if option_1 == 'S':
            self.new_value()
        else:
            return
 
    def new_value(self): # Permiti alterar os valores dos parâmetros que são base para escolha do anúncio
        print('\nDIGITE OS NOVOS VALORES')
        del self.index_dic['values'][1:]
        self.index_dic['percentages'].clear()
        idx = 0
        while True:
            print('\nFaixa: ', idx + 1)
            print('Valor do anúncio entre: ', self.index_dic['values'][idx])
            range_value = 0
            margin_profit = 0
            range_value = input('Até: ')
            margin_profit = input('Percentual da margem de lucro bruta (%): ')                       
            option_2 = ' '
            while not re.findall(r'^[S|N]{1}$', str(option_2)):
                option_2 = input('\nConfirma estes valores (S/N)? ').upper()
            if option_2 == 'S' and re.findall(r'\d{1,2}', margin_profit) and re.findall(r'\d{4,6}', range_value) and self.index_dic['values'][idx] < int(range_value): 
                self.index_dic['values'].append(int(range_value))
                self.index_dic['percentages'].append(int(margin_profit)/100)
                option_3 = ' '
                while not re.findall(r'^[S|N]{1}$', str(option_3)):
                    option_3 = input('\nPretende digitar outra faixa para ampliar a avaliação dos anúncios (S/N) ').upper()                    
                if option_3 == 'S':
                    idx += 1
                else:
                    break 
            elif option_2 == 'N':
                continue
            else:
                print('\nDados incorretos!')  
                print('Cada Faixa deve ser composta por um valor inicial menor que o valor final e estes valores devem possuir de 4 a 6 dígitos.')
                print('O percentual correspondente a margem de lucro bruta deve ser um numeral composto de 1 a 2 dígitos')
