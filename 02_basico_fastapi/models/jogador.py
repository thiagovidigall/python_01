from pydantic import BaseModel

# Modelo de dados, porem esta em Maiusculo e no mongo para ser Minisculo
# ou seja, local.jogador

class Jogador(BaseModel):
    jogador_nome: str
    jogador_idade: int
    jogador_time: str