from pydantic import BaseModel


class ResponseDto[T](BaseModel):
    code: int
    message: str
    data: T