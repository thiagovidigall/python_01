from pymongo import MongoClient

#vai usar padrão mas poderia ser: MongoClient("mongodb://localhost/27017/")
# outra coisa não possou o banco entao sera usado o default: local
# ficano do formato banco.nome_da_colecao = local.jogador

#sem senha ao subir o mongo
#conexao = MongoClient()

conexao = MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")

