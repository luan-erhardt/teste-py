class cliente:
    def __init__(self,nome,plano,idade):
        self.nome = nome
        self.plano = plano
        self.idade = idade


cliente1 = cliente('luan','premium','23')
cliente2 = cliente('joão','basic','24')

print(cliente1.nome,cliente1.plano,cliente1.idade)

        
    