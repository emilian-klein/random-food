from dataclasses import dataclass


@dataclass
class Recipe:
    title: str
    image: str
    description: str
    instructions: list
    ingredients: list
