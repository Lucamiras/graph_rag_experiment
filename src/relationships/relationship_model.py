from pydantic import BaseModel, Field
from typing import List


class Entity(BaseModel):
    name: str = Field(description="Name of the entity (Person, Organization)")

class Relationship(BaseModel):
    source: Entity
    description: str = Field(description="Short, broad description of the relationship, such as 'Married to' or 'Seeks'")
    target: Entity

class RelationshipModel(BaseModel):
    entities: List[Entity]
    relationships: List[Relationship]
