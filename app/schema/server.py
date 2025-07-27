from pydantic import BaseModel


class Receive(BaseModel):
    fen: str
    player: str
    opponent: str


class Send(BaseModel):
    fen: str
    resp: list
    isvalid: bool
    iserr: bool
    err: str