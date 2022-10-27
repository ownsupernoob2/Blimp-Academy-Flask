from typing import List, Union
import pathlib

from pydantic import BaseModel, Field

from .circuit import Circuit


class MultipleChoices(BaseModel):
    choices: List[str] = Field(["A", "B", "C", "D"], description="A B C D")
    correct: str = Field(..., description="The correct choice")
    answers_media: Union[List[str], List[pathlib.Path], List[Circuit]] = Field([], description="string, image, or circuit to display for each choice.")
    answers_type: str = Field(..., description="Type of answer. Must be 'str', 'path', or 'circuit'")


class CircuitDraw(BaseModel):
    start: Circuit = Field(Circuit(), description="The starting state for the circuit")
    correct: Circuit = Field(..., description="The correct circuit")


class QuizQuestion(BaseModel):
    question_id: str = Field(..., description="The question number, it is a unique identifier")
    progression: float = Field(..., description="The progression of this question into the quiz")
    name: str = Field(..., description="The question name. This gets displayed as the question")
    name_media: Union[pathlib.Path, Circuit] = Field(None, description="The question media, if any")
    media_type: str = Field(None, description="Media type for question. Must be 'path', or 'circuit'")
    is_multiple_choice: bool = Field(False, description="True if this a multiple choice question")
    is_circuit_draw: bool = Field(False, description="True if this a circuit drawing question")
    multiple_choice: MultipleChoices = Field(None, description="If this is a multiple choice question, the options")
    circuit_draw: CircuitDraw = Field(None, description="A circuit draw")
    interactive_sphere: bool = Field(False, description="Include interactive sphere in question.")
    bloch_sphere: pathlib.Path = Field(None, description="The url to the file which contains the bloch sphere image")
    next_name: str = Field("Next", description="The next indicator.")
    next_page: str = Field(None, description="href for next page")
    prev_page: str = Field(None, description="href for prev page")


class MultipleChoiceAnswer(BaseModel):
    answer: str = Field(..., description="The answer a user chose for a question")