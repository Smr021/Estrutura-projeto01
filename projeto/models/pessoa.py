from projeto.models.enums.sexo import Sexo

class Pessoa:
    def __init__(self,nome:str,idade:int,sexo:Sexo) -> None:
        self._nome = nome
        self._idade = idade
        self._sexo = sexo

    
    def _verificar_idade(self,idade):
        if idade < 0:
            self._idade = 0
        else:
            self._idade = idade

    def __str__(self) -> str:
        return (
            f"\n Nome: {self._nome}"
            f"\n Idade: {self._idade}"
            f"\n Sexo: {self._sexo}"
            )