class Produto:  # Classes começam com letra maiúscula

    #Construtor
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    #Getters
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    #Setters
    @nome.setter
    def nome(self, vl_nome):
        self.__nome = str(vl_nome)

    @preco.setter
    def preco(self, vl_preco):
        #Se for uma string: Retira os espaços(strip(' ')) e troca o 'R$' por vazio
        if isinstance(vl_preco, str):
            vl_preco = float(vl_preco.strip(' ').replace('R$',''))
        
        #Tratamento de erro
        try: 
            self.__preco = float(vl_preco)

        except Exception:
            print("[ERRO] Valores inválidos para Preco!")