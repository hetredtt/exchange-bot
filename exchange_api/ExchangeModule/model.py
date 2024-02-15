from pydantic import BaseModel

class CodeList(BaseModel):
    codes: list[dict]