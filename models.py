from typing import Optional
from datetime import datetime
from enum import Enum
from sqlmodel import Field, SQLModel

class UserRole(str, Enum):
    BANK = "bank"
    CORPORATE = "corporate"
    AUDITOR = "auditor"
    ADMIN = "admin"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    password: str
    role: UserRole
    org_name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)