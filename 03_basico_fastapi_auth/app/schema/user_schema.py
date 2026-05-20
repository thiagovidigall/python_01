from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="User email")
    username: str = Field(..., description="User username")
    password: str = Field(..., description="User password")

class UserResponse(BaseModel):
    user_id: UUID = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User email")
    first_name: Optional[str] = Field(None, description="User first name")
    last_name: Optional[str] = Field(None, description="User last name")
    disabled: bool = Field(False, description="User disabled")
    create: datetime = Field(..., description="User creation date")