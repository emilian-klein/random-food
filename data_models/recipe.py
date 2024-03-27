from dataclasses import dataclass


@dataclass
class Recipe:
    title: str
    description: str
    instructions: list
    ingredients: list
