# Basico FastAPI Auth

Projeto inicial de API com FastAPI e configuração centralizada via `BaseSettings` (Pydantic) e variáveis de ambiente (`.env`).

## Instalacoes realizadas

Pacotes que já aparecem no código atual:

- `fastapi` - framework para criar APIs HTTP de forma rápida e tipada.
- `python-decouple` - separa configurações do código, lendo variáveis do `.env`.
- `pydantic` - valida dados e modelos com tipos Python.
- `pydantic-settings` - gerencia configurações da aplicação via `BaseSettings` no Pydantic v2.
- `beanie` - ODM assíncrono para modelar e acessar documentos no MongoDB.

Comando para instalar tudo de uma vez:

```bash
pip install fastapi python-decouple pydantic pydantic-settings beanie
```

Para salvar as dependências atuais no arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```
