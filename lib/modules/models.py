from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from modules import Base

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    instructions = relationship("Instruction", back_populates="recipe")
    ingredients = relationship("Ingredient", back_populates="recipe")
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="recipes")
    total_cooktime = Column(Float)

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship("Recipe", back_populates="ingredients")

class Instruction(Base):
    __tablename__ = 'instructions'
    id = Column(Integer, primary_key=True)
    step = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    recipe = relationship("Recipe", back_populates="instructions")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    recipes = relationship("Recipe", back_populates="category")
