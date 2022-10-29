import pathlib
from typing import Union, List, Optional
from pydantic import BaseModel, Field, HttpUrl

from .circuit import LearnCircuit


class GateLearnData(BaseModel):
    learn_circuit: LearnCircuit = Field(..., description="The LearnCircuit for this page")
    bloch_sphere: pathlib.Path = Field(..., description="The url to the file which contains the bloch sphere image")
    gate: str = Field(None, description="The featured gate for this page")


class CaptionedBlochSphere(BaseModel):
    bloch_sphere: pathlib.Path = Field(..., description="The bloch sphere image")
    caption: str = Field(..., description="The caption for the bloch sphere")


class LearnData(BaseModel):
    learn_id: str = Field(..., description="The id for this learn page")
    progression: float = Field(..., description="The progression of this page so far")
    title: str = Field(..., description="The title for this learning page")
    text: Union[List[str], str] = Field(..., description="The text to learn for this page")
    question: Union[List[str], str] = Field(..., description="The prompt to learn for this page")
    response: Union[List[str], str] = Field(..., description="The text for the AI for this page")
    instruction: str = Field(None, description="The text to use as an instruction for the page")
    media: Union[GateLearnData, List[CaptionedBlochSphere]] = Field(None, description="Media to display, if any")
    next: HttpUrl = Field(None, description="The next page")
    next_page: str = Field(None, description="href for next page")
    prev_page: str = Field(None, description="href for prev page")
    next_name: str = Field("", description="The name of the next page")
    prev_name: str = Field("", description="The name of the previous page")
    prev: HttpUrl = Field(None, description="The previous page")
