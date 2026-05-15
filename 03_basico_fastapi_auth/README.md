# Basico FastAPI Auth

Projeto inicial de API com FastAPI e configuração centralizada via `BaseSettings` (Pydantic) e variáveis de ambiente (`.env`).

## Ambiente virtual (somente dentro de `app/`)

Crie e use o `.venv` **na pasta `app`**, não na raiz do repositório:

```bash
cd app
python -m venv .venv
```

Windows (PowerShell), ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

Depois: `pip install -r requirements.txt`

### Cursor / VS Code (extensão Python)

- **Interpretador:** `Ctrl+Shift+P` → **Python: Select Interpreter** (em PT-BR pode aparecer como **Python: Selecionar interpretador**) → escolha `app\.venv\Scripts\python.exe`. A escolha fica salva no workspace.
- **Terminal:** nas configurações do editor, ative **Python › Terminal: Activate Environment** (em PT-BR o rótulo segue em inglês na busca: digite `Python Terminal Activate`) para que terminais novos já entrem no `.venv` automaticamente.

## Configuração (`.env`)

Crie o arquivo **`app/.env`** (mesma pasta que `app.py` e `requirements.txt`). O `python-decouple` lê essas variáveis na subida da API:

| Variável | Obrigatória | Descrição |
|----------|-------------|-----------|
| `JWT_SECRET_KEY` | sim | Chave secreta para assinar tokens de acesso. |
| `JWT_REFRESH_SECRET_KEY` | sim | Chave para tokens de refresh. |
| `MONGO_CONNECTION_STRING` | sim | URI do MongoDB (ex.: `mongodb://usuario:senha@host:27017/?authSource=admin`). |
| `MONGO_DATABASE_NAME` | não | Nome do banco de dados lógico; padrão no código é `todo` se omitida. |

## E-mail no Pydantic (`EmailStr`)

O modelo de usuário usa o tipo **`EmailStr`**, que exige dependências extras:

- **`email-validator`** — valida formato de e-mail em tempo de validação do Pydantic.
- **`pydantic[email]`** — extra do pacote `pydantic` que declara essa dependência (equivalente a instalar `pydantic` já com suporte a e-mail).

No PowerShell ou bash, use aspas no extra para o shell não interpretar os colchetes:

```bash
pip install "pydantic[email]" email-validator
```

O arquivo **`requirements.txt`** já fixa versões compatíveis (`pydantic[email]` + `email-validator`).

## Instalacoes realizadas

Pacotes que já aparecem no código atual:

- `fastapi` - framework para criar APIs HTTP de forma rápida e tipada.
- `python-decouple` - separa configurações do código, lendo variáveis do `.env`.
- `pydantic` - valida dados e modelos com tipos Python.
- `pydantic[email]` + `email-validator` - necessários para `EmailStr` nos modelos (ver seção acima).
- `pydantic-settings` - gerencia configurações da aplicação via `BaseSettings` no Pydantic v2.
- `beanie` - ODM assíncrono para modelar e acessar documentos no MongoDB.


Comando para instalar tudo de uma vez:

```bash
pip install fastapi python-decouple "pydantic[email]" pydantic-settings beanie email-validator
```

## Executar a API

Na pasta **`app`** (onde está o módulo `app.py`):

```bash
uvicorn app:app --host 0.0.0.0 --port 8081 --reload
```

Ou: `python app.py` (usa host/porta definidos no `if __name__ == "__main__"`).

Para salvar as dependências atuais no arquivo `requirements.txt`:

```bash
pip freeze > requirements.txt
```
