"""
This model is to be used to transfer the contents of a circuit
to and from client or backend
"""

from typing import List

from pydantic import BaseModel, Field


class Circuit(BaseModel):

    gates: List[str] = Field([], description="A list of gates on a circuit")


class LearnCircuit(Circuit):
    """ Learn circuits come with a bloch sphere and a gate tray in the ui"""
    learn_circuit_id: str = Field(..., description="The learn id for this circuit")
