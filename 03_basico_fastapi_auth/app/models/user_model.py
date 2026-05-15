# `from beanie import Document, Indexed`:
# - `from ... import ...` traz nomes definidos em outro módulo para usar aqui sem prefixo.
# - `beanie` é o pacote ODM; `Document` é a classe base que liga esta classe a uma coleção MongoDB;
#   `Indexed` declara índice (e opções como unique) no campo correspondente.
from beanie import Document, Indexed

# `from uuid import UUID, uuid4`:
# - `uuid` é o módulo padrão Python para identificadores únicos universais;
# - `UUID` é o tipo; `uuid4()` gera um UUID aleatório (usado como factory do campo user_id).
from uuid import UUID, uuid4

# `from pydantic import EmailStr, Field`:
# - `pydantic` valida dados; `EmailStr` valida formato de e-mail (exige email-validator instalado);
# - `Field` configura metadados do campo (default_factory, unique, etc.) no modelo.
from pydantic import EmailStr, Field

# `from typing import Optional`:
# - `typing` define tipos genéricos; `Optional[str]` significa `str | None` (campo pode ser string ou None).
from typing import Optional
from datetime import datetime


# Herda `Document`: cada instância é um documento na coleção; nome da coleção deriva do nome da classe (ex.: User).
class User(Document):
    # UUID único da aplicação; `default_factory=uuid4` chama uuid4() ao criar documento novo; `unique=True` no Field (Pydantic/Beanie).
    user_id: UUID = Field(default_factory=uuid4, unique=True)
    # `Indexed(str, unique=True)`: cria índice único no MongoDB para login/busca por username.
    username: Indexed(str, unique=True)
    # Índice único no e-mail; tipo EmailStr valida formato antes de persistir.
    email: Indexed(EmailStr, unique=True)
    # Senha já com hash (nunca armazenar senha em texto puro).
    hash_password: str
    # Opcional: pode ser None se não informado.
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    # Opcional com default False: usuário ativo por padrão.
    disabled: Optional[bool] = False

    
    # Representação para debug (ex.: em logs, REPL).
    def __repr__(self) -> str:
        return f"<User {self.email}>"

    # Representação “humana” ao converter User para str().
    def __str__(self) -> str:
        return self.email

    # Permite usar User em conjuntos (set) e como chave em dict se combinar com __eq__ consistente.
    def __hash__(self) -> int:
        return hash(self.email)

    # Duas instâncias User são iguais se o e-mail for o mesmo (identidade de negócio por e-mail).
    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email

    @property
    def create(self) -> datetime:
        return self.id.generation_time

    #`cls` = a classe em `@classmethod` (≈ `static`).
    @classmethod
    async def  find_by_email(cls, email: EmailStr) -> Optional["User"]:
        return await cls.find_one(cls.email == email)

    # self vs cls (lembrete): `self` = instância (≈ `this` no TS). `cls` = a classe em `@classmethod` (≈ `static`).
    @classmethod
    async def by_email(self, email: str) -> "User":
        return await self.find_one(self.email == email)

    # @classmethod
    # async def by_username(self, username: str) -> "User":
        # return await self.find_one(cls.username == username)

    # @classmethod
    # async def by_user_id(self, user_id: UUID) -> "User":
        # return await self.find_one(cls.user_id == user_id)