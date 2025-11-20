from typing import Annotated

from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .sailor import Sailor

app = FastAPI()
sailor = Sailor()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    return sailor.is_profane(body["message"])


@app.post("/censor")
async def censor(request: Annotated[CensorRequest, Body(embed=False)]) -> str:
    """
    Returns the provided message string, censoring any text deemed as profane.
    """
    body = request.model_dump()
    return sailor.censor(body["message"])


@app.head("/health")
async def health():
    pass
