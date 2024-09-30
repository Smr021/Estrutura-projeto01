import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():
    # Instanciando classe pessoa.
    pessoa = Pessoa("Marta",22,Sexo.FEMININO)
    return pessoa

def test_pessoa_mudar_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == 'Marta'

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22

def test_pessoa_idade_negativa():
    with pytest.raises(ValueError, match="A idade não pode ser negativa "):
        Pessoa("Marta",-23,Sexo.FEMININO)

def test_idade_acima_de_130_retorna_mensagem():
    with pytest.raises(ValueError, match="A idade não pode ser acima de 130 anos "):
        Pessoa("Marta",131,Sexo.FEMININO)

def test_pessoa_idade_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A idade de ser um numero inteiro. "):
        Pessoa("Marta","131",Sexo.FEMININO)


    # assert verificação usa como verdade o que foi estabelicido
    # quando quiser testar o codigo. digite no terminal: pytest