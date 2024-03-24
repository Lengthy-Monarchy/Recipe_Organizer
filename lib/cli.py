import click
from sqlalchemy import or_
from modules import Category, Recipe, Ingredient, Instruction, session
import sys

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

def add_recipe():
    """Add a new recipe to the collection."""
    click.echo("Adding a new recipe...")
    name = click.prompt("Enter the recipe name", type=str)
    total_cooktime = click.prompt("Enter the total cook time (in minutes)", type=float)  # Prompt for cook time
    
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
    recipe = Recipe(name=name, category=category_obj, total_cooktime=total_cooktime)  # Include cook time
    session.add(recipe)
    session.commit()

    # Adding instructions
    click.echo(f"Adding instructions for '{name}':")
    instructions = click.prompt("Enter instructions separated by commas").split(',')
    for idx, instruction_text in enumerate(instructions, start=1):
        instruction = Instruction(step=idx, description=instruction_text.strip(), recipe=recipe)
        session.add(instruction)
    session.commit()
    click.echo("Instructions saved successfully!")

    # Adding ingredients
    click.echo(f"Adding ingredients for '{name}':")
    ingredients = click.prompt("Enter ingredients separated by commas").split(',')
    for ingredient_text in ingredients:
        ingredient_name = ingredient_text.strip()
        ingredient = Ingredient(name=ingredient_name, recipe=recipe)
        session.add(ingredient)
    session.commit()
    click.echo("Ingredients saved successfully!")

    click.echo(f"Recipe '{name}' added successfully!")

def search_by_ingredient():
    """Search for recipes by ingredient."""
    query = click.prompt("Enter ingredients separated by commas", type=str)
    search_terms = query.split(',')
    ingredient_filters = [Ingredient.name.ilike(f'%{term.strip()}%') for term in search_terms]
    combined_ingredient_filter = or_(*ingredient_filters)
    recipes = session.query(Recipe).filter(Recipe.ingredients.any(combined_ingredient_filter)).all()
    display_search_results(recipes)

def search_by_name():
    """Search for recipes by recipe name."""
    query = click.prompt("Enter the recipe name", type=str)
    recipes = session.query(Recipe).filter(Recipe.name.ilike(f'%{query}%')).all()
    display_search_results(recipes)

def search_by_category():
    """Search for recipes by category."""
    click.echo("Select a category:")
    existing_categories = ['Dinner', 'Snack', 'Lunch', 'Breakfast', 'Dessert']
    for idx, category in enumerate(existing_categories, start=1):
        click.echo(f"{idx}. {category}")
    category_choice = click.prompt("Enter the category number", type=int)
    category_name = existing_categories[category_choice - 1]
    
    # Query recipes belonging to the selected category
    recipes = session.query(Recipe).filter(Recipe.category.has(Category.name == category_name)).all()
    
    # Display search results
    display_search_results(recipes)

def display_search_results(recipes):
    """Display search results."""
    if recipes:
        click.echo("Matching Recipes:")
        for idx, recipe in enumerate(recipes, start=1):
            click.echo(f"{idx}. {recipe.name}")

        selection = click.prompt("Enter the number of the recipe to view details (0 to return to home)", type=int)
        if selection == 0:
            return  # Return to home

        selected_recipe = recipes[selection - 1]
        click.echo(f"\nRecipe Details for '{selected_recipe.name}':")
        click.echo(f"Category: {selected_recipe.category.name}")
        click.echo(f"Total Cook Time: {selected_recipe.total_cooktime} minutes")

        click.echo("\nIngredients:")
        for ingredient in selected_recipe.ingredients:
            click.echo(f"- {ingredient.name}")

        click.echo("\nInstructions:")
        for instruction in selected_recipe.instructions:
            click.echo(f"{instruction.step}. {instruction.description}")

        click.echo("\nOptions:")
        click.echo("1. Edit Recipe")
        click.echo("2. Delete Recipe")
        option = click.prompt("Select an option (0 to return to home)", type=int)

        if option == 1:
            # Add logic to edit the recipe
            pass
        elif option == 2:
            confirm = click.confirm("Are you sure you want to delete this recipe?")
            if confirm:
                session.delete(selected_recipe)
                session.commit()
                click.echo("Recipe deleted successfully!")
    else:
        click.echo("No matching recipes found.")

def search():
    """Search for recipes by recipe name, ingredient, or category."""
    while True:
        click.echo("Search For Recipes")
        click.echo("1. Search by ingredient")
        click.echo("2. Search by Name")
        click.echo("3. Search By categories")
        click.echo("0. Back")  # Add a back option
        selection = click.prompt("Enter your selection", type=int)

        if selection == 1:
            search_by_ingredient()
        elif selection == 2:
            search_by_name()
        elif selection == 3:
            search_by_category()
        elif selection == 0:
            return  # Return to home
        else:
            click.echo("Invalid selection. Please enter a valid option.")

def menu():
    click.echo("Welcome to Recipe Organizer CLI Application!")
    click.echo("1. Add new recipe")
    click.echo("2. Search Recipes")
    click.echo("3. Exit")

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
        elif selection == 0:
            continue
        else:
            click.echo("Invalid selection. Please enter a valid option.")

# Run the CLI
if __name__ == "__main__":
    main()
