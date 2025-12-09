from pydantic import BaseModel

class ClientData(BaseModel):
    full_name: str
    id: int