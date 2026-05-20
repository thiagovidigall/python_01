from fastapi import FastAPI
from core.config import settings  # `core.config` = pacote.arquivo (como `from core/config.ts` no TS); aqui importamos o objeto `settings` definido nesse modulo
from beanie import init_beanie  # função para inicializar o Beanie com o MongoDB
from pymongo import AsyncMongoClient  # cliente assíncrono oficial do PyMongo (compatível com Beanie 2.x)
import uvicorn  # servidor ASGI para executar a aplicação FastAPI

from models.user_model import User  # importa o modelo User
from api.api_v1.router import router

# instancia aqui no app.py para garantir que as variáveis de ambiente sejam lidas e validadas antes de usar
# não precisou pois já havia feito no core/config.py, onde criamos a instância `settings` logo após a definição da classe Settings. Assim, ao importar `settings` em app.py, já temos a instância pronta para uso.
## from core.config import Settings  # importa a classe, não a instância
## settings = Settings()  

app = FastAPI(
    title=settings.PROJECT_NAME,  # usa o nome do projeto definido no settings
    # OpenAPI em /openapi.json (padrão). Evita /docs carregar JSON antigo em /api/v1/openapi.json (cache).
    # openapi_url=f"{settings.API_V1_STR}/openapi.json"  # define a URL do OpenAPI usando a versão da API do settings    
)

@app.on_event("startup")
async def app_init():
    # Inicializa o cliente MongoDB e o Beanie
    client = AsyncMongoClient(settings.MONGO_CONNECTION_STRING)
    database = client[settings.MONGO_DATABASE_NAME]
    await init_beanie(
        database=database,
        document_models=[
            User
        ])  # aqui passamos os modelos de documento do Beanie, se tivéssemos algum definido


app.include_router(
    router, 
    prefix=settings.API_V1_STR
    )

