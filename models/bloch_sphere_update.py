
import pathlib

from pydantic import BaseModel, Field


class BlochSphereUpdate(BaseModel):
    bloch_sphere: pathlib.Path = Field(None, description="The url to the file which contains the bloch sphere image")

