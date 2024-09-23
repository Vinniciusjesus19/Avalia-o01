from models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self, Longradouro; str, numero:str, complemento:str, cep:str, cidade:str, uf: unidadeFederativa)-> None:
    self.longradouro = Longradouro
    self.numero = numero
    self.complemento = complemento
    self.cp = cep
    self.cidade = cidade
    self.uf = uf 
    
    def __str__(self) -> str:
        return (f"{self.logradouro}"), (f"{self.numero}"), (f"{self.complemento}"), (f"{self.cep}"), (f"{self.cidade}")/(f"{self.uf.value}")
