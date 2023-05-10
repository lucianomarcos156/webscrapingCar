class ConvertValue: # Tratando os valores para serem apresentados no formato padrão(0,00)

    def format_decimal(self, value):
        if isinstance(value, str): 
            value = (value.replace('R$','').replace('.','').replace(',','')).strip()
            value = int(value)
        else:
            value = float(value)
            value = f'{value:_.2f}'
            value = (value.replace('.',',').replace('_','.')).strip()
        self.value = value