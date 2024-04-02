from dataclasses import dataclass, field
from typing import List


@dataclass
class Recipe:
    title: str = ""
    image: str = ""
    description: str = ""
    ingredients: List[str] = field(default_factory=list)
    instructions: List[str] = field(default_factory=list)
