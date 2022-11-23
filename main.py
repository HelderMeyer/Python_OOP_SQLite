#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
#Exemplo de uso
helder = Pessoa(1, "Helder Meyer")
print(helder)
#Quero mostrar só nome
print(helder.nome)