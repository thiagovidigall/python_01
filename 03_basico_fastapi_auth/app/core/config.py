# configurações iniciais
# pip install python-decouple

from typing import List  # fornece tipagem para listas
from decouple import config  # lê variáveis de ambiente e arquivo .env
from pydantic import AnyHttpUrl  # tipo para validar URLs HTTP
from pydantic_settings import BaseSettings  # em Pydantic v2, BaseSettings foi movido para este pacote

class Settings(BaseSettings):  # em TS seria como "extends BaseSettings": aqui é herança da classe, não parâmetro
    PROJECT_NAME: str = 'TODOFast'  # nome do projeto
    API_V1_STR: str = '/api/v1'  # versão da API
    # Configurações de segurança
    JWT_SECRET_KEY: str = config('JWT_SECRET_KEY', cast=str)  # cast=str força leitura como texto, evitando tipo inesperado vindo do .env
    JWT_REFRESH_SECRET_KEY: str = config('JWT_REFRESH_SECRET_KEY', cast=str)  # chave para tokens de refresh
    ALGORITHM: str = 'HS256'  # algoritmo de criptografia
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # tempo de expiração do token
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # expiração do token de refresh (7 dias)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []  # origens permitidas para CORS
    # Configurações do banco de dados
    MONGO_CONNECTION_STRING: str = config('MONGO_CONNECTION_STRING', cast=str)  # só host/porta/credenciais; o nome do banco fica em MONGO_DATABASE_NAME
    MONGO_DATABASE_NAME: str = config('MONGO_DATABASE_NAME', default='todo', cast=str)

    class Config:  # classe interna (nested class): usada pelo Pydantic para configurar o comportamento desta classe Settings
        case_sensitive = True  # metaconfiguracao: nomes de variaveis de ambiente ficam sensiveis a maiusculas/minusculas

# Padrao de uso parecido com Singleton: criamos uma vez no modulo e reutilizamos via import.
# Em TS seria equivalente a: export const settings = new Settings()
# Nao impede criar outra instancia, mas no projeto tratamos esta como a instancia global.
settings = Settings()
    
