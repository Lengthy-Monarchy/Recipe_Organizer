#!usr/bin/env python3

from modules import Base
from modules import engine, Category, Recipe, Ingredient, Instruction, Base, session

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# Base.metadata.create_all(engine)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

def seed_database():
    # Seed categories
    categories = ["Breakfast", "Lunch", "Dinner", "Dessert", "Snack"]
    for category_name in categories:
        category = Category(name=category_name)
        session.add(category)
    session.commit()


    # Seed recipes
    recipes_data = {
        "Blueberry Muffins": { 
        "category": "Breakfast",
        "total_cooktime": 30.0,  # Cook time in minutes
        "instructions": [
            "Preheat oven to 375 degrees F (190 degrees C). Grease muffin cups or line with muffin liners.",
            "Combine flour, baking powder, and salt in a bowl.",
            "Beat together butter, sugar, and egg until smooth. Mix in milk and vanilla extract until well combined.",
            "Stir in flour mixture until just combined. Fold in blueberries.",
            "Scoop batter into prepared muffin cups.",
            "Bake in preheated oven until a toothpick inserted into the center comes out clean, about 20 minutes."
        ],
        "ingredients": ["All-purpose flour", "Baking powder", "Salt", "Butter", "Granulated sugar", "Egg", "Milk", "Vanilla extract", "Blueberries"]
    },
    "Grilled Cheese Sandwich": {
        "category": "Lunch",
        "total_cooktime": 15.0,  # Cook time in minutes
        "instructions": [
            "Preheat skillet over medium heat.",
            "Generously butter one side of a slice of bread.",
            "Place bread butter-side-down onto skillet bottom and add 1 slice of cheese.",
            "Butter a second slice of bread on one side and place butter-side-up on top of sandwich.",
            "Grill until lightly browned and flip over; continue grilling until cheese is melted.",
            "Repeat with remaining 2 slices of bread, butter, and slice of cheese."
        ],
        "ingredients": ["Bread slices", "Butter", "Cheese slices"]
    },
    "Chocolate Cake": {
        "category": "Dessert",
        "total_cooktime": 45.0,  # Cook time in minutes
        "instructions": [
            "Preheat oven to 350 degrees F (175 degrees C). Grease and flour two 9-inch round pans.",
            "In a large bowl, combine flour, sugar, cocoa, baking powder, baking soda, and salt.",
            "Add eggs, milk, oil, and vanilla; beat on medium speed for 2 minutes.",
            "Stir in boiling water (batter will be thin). Pour batter into prepared pans.",
            "Bake 30 to 35 minutes, or until a toothpick inserted into the center comes out clean.",
            "Cool in pans for 10 minutes, then remove from pans and cool completely on wire racks."
        ],
        "ingredients": ["All-purpose flour", "White sugar", "Cocoa powder", "Baking powder", "Baking soda", "Salt", "Eggs", "Milk", "Vegetable oil", "Vanilla extract", "Boiling water"]
    },
    "Apple Pie": {
        "category": "Dessert",
        "total_cooktime": 60.0,  # Cook time in minutes
        "instructions": [
            "Preheat oven to 425 degrees F (220 degrees C).",
            "Mix sugar, flour, and cinnamon together in a bowl.",
            "Place bottom crust in pie plate; pour apple slices into crust. Sprinkle sugar mixture over apples.",
            "Cover apples with top crust, cutting slits in the crust for ventilation.",
            "Bake in the preheated oven for 15 minutes. Reduce heat to 350 degrees F (175 degrees C) and bake until crust is golden brown, about 35 minutes more."
        ],
        "ingredients": ["Pastry for double-crust pie", "White sugar", "All-purpose flour", "Ground cinnamon", "Apples"]
    },
    "Popcorn": {
        "category": "Snack",
        "total_cooktime": 10.0,  # Cook time in minutes
        "instructions": [
            "Heat oil in a large saucepan over medium heat.",
            "Add popcorn kernels to the heated oil and cover the saucepan with a lid.",
            "Shake the saucepan gently to coat kernels with oil.",
            "Continue cooking, shaking the saucepan frequently, until popping ceases, about 5 minutes.",
            "Remove from heat and transfer popcorn to a large serving bowl.",
            "Season with salt or desired toppings, and toss to coat evenly."
        ],
        "ingredients": ["Popcorn kernels", "Oil", "Salt"]
    },
    "Chocolate Cake": {
        "category": "Dessert",
        "total_cooktime": 60.0,  # Cook time in minutes
        "instructions": [
            "Preheat oven to 350 degrees F (175 degrees C). Grease and flour two 9-inch round pans.",
            "In a large bowl, beat butter, sugar, eggs, and vanilla until light and fluffy.",
            "Combine flour, cocoa, baking soda, and salt; gradually add to the butter mixture alternately with milk, beating well after each addition.",
            "Divide batter evenly between prepared pans. Bake in preheated oven for 30 to 35 minutes, or until a toothpick inserted into the center comes out clean. Allow to cool in pans on wire racks for 10 minutes. Then invert onto wire racks to cool completely."
        ],
        "ingredients": ["Butter", "Sugar", "Eggs", "Vanilla extract", "All-purpose flour", "Cocoa powder", "Baking soda", "Salt", "Milk"]
    },
    "Caesar Salad": {
        "category": "Lunch",
        "total_cooktime": 15.0,  # Cook time in minutes
        "instructions": [
            "In a large salad bowl, rub the inside of the bowl with the cut garlic clove, and discard clove.",
            "Add the lettuce to the bowl. Sprinkle with cheese and croutons. Drizzle with the oil, lemon juice, Worcestershire sauce, and vinegar. Toss well, and season to taste with salt and pepper.",
            "Add the lettuce to the bowl. Sprinkle with cheese and croutons. Drizzle with the oil, lemon juice, Worcestershire sauce, and vinegar. Toss well, and season to taste with salt and pepper."
        ],
        "ingredients": ["Romaine lettuce", "Garlic", "Parmesan cheese", "Croutons", "Olive oil", "Lemon juice", "Worcestershire sauce", "Vinegar", "Salt", "Pepper"]
    },
    "Grilled Cheese Sandwich": {
        "category": "Snack",
        "total_cooktime": 10.0,  # Cook time in minutes
        "instructions": [
            "Preheat skillet over medium heat.",
            "Spread butter onto one side of each slice of bread. Place 4 slices of bread butter-side down onto the skillet.",
            "Place a slice of cheese onto each piece of bread.",
            "Top with the remaining bread slices, butter-side up.",
            "Cook until golden brown on each side, about 3 to 4 minutes per side."
        ],
        "ingredients": ["Bread slices", "Butter", "Cheddar cheese slices"]
    },
    "Chicken Alfredo": {
        "category": "Dinner",
        "total_cooktime": 30.0,  # Cook time in minutes
        "instructions": [
            "Cook fettuccine according to package directions.",
            "Meanwhile, in a large skillet, saute chicken and garlic powder in butter until chicken is no longer pink.",
            "Remove and keep warm.",
            "In the same skillet, saute mushrooms until tender.",
            "Add the cream, cheese, salt and pepper; cook and stir over low heat until cheese is melted.",
            "Return chicken to the skillet.",
            "Drain fettuccine; toss with chicken mixture."
        ],
        "ingredients": ["Fettuccine pasta", "Chicken breasts", "Garlic powder", "Butter", "Mushrooms", "Heavy cream", "Parmesan cheese", "Salt", "Pepper"]
    },
    "Blueberry Pancakes": {
        "category": "Breakfast",
        "total_cooktime": 25.0,  # Cook time in minutes
        "instructions": [
            "In a large bowl, sift together flour, sugar, baking powder, and salt.",
            "In another bowl, beat together egg, milk, and melted butter.",
            "Combine wet and dry ingredients and stir in blueberries.",
            "Heat a lightly oiled griddle or frying pan over medium-high heat.",
            "Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake.",
            "Brown on both sides and serve hot."
        ],
        "ingredients": ["All-purpose flour", "Sugar", "Baking powder", "Salt", "Egg", "Milk", "Butter", "Blueberries"]
    },
    "Chicken Caesar Wrap": {
        "category": "Lunch",
        "total_cooktime": 20.0,  # Cook time in minutes
        "instructions": [
            "In a large bowl, toss together romaine lettuce, grilled chicken strips, Parmesan cheese, and Caesar dressing.",
            "Warm tortillas in a dry skillet over medium heat until pliable.",
            "Place lettuce mixture in the center of each tortilla.",
            "Fold in the sides, and then roll up tightly like a burrito."
        ],
        "ingredients": ["Romaine lettuce", "Grilled chicken strips", "Parmesan cheese", "Caesar dressing", "Flour tortillas"]
    },
    "Chocolate Chip Cookies": {
        "category": "Dessert",
        "total_cooktime": 25.0,  # Cook time in minutes
        "instructions": [
            "Preheat oven to 350 degrees F (175 degrees C).",
            "Cream together butter, white sugar, and brown sugar until smooth.",
            "Beat in the eggs one at a time, then stir in the vanilla.",
            "Combine flour, baking soda, and salt; stir into the creamed mixture.",
            "Fold in chocolate chips.",
            "Drop by large spoonfuls onto ungreased pans.",
            "Bake for about 10 minutes in the preheated oven, or until edges are nicely browned."
        ],
        "ingredients": ["Butter", "White sugar", "Brown sugar", "Eggs", "Vanilla extract", "All-purpose flour", "Baking soda", "Salt", "Semisweet chocolate chips"]
    },
    "Guacamole": {
        "category": "Snack",
        "total_cooktime": 10.0,  # Cook time in minutes
        "instructions": [
            "In a medium bowl, mash together the avocados, lime juice, and salt.",
            "Mix in onion, cilantro, tomatoes, and garlic.",
            "Refrigerate 1 hour for best flavor, or serve immediately."
        ],
        "ingredients": ["Avocados", "Lime juice", "Salt", "Onion", "Cilantro", "Tomatoes", "Garlic"]
    },
    "Steak Tacos": {
        "category": "Dinner",
        "total_cooktime": 25.0,  # Cook time in minutes
        "instructions": [
            "Rub each steak lightly with oil. Season both sides of the steaks with salt and pepper.",
            "Grill steaks for 7-9 minutes on each side, until internal temperature reaches 140°F for medium-rare, or until desired degree of doneness is reached.",
            "Remove steaks from the grill and let them rest for 5 minutes before slicing them thinly against the grain."
        ],
        "ingredients": ["Steak", "Salt", "Pepper", "Oil", "Tortillas", "Salsa", "Lettuce", "Tomato", "Onion", "Sour cream"]
    },
    "Fruit Salad": {
        "category": "Snack",
        "total_cooktime": 10.0,  # Cook time in minutes
        "instructions": [
            "In a large bowl, combine all the fruits.",
            "In a small bowl, whisk together the honey, lime juice, and mint.",
            "Pour the honey-lime dressing over the fruit and toss gently to coat.",
            "Chill for at least 30 minutes before serving."
        ],
        "ingredients": ["Strawberries", "Blueberries", "Pineapple chunks", "Grapes", "Honey", "Lime juice", "Fresh mint leaves"]
    },
    "Margarita Pizza": {
        "category": "Dinner",
        "total_cooktime": 20.0,  # Cook time in minutes
        "instructions": [
            "Preheat oven to 475°F (245°C).",
            "Roll out the pizza dough on a floured surface to your desired thickness.",
            "Place the dough on a pizza pan or baking sheet.",
            "Spread pizza sauce evenly over the dough, leaving a small border around the edges.",
            "Sprinkle shredded mozzarella cheese over the sauce.",
            "Arrange tomato slices and fresh basil leaves on top of the cheese.",
            "Bake in preheated oven for 10-12 minutes, or until crust is golden and cheese is bubbly and lightly browned."
        ],
        "ingredients": ["Pizza dough", "Pizza sauce", "Mozzarella cheese", "Tomato slices", "Fresh basil leaves"]
    },
    "Omelette": {
        "category": "Breakfast",
        "total_cooktime": 15.0,  # Cook time in minutes
        "instructions": [
            "In a small bowl, beat eggs with salt and pepper.",
            "Heat butter in a pan over medium heat until melted and hot.",
            "Pour in the beaten eggs and cook until partially set, about 2 minutes.",
            "Sprinkle cheese, ham, and vegetables evenly over the eggs.",
            "Fold omelette in half and cook for an additional 2-3 minutes, or until cheese is melted and eggs are cooked through."
        ],
        "ingredients": ["Eggs", "Salt", "Pepper", "Butter", "Shredded cheese", "Ham", "Vegetables (e.g., bell peppers, onions, mushrooms)"]
    },

    "Pancakes": {
        "category": "Breakfast",
        "instructions": [
            "Mix flour, eggs, milk, sugar, baking powder, and salt in a bowl.",
            "Heat a lightly oiled griddle or frying pan over medium-high heat.",
            "Pour or scoop the batter onto the griddle, using approximately 1/4 cup for each pancake.",
            "Brown on both sides and serve hot."
        ],
        "ingredients": ["Flour", "Eggs", "Milk", "Butter", "Sugar", "Baking powder", "Salt"]
    },
    "Spaghetti": {
        "category": "Dinner",
        "instructions": [
            "Bring a large pot of lightly salted water to a boil.",
            "Cook spaghetti in the boiling water, stirring occasionally until cooked through but firm to the bite, about 12 minutes; drain.",
            "Heat olive oil in a large skillet over medium heat; cook and stir garlic until lightly browned, about 1 minute.",
            "Add ground beef, onion, salt, and black pepper; cook and stir until browned and crumbly, 5 to 7 minutes.",
            "Pour diced tomatoes and tomato sauce into the skillet; season with sugar, Italian seasoning, basil, salt, and pepper.",
            "Simmer sauce for 10 minutes; add spaghetti and cook, stirring occasionally, until heated through and flavors are blended, about 10 minutes more."
        ],
        "ingredients": ["Spaghetti pasta", "Tomato sauce", "Ground beef", "Onion", "Garlic", "Olive oil", "Salt", "Pepper"]
    }
}

    for recipe_name, recipe_data in recipes_data.items():
        category = session.query(Category).filter_by(name=recipe_data["category"]).first()
        if category:
            recipe = Recipe(name=recipe_name, category=category)
            session.add(recipe)
            session.commit()

            # Seed instructions
            instructions = recipe_data["instructions"]
            for idx, instruction_desc in enumerate(instructions, start=1):
                instruction = Instruction(step=idx, description=instruction_desc, recipe=recipe)
                session.add(instruction)
            session.commit()

            # Seed ingredients
            ingredients = recipe_data["ingredients"]
            for ingredient_name in ingredients:
                ingredient = Ingredient(name=ingredient_name, recipe=recipe)
                session.add(ingredient)
            session.commit()

# if __name__ == "__main__":
seed_database()
print("Seeded database succesfully")
