
from pydantic import BaseModel, Field

class QuizResultData(BaseModel):
    
    correct: int = Field(0, description="The number of correct answers")
    total_questions: int = Field(5, description="The number of questions")
    prev_page: str = Field("/quiz", description="Try again with the quiz")
    prev_name: str = Field("Try Again", description="What to say when trying again")
    next_page: str = Field("/", description="Where to go next")
    next_name: str = Field("Home", description="What is next")
    results: list = Field([0 for _ in range(5)], description="array for correct answers. 0 is incorrect, 1 is correct.")

