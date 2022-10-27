
import pathlib

from pydantic import BaseModel, Field

class QuizLanding(BaseModel):
    title: str = Field("Quiz", description="The title for the quiz landing page")
    description: str = Field("Ready to be tested on what you’ve learned?", description="The description for the quiz landing page")
    bloch_sphere: pathlib.Path = Field(..., description="Path to the bloch sphere for the quiz landing page")
    next_name: str = Field("Start", description="The next indicator.")
    next_page: str = Field("/quiz/1", description="href for next page")
    prev_page: str = Field("/", description="href for home page")
    prev_name: str = Field("Go Home", description="Text for home button")