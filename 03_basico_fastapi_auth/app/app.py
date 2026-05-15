from fastapi import FastAPI
from core.config import settings  # `core.config` = pacote.arquivo (como `from core/config.ts` no TS); aqui importamos o objeto `settings` definido nesse modulo
from beanie import init_beanie  # função para inicializar o Beanie com o MongoDB
from pymongo import AsyncMongoClient  # cliente assíncrono oficial do PyMongo (compatível com Beanie 2.x)
import uvicorn  # servidor ASGI para executar a aplicação FastAPI
from models.user_model import User  # importa o modelo User



# instancia aqui no app.py para garantir que as variáveis de ambiente sejam lidas e validadas antes de usar
# não precisou pois já havia feito no core/config.py, onde criamos a instância `settings` logo após a definição da classe Settings. Assim, ao importar `settings` em app.py, já temos a instância pronta para uso.
## from core.config import Settings  # importa a classe, não a instância
## settings = Settings()  

app = FastAPI(
    title=settings.PROJECT_NAME,  # usa o nome do projeto definido no settings
    openapi_url=f"{settings.API_V1_STR}/openapi.json"  # define a URL do OpenAPI usando a versão da API do settings    
)

@app.on_event("startup")
async def app_init():
    # Inicializa o cliente MongoDB e o Beanie
    client_db = AsyncMongoClient(settings.MONGO_CONNECTION_STRING).todoapp  # cria o cliente Mongo assíncrono
    # client_db = client[settings.MONGO_DATABASE_NAME]  # banco definido em settings (padrão "todo"; pode vir do .env depois)
    await init_beanie(
        database=client_db,
        document_models=[
            User
        ])  # aqui passamos os modelos de documento do Beanie, se tivéssemos algum definido

# @app.get('/')
# async def hello():
#     return {"message": "teste hello"}


#if __name__ == "__main__":
    # uvicorn.run("app:app", host="0.0.0.0", port=8081, reload=True)
