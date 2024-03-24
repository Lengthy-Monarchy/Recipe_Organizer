import click
from modules import Category, Recipe, Ingredient, Instruction,session
import sys
# from model_modules import engine
# from sqlalchemy.orm import sessionmaker

# Create a session factory
# Session = sessionmaker(bind=engine)

# Define get_or_create function
def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance, True

@click.group()
def cli():
    """Welcome to Recipe Organizer CLI Application!"""
    pass

@cli.command()
def add_recipe():
    """Add a new recipe to the collection."""
    click.echo("Adding a new recipe...")
    name = click.prompt("Enter the recipe name", type=str)
    
    # Display pre-existing categories
    click.echo("Select a category:")
    existing_categories = ['Dinner', 'Snack', 'Lunch', 'Breakfast', 'Dessert']
    for idx, category in enumerate(existing_categories, start=1):
        click.echo(f"{idx}. {category}")
    category_choice = click.prompt("Enter the category number", type=int)

    # Get or create category
    category_name = existing_categories[category_choice - 1]
    category_obj, _ = get_or_create(session, Category, name=category_name)

    # Create recipe
    recipe = Recipe(name=name, category=category_obj)
    session.add(recipe)
    session.commit()

    # Adding instructions
    click.echo(f"Adding instructions for '{name}':")
    instructions = []
    while True:
        click.echo("Select an option:")
        click.echo("1. Add Instruction")
        click.echo("2. Save Instructions")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            instruction_text = click.prompt("Enter instruction")
            instructions.append(instruction_text)
        elif choice == 2:
            for idx, instruction_text in enumerate(instructions, start=1):
                instruction = Instruction(step=idx, description=instruction_text, recipe=recipe)
                session.add(instruction)
            session.commit()
            click.echo("Instructions saved successfully!")
            break
        else:
            click.echo("Invalid choice. Please enter a valid option.")

    # Adding ingredients
    click.echo(f"Adding ingredients for '{name}':")
    ingredients = []
    while True:
        click.echo("Select an option:")
        click.echo("1. Add Ingredient")
        click.echo("2. Save Ingredients")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            ingredient_name = click.prompt("Enter ingredient name")
            ingredients.append(ingredient_name)
        elif choice == 2:
            for ingredient_name in ingredients:
                ingredient = Ingredient(name=ingredient_name, recipe=recipe)
                session.add(ingredient)
            session.commit()
            click.echo("Ingredients saved successfully!")
            break
        else:
            click.echo("Invalid choice. Please enter a valid option.")

    click.echo(f"Recipe '{name}' added successfully!")

@cli.command()
def search():
    """Search for recipes by ingredients or categories."""
    query = click.prompt("Enter your search query", type=str)
    # Search for recipes by name, ingredients, or category
    recipes = (
        session.query(Recipe)
        .filter(Recipe.name.like(f'%{query}%') |
                Recipe.category.has(Category.name.like(f'%{query}%')) |
                Recipe.ingredients.any(Ingredient.name.like(f'%{query}%')))
        .all()
    )

    if recipes:
        click.echo("Matching Recipes:")
        for recipe in recipes:
            click.echo(f"- {recipe.name} ({recipe.category.name})")
    else:
        click.echo("No matching recipes found.")


def main():
    while True:
        menu()
        selection = click.prompt("Enter your selection", type=int)    
        if selection == 1:
            add_recipe()
        elif selection == 2:
            search()
        elif selection == 3:            
            click.echo("Exiting...")
            sys.exit()
        else:
            click.echo("Invalid selection. Please enter a valid option.")
def menu():
    click.clear()
    click.echo("1. Add new recipe")
    click.echo("2. Search Recipes")
    click.echo("3. Exit")

# Run the CLI
if __name__ == "__main__":
    main()
