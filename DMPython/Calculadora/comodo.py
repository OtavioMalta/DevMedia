class Comodo:

    # Propriedades privadas (__x) que só são acessadas pelos Getters e Setters
    #__largura:float
    #__profundidade:float
    #__altura:float

    # Construtor
    def __init__(self, largura, profundidade):
        # Largura e Profundidade fazem referêcia aos Getters -> Setters
        self.largura = largura
        self.profundidade = profundidade

        # Altura não faz referência aos Setters, por isso precisa ser precisa setar direto nas propriedades privas diretamente
        self.__altura = 2.9
        
    #Getters - Pegam os valores e retornam    
    @property
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura
    
    #Setters - Atribuem valores as propriedades 
    @largura.setter
    def largura(self, valor):

        #1-Tenta atribuir
        try:
            self.__largura = float(valor)
        #2-Caso não consiga e encontre um erro (Exception), retorna um print
        except Exception:
            print("[ERRO] Parâmetro Inválido!")
            exit()

    @profundidade.setter
    def profundidade(self, valor):
        try:
            self.__profundidade = float(valor)

        except Exception:
            print("[ERRO] Parâmetro Inválido!")
            exit()
