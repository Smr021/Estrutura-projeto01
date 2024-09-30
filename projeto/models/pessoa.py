from projeto.models.enums.sexo import Sexo

class Pessoa:
    def __init__(self,nome:str,idade:int,sexo:Sexo) -> None:
        self.nome = nome
        self.idade = self._verificar_idade(idade)
        self.sexo = sexo

    
    def _verificar_idade(self,valor):
        self._verificar_idade_tipo_invalido(valor)
        self._verificar_idade_negativa(valor)
        self._verificar_idade_acima_de_130(valor)

        self.idade = valor
        return self.idade


    def _verificar_idade_tipo_invalido(self,valor):
        if not isinstance(valor,int):
            raise TypeError("A idade de ser um numero inteiro. ")
    
    def _verificar_idade_negativa(self,valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa ")

    def _verificar_idade_acima_de_130(self,valor):
         if valor > 130:
            raise ValueError("A idade não pode ser acima de 130 anos ")


    def __str__(self) -> str:
        return (
            f"\n Nome: {self.nome}"
            f"\n Idade: {self.idade}"
            f"\n Sexo: {self.sexo}"
            )