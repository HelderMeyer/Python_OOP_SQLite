#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO
#Exemplo de uso
helder = Pessoa(1, "Helder Meyer")
print(helder)
#Quero mostrar só nome
print(helder.nome)
#Chama o objeto de banco de dados
db = Database()
#Instancia o objeto pessoadao
pessoaDAO = PessoaDAO(db.conexao, db.cursor)
#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll()
for pessoa in pessoas:
  print(pessoa)