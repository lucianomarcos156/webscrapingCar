from treat_data import ConvertValue

class ClassificationAdvert:   

    msn = False
    feature_save = []
    viableads_dic = {}

    def filter_advert(self, index_dic, feature_dic): # Seleciona os anúncios de acordo com os parâmetros pré-definidos
        self.index_dic = index_dic
        self.feature_dic = feature_dic
        for i, value in enumerate(self.index_dic['values']):
            if i == (len(self.index_dic['values']) - 1): 
                print('>>>>>>>> Anúncio inviável pois está fora dos parâmetros de compra previamente definidos no sistema')
                break
            elif (self.feature_dic['priceadvert_car'] > value) and (self.feature_dic['priceadvert_car'] <= self.index_dic['values'][i + 1]):
                if self.feature_dic['pricefipe_car'] != 0 and ((self.feature_dic['pricefipe_car'] - self.feature_dic['priceadvert_car']) >= (self.feature_dic['pricefipe_car'] * self.index_dic['percentages'][i])):
                    self.feature_save.append(self.feature_dic)
                    self.viable_advert(access=True)
                    self.msn = True
                    break
                elif self.feature_dic['pricefipe_car'] == 0 and ((self.feature_dic['priceaverage_car'] - self.feature_dic['priceadvert_car']) >= (self.feature_dic['priceaverage_car'] * self.index_dic['percentages'][i])):
                    self.feature_save.append(self.feature_dic)
                    self.viable_advert(access=True)
                    self.msn = True
                    break
                else:               
                    continue  
            else:
                continue  
        
    def viable_advert(self, access): # Relaciona os anúncios considerados viáveis
        if access == True:
            if self.feature_dic['pricefipe_car'] != 0:  
                grossmargin = self.feature_dic['pricefipe_car'] - self.feature_dic['priceadvert_car']
            elif self.feature_dic['pricefipe_car'] == 0:
                grossmargin = self.feature_dic['priceaverage_car'] - self.feature_dic['priceadvert_car']
            treat = ConvertValue()
            treat.format_decimal(self.feature_dic['priceadvert_car'])
            valueadvert = treat.value
            treat.format_decimal(self.feature_dic['priceaverage_car'])
            valueaverage = treat.value  
            treat.format_decimal(self.feature_dic['pricefipe_car'])
            valuefipe = treat.value   
            treat.format_decimal(grossmargin)
            grossmargin = treat.value  
            self.viableads_dic = {
                'valueadvert': valueadvert,
                'valueaverage': valueaverage,
                'valuefipe': valuefipe,
                'grossmargin': grossmargin,
                'url_car': self.feature_dic['url_car']
            }
            print('Modelo: ', self.feature_dic['brandmodel_car'], ' Ano: ', self.feature_dic['year_car'])
            print('Localização:', self.feature_dic['municipality_car'])
            print('Valor Anunciado......R$', self.viableads_dic['valueadvert'])
            print('Vl Médio no Site.....R$', self.viableads_dic['valueaverage'])
            print('Tabela FIPE..........R$', self.viableads_dic['valuefipe'])
            print('Margem Bruta.........R$', self.viableads_dic['grossmargin'])
            print('>>>>>>>>  Anúncio negociável!  <<<<<<<<')
        else:
            return self.viableads_dic