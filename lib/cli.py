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
    """\033[1;35;40mWelcome to Recipe Organizer CLI Application!\033[0;37;40m"""
    pass

def add_recipe():
    """Add a new recipe to the collection."""
    click.echo("\033[1;32;40mAdding a new recipe...\033[0;37;40m")
    name = click.prompt("\033[1;33;40mEnter the recipe name:\033[0;37;40m", type=str)
    total_cooktime = click.prompt("\033[1;33;40mEnter the total cook time (in minutes):\033[0;37;40m", type=float)
    
    # Display pre-existing categories
    click.echo("\033[1;34;40mSelect a category:\033[0;37;40m")
    existing_categories = ['Dinner', 'Snack', 'Lunch', 'Breakfast', 'Dessert']
    for idx, category in enumerate(existing_categories, start=1):
        click.echo(f"\033[1;36;40m{idx}. {category}\033[0;37;40m")
    category_choice = click.prompt("\033[1;33;40mEnter the category number:\033[0;37;40m", type=int)

    # Get or create category
    category_name = existing_categories[category_choice - 1]
    category_obj, _ = get_or_create(session, Category, name=category_name)

    # Create recipe
    recipe = Recipe(name=name, category=category_obj, total_cooktime=total_cooktime)
    session.add(recipe)
    session.commit()

    # Adding instructions
    click.echo("\033[1;34;40mAdding instructions:\033[0;37;40m")
    instructions = click.prompt("\033[1;33;40mEnter instructions separated by commas:\033[0;37;40m").split(',')
    for idx, instruction_text in enumerate(instructions, start=1):
        instruction = Instruction(step=idx, description=instruction_text.strip(), recipe=recipe)
        session.add(instruction)
    session.commit()
    click.echo("\033[1;32;40mInstructions saved successfully!\033[0;37;40m")

    # Adding ingredients
    click.echo("\033[1;34;40mAdding ingredients:\033[0;37;40m")
    ingredients = click.prompt("\033[1;33;40mEnter ingredients separated by commas:\033[0;37;40m").split(',')
    for ingredient_text in ingredients:
        ingredient_name = ingredient_text.strip()
        ingredient = Ingredient(name=ingredient_name, recipe=recipe)
        session.add(ingredient)
    session.commit()
    click.echo("\033[1;32;40mIngredients saved successfully!\033[0;37;40m")

    click.echo(f"\033[1;32;40mRecipe '{name}' added successfully!\033[0;37;40m")

def search_by_ingredient():
    """Search for recipes by ingredient."""
    query = click.prompt("\033[1;33;40mEnter ingredients separated by commas:\033[0;37;40m", type=str)
    search_terms = query.split(',')
    ingredient_filters = [Ingredient.name.ilike(f'%{term.strip()}%') for term in search_terms]
    combined_ingredient_filter = or_(*ingredient_filters)
    recipes = session.query(Recipe).filter(Recipe.ingredients.any(combined_ingredient_filter)).all()
    display_search_results(recipes)

def search_by_name():
    """Search for recipes by recipe name."""
    query = click.prompt("\033[1;33;40mEnter the recipe name:\033[0;37;40m", type=str)
    recipes = session.query(Recipe).filter(Recipe.name.ilike(f'%{query}%')).all()
    display_search_results(recipes)

def search_by_category():
    """Search for recipes by category."""
    click.echo("\033[1;34;40mSelect a category:\033[0;37;40m")
    existing_categories = ['Dinner', 'Snack', 'Lunch', 'Breakfast', 'Dessert']
    for idx, category in enumerate(existing_categories, start=1):
        click.echo(f"\033[1;36;40m{idx}. {category}\033[0;37;40m")
    category_choice = click.prompt("\033[1;33;40mEnter thecategory number:\033[0;37;40m", type=int)
    category_name = existing_categories[category_choice - 1]
    
    # Query recipes belonging to the selected category
    recipes = session.query(Recipe).filter(Recipe.category.has(Category.name == category_name)).all()
    
    # Display search results
    display_search_results(recipes)

def display_search_results(recipes):
    """Display search results."""
    if recipes:
        click.echo("\033[1;32;40mMatching Recipes:\033[0;37;40m")
        for idx, recipe in enumerate(recipes, start=1):
            click.echo(f"{idx}. {recipe.name}")

        selection = click.prompt("\033[1;33;40mEnter the number of the recipe to view details (0 to return to home):\033[0;37;40m", type=int)
        if selection == 0:
            return  # Return to home

        selected_recipe = recipes[selection - 1]
        click.echo(f"\n\033[1;32;40mRecipe Details for '{selected_recipe.name}':\033[0;37;40m")
        click.echo(f"\033[1;33;40mCategory:\033[0;37;40m {selected_recipe.category.name}")
        click.echo(f"\033[1;33;40mTotal Cook Time:\033[0;37;40m {selected_recipe.total_cooktime} minutes")

        click.echo("\n\033[1;33;40mIngredients:\033[0;37;40m")
        for ingredient in selected_recipe.ingredients:
            click.echo(f"- {ingredient.name}")

        click.echo("\n\033[1;33;40mInstructions:\033[0;37;40m")
        for instruction in selected_recipe.instructions:
            click.echo(f"{instruction.step}. {instruction.description}")

        click.echo("\n\033[1;33;40mOptions:\033[0;37;40m")
        click.echo("1. Delete Recipe")
        option = click.prompt("\033[1;33;40mSelect an option (0 to return to home):\033[0;37;40m", type=int)

        if option == 1:
            confirm = click.confirm("\033[1;33;40mAre you sure you want to delete this recipe?\033[0;37;40m")
            if confirm:
                session.delete(selected_recipe)
                session.commit()
                click.echo("\033[1;32;40mRecipe deleted successfully!\033[0;37;40m")
    else:
        click.echo("\033[1;31;40mNo matching recipes found.\033[0;37;40m")

def search():
    """Search for recipes by recipe name, ingredient, or category."""
    while True:
        click.echo("\033[1;35;40mSearch For Recipes\033[0;37;40m")
        click.echo("1. Search by ingredient")
        click.echo("2. Search by Name")
        click.echo("3. Search By categories")
        click.echo("0. Back")  # Add a back option
        selection = click.prompt("\033[1;33;40mEnter your selection:\033[0;37;40m", type=int)

        if selection == 1:
            search_by_ingredient()
        elif selection == 2:
            search_by_name()
        elif selection == 3:
            search_by_category()
        elif selection == 0:
            return  # Return to home
        else:
            click.echo("\033[1;31;40mInvalid selection. Please enter a valid option.\033[0;37;40m")

def menu():
    click.echo("\033[1;35;40mWelcome to Recipe Organizer CLI Application!\033[0;37;40m")
    click.echo("1. Add new recipe")
    click.echo("2. Search Recipes")
    click.echo("3. Exit")

def main():
    while True:
        menu()
        selection = click.prompt("\033[1;33;40mEnter your selection:\033[0;37;40m", type=int)    
        if selection == 1:
            add_recipe()
        elif selection == 2:
            search()
        elif selection == 3:            
            click.echo("\033[1;33;40mExiting...\033[0;37;40m")
            sys.exit()
        elif selection == 0:
            continue
        else:
            click.echo("\033[1;31;40mInvalid selection. Please enter a valid option.\033[0;37;40m")

# Run the CLI
if __name__ == "__main__":
    main()
