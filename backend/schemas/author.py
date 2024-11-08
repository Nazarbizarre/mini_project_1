from typing import Optional

from bcrypt import (hashpw,
                    gensalt)
from pydantic import (BaseModel,
                      EmailStr,
                      Field,
                      field_validator)
from ..utils.hash_pwd import get_password_hash
from ..loggers.loggers import validations_logger


class AuthorData(BaseModel):
    name: str = Field(..., description="The name of the author")
    email: EmailStr = Field(..., description="The author's email adress")
    bio: Optional[str] = Field(..., description="A short biography of the author")
    password: str = Field(
        ...,
        min_length=8,
        description="Password for author login, 8 characters at least",
    )

    @field_validator("password")
    def hash_password(cls, value):
        validations_logger.info("Model: AuthorData, Field: password, Result: Hash Created")
        return get_password_hash(value)
