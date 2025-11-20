from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

from .profanity import Profanity

app = FastAPI()
profanity = Profanity()


class CheckRequest(BaseModel):
    """
    The request object for the `/check` endpoint.
    """

    message: str = Field(
        description="The message to be checked for profanity.",
        min_length=1,
        max_length=280,
    )


class CensorRequest(BaseModel):
    """
    The request object for the `/censor` endpoint.
    """

    message: str = Field(
        description="The message to be censored of profanity.",
        min_length=1,
        max_length=280,
    )


@app.post("/check")
async def check(request: Annotated[CheckRequest, Body(embed=False)]) -> bool:
    """
    Returns a boolean representing whether or not the provided message string contains profanity.
    """
    body = request.model_dump()
    return profanity.is_profane(body["message"])


@app.post("/censor")
async def censor(request: Annotated[CensorRequest, Body(embed=False)]) -> str:
    """
    Returns the provided message string, censoring any text deemed as profane.
    """
    body = request.model_dump()
    return profanity.censor(body["message"])


@app.head("/health")
async def health():
    pass
