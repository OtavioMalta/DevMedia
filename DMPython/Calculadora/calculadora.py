class Calculadora:
    __area_parede:float
    __area_teto:float

    def calcular_area_paredes(self, comodo):
        self.area_parede = 2*(comodo.largura+comodo.profundidade)*comodo.altura
        return self.area_parede
    
    def calcular_area_teto(self,comodo):
        self.area_teto = comodo.largura*comodo.profundidade
        return self.area_teto
    
    def calcular_litragem(self):
        if(self.area_teto <= 0 or self.area_parede<=0):
            print("[ERRO] Valores Inválidos para calcular a litragem!")
            exit()
        else:
            return (self.area_teto + self.area_parede)/10