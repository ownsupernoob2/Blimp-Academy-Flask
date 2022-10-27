import pathlib
from typing import Union, List, Optional
from pydantic import BaseModel, Field, HttpUrl

from .circuit import LearnCircuit
from .learn_data import GateLearnData, CaptionedBlochSphere


class HomeData(BaseModel):
    title: str = Field(..., description="The title for this learning page")
    text: Union[List[str], str] = Field(..., description="The text to learn for this page")
    media: Union[GateLearnData, List[CaptionedBlochSphere]] = Field(None, description="Media to display, if any")
    complete_sections: int = Field(0, description="The number of completed sections")
