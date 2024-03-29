import webapp2
import jinja2
import os
from ee_models import User, FoodItem, Restaurant

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/loginpage.html')
        self.response.write(login_template.render())

restaurant_dict = {
    'Rest1': 'Panera',
    'Rest2': 'McDonalds',
    'Rest3': 'Chipotle',
    'Rest4': 'ChickFilA',
}

class RestaurantHandler(webapp2.RequestHandler):
    def get(self):
        restaurant_list = Restaurant.query().fetch()
        restaurant_template = the_jinja_env.get_template('templates/restaurants.html')
        self.response.write(restaurant_template.render(restaurant_dict))

class RestaurantHomeHandler(webapp2.RequestHandler):
    def get(self):
        RestaurantHome_template = the_jinja_env.get_template('templates/restaurantHome.html')
        restaurant_name = self.request.get("restaurant")
        self.response.write(RestaurantHome_template.render({"restaurant_name":restaurant_name}))

class SeedDataHandler(webapp2.RequestHandler):
    def get(self):
        # FoodItem initialization

        # McDonalds Vegan food items
        mapleOatmeal = FoodItem(name="Fruit and Maple Oatmeal (no cream)", dietaryRest=["Vegan"], picture="https://cbsnews2.cbsistatic.com/hub/i/r/2011/02/23/16c05afd-a644-11e2-a3f0-029118418759/resize/620x465/19626f7f0f253a5a129984333ab5b312/mcdonalds_fruit-and-maple-o.jpg",
                                ingredients="Oatmeal(Water, Whole Grain Rolled Oats, Brown Sugar, Modified Food Starch, Salt, Natural Flavor, Barley Malt Extract, Caramel Color), Diced apples, Cranberry raisin blend(Sweetened Dried Cranberries (Sugar, Cranberries), California Raisins, Golden Raisins, Sunflower Oil, Sulfur Dioxide as a Preservative (Contains Sulfites)",
                                nutrition="290 cal, 61g carbs, 2g fat, 5g protein, 130mg sodium")
        mapleOatmeal_key = mapleOatmeal.put()

        sideSalad = FoodItem(name="Basic Side Salad", dietaryRest=["Vegan"], picture="https://d1gh87f4j52fki.cloudfront.net/m/i/mcdsidesaladphoto.jpg",
                            ingredients="Romaine Lettuce, Baby Spinach, Carrots, Baby Kale, Lollo Rossa Lettuce, Red Leaf Lettuce, Red Oak Lettuce, Red Tango Lettuce, Red Romaine Lettuce, Red Butter Lettuce, Tomato",
                            nutrition="15 cal, 3g carbs, 0g fat, 1g protein, 15mg sodium")

        sideSalad_key = sideSalad.put()

        fruit = FoodItem(name="Fruit(Apple slices)", dietaryRest=["Vegan"], picture="https://spoonuniversity.com/wp-content/uploads/sites/54/2016/06/product_hero_fruit-bag-2016.png",
                        ingredients="Apples, Calcium Ascorbate", nutrition="15 cal, 4g carbs, 0g fat, 0g protein, 0mg sodium")

        fruit_key = fruit.put()

        # McDonalds Vegetarian food items
        fruitParfait = FoodItem(name="Fruit and yogurt parfait", dietaryRest=["Vegetarian"], picture="https://i.pinimg.com/originals/bf/d0/2e/bfd02e90e8077e89b50041d6a34af1f8.png",
                                ingredients="Lowfat Yogurt (Cultured Pasteurized Grade A Reduced Fat Milk, Sugar, Modified Corn Starch, Fructose, Whey Protein Concentrate, Gelatin, Corn Starch, Natural Flavor, Potassium Sorbate), Strawberries, Blueberries, Low Fat Crunchy Granola(Whole Grain Rolled Oats, Brown Sugar, Crisp Rice (Rice Flour, Barley Malt Extract, Salt), Sugar, Corn Syrup, Sunflower Oil, Salt, Baking Soda, Citric Acid, Cinnamon, Crushed Oranges, Natural Flavor)",
                                nutrition="210 cal, 40g carbs, 3g fat, 6g protein, 75mg sodium")

        fruitParfait_key = fruitParfait.put()

        mcmuffin = FoodItem(name="Egg McMuffin (no meat)", dietaryRest=["Vegetarian"], picture="https://a57.foxnews.com/a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2018/09/640/320/1862/1048/5b4abf1c-EggMcMuffin.jpg?ve=1&tl=1?ve=1&tl=1",
                            ingredients="English muffin(Enriched Flour (Wheat Flour, Malted Barley Flour, Niacin, Iron, Thiamine, Riboflavin, Folic Acid), Water, Yeast, Yellow Corn Meal (Degermed Yellow Corn Meal and Corn Flour), Contains 2% or Less: Sugar, Soybean Oil, Salt, Dough Conditioners (Mono-, Di- and Tricalcium Phosphate, DATEM, Ascorbic Acid, Enzymes, Ethylated Mono and Digylcerides), Wheat Gluten, Cultured Wheat Flour, Citric Acid, Baking Soda, Fumaric Acid), Egg, Pasteurized Process American Cheese(Milk, Cream, Water, Sodium Citrate, Salt, Cheese Cultures, Citric Acid, Enzymes, Soy Lecithin, Color Added), Salted butter(cream, salt), Clarified butter(Pasteurized Cream (Butterfat))",
                            nutrition="280 cal, 29g carbs, 12g fat, 14g protein, 550mg sodium")

        mcmuffin_key = mcmuffin.put()

        mcwrap = FoodItem(name="Veggie McWrap", dietaryRest=["Vegetarian"], picture="https://dynamicmedia.zuza.com/zz/m/original_/1/6/169f39a2-0e25-4081-aa82-39f6c7fd3747/B821370149Z.1_20130828072353_000_G9R12AVTN.2_Gallery.jpg",
                        ingredients="Southwest Vegetable Blend(Roasted Corn, Black Beans, Roasted Tomato, Poblano Pepper, Lime Juice (Water, Lime Juice Concentrate, Lime Oil), Cilantro), Flour tortilla(Enriched Flour (Bleached Wheat Flour, Malted Barley Flour, Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Water, Shortening (Intereserified Soybean Oil, Soybean Oil, Hydrogenated Soybean Oil, Hydrogenated Cottonseed Oil), Contains 2% or Less: Sugar, Leavening (Baking Soda, Corn Starch, Sodium Aluminum Sulfate, Calcium Sulfate, Monocalcium Phosphate), Salt, Mono-diglycerides, Vital Wheat Gluten, Dough Conditioner (Sodium Metabisulfite, Corn Starch, Microcrystalline Cellulose, Dicalcium Phosphate)), Salad blend(Romaine Lettuce, Baby Spinach, Carrots, Baby Kale, Lollo Rossa Lettuce, Red Leaf Lettuce, Red Oak Lettuce, Red Tango Lettuce, Red Romaine Lettuce, Red Butter Lettuce), Cilantro Lime Glaze(Water, Corn Syrup Solids, High Fructose Corn Syrup, Sugar, Distilled Vinegar, Olive Oil, Soybean Oil, Freeze-Dried Orange Juice Concentrate, Contains 2% or Less: Salt, Freeze-Dried Lime Juice Concentrate, Cilantro, Xanthan Gum, Preservatives (Sodium Benzoate and Potassium Sorbate), Garlic Powder, Spice, Propylene Glycol Alginate, Onion Powder, Citric Acid), Shredded Cheddar/Jack Cheese(Cheddar Cheese (Pasteurized Milk, Cheese Culture, Salt, Enzymes",
                        nutrition="480 cal, 62g carbs, 19g fat, 15g protein, 870mg sodium")

        mcwrap_key = mcwrap.put()

        # McDonalds Lactose Intolerant
        hamburger = FoodItem(name="Hamburger", dietaryRest=["Lactose Intolerant"], picture="https://www.mcdonalds.com/is/image/content/dam/usa/nfl/nutrition/items/hero/desktop/t-mcdonalds-Hamburger.jpg",
                            ingredients="Regular bun(Enriched Flour (Wheat Flour, Malted Barley Flour, Niacin, Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Water, Sugar, Yeast, Soybean Oil, Contains 2% or Less: Salt, Wheat Gluten, Potato Flour, May Contain One or More Dough Conditioners (DATEM, Ascorbic Acid, Mono and Diglycerides, Enzymes), Vinegar), 100% Beef Patty(100% Pure USDA Inspected Beef; No Fillers, No Extenders. Prepared with Grill Seasoning (Salt, Black Pepper)), Ketchup(Tomato Concentrate from Red Ripe Tomatoes, Distilled Vinegar, High Fructose Corn Syrup, Corn Syrup, Water, Salt, Natural Flavors), Pickle slices(Cucumbers, Water, Distilled Vinegar, Salt, Calcium Chloride, Alum, Potassium Sorbate (Preservative), Natural Flavors, Polysorbate 80, Extractives of Turmeric (Color)), Onions, Mustard(Distilled Vinegar, Water, Mustard Seed, Salt, Turmeric, Paprika, Spice Extractive)",
                            nutrition="250 cal, 31g carbs, 8g fat, 13g protein, 480mg sodium")
        hamburger_key = hamburger.put()

        mcchicken = FoodItem(name="McChicken", dietaryRest=["Lactose Intolerant"], picture="https://www.mcdonalds.com/content/dam/usa/nfl/nutrition/items/regular/desktop/t-mcdonalds-McChicken.jpg",
                            ingredients="McChicken patty(Boneless Chicken, Bleached Wheat Flour, Water, Vegetable Oil (Canola Oil, Corn Oil, Soybean Oil, Hydrogenated Soybean Oil), Wheat Flour, Modified Corn Starch, Sea Salt, Spice, Potassium Chloride, Salt, Paprika, Dextrose, Sodium Phosphates, Leavening (Ammonium Bicarbonate, Sodium Acid Pyrophosphate, Baking Soda, Monocalcium Phosphate), Wheat Gluten, Natural Flavors with Extractives of Paprika, Yeast, Corn Starch, Garlic Powder), Regular Bun(Enriched Flour (Wheat Flour, Malted Barley Flour, Niacin, Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Water, Sugar, Yeast, Soybean Oil, Contains 2% or Less: Salt, Wheat Gluten, Potato Flour, May Contain One or More Dough Conditioners (DATEM, Ascorbic Acid, Mono and Diglycerides, Enzymes), Vinegar), Shredded lettuce, Mayonnaise(Soybean Oil, Egg Yolk, Water, Distilled Vinegar, Salt, Sugar, Spice, Lemon Juice Concentrate)",
                            nutrition="410cal, 39g carbs, 22g fat, 15g protein, 590mg sodium")
        mcchicken_key = mcchicken.put()

        nuggets = FoodItem(name="10 piece Chicken McNuggets", dietaryRest=["Lactose Intolerant"], picture="https://i2.wp.com/www.eatthis.com/wp-content/uploads/2019/02/mcdonalds-chicken-nuggets.jpg?fit=500%2C366&ssl=1",
                            ingredients="White Boneless Chicken, Water, Vegetable Oil (Canola Oil, Corn Oil, Soybean Oil, Hydrogenated Soybean Oil), Enriched Flour (Bleached Wheat Flour, Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Bleached Wheat Flour, Yellow Corn Flour, Vegetable Starch (Modified Corn, Wheat, Rice, Pea, Corn), Salt, Leavening (Baking Soda, Sodium Aluminum Phosphate, Sodium Acid Pyrophosphate, Calcium Lactate, Monocalcium Phosphate), Spices, Yeast Extract, Lemon Juice Solids, Dextrose, Natural Flavors",
                            nutrition="440 cals, 26g carbs, 27g fat, 24g protein, 840mg sodium")

        nuggets_key = nuggets.put()

        # Panera Vegan food items
        oatmeal = FoodItem(name="Steel Cut Oatmeal with Strawberries & Pecans", dietaryRest=["Vegan"], picture="https://www.panerabread.com/content/dam/panerabread/menu/details/steel-cut-oatmeal-strawberries-pecans.jpg",
                            ingredients="Cooked Steel Cut Oats (Water, Cooked Steel Cut Oat Groats [May Contain Traces Of Wheat, Soy And Mustard], Salt), Organic Quinoa (Water, Organic Golden Quinoa, Organic Red Quinoa, Sea Salt, Glucono Delta Lactone), Honey, Toasted Almonds, Cinnamon",
                            nutrition="Cal=320, Total Fat=8g, Sodium=200mg, Total Carb=51g, Protein= 10g, Sugar= 7g")

        oatmeal_key = oatmeal.put()

        bowl = FoodItem(name="Vegan Lentil Quinoa Bowl", dietaryRest=["Vegan"], picture="https://www.panerabread.com/content/dam/panerabread/menu/details/vegan-lentil-quinoa-broth-bowl.jpg",
                        ingredients="Lentil Broth Bowl Blend (Citrus & Pepper Chicken (Boneless Skinless Chicken Breast Fillets With Rib Meat, Water, Seasoning [Lemon, Mangosteen, Natural Smoke Flavor], Sea Salt, Dehydrated Garlic, Dehydrated Onion, Sugar, Dry Lemon Peel, Spices, Dehydrated Rosemary, Dehydrated Basil, Citric Acid, Malic Acid And Paprika For Flavor, Vinegar, Rice Starch), Quinoa Sofrito Tomato Blend [Organic Quinoa (Water, Organic Golden Quinoa, Organic Red Quinoa, Sea Salt, Glucono Delta Lactone), Roasted Tomato Sofrito Blend (Tomatoes, Onion, Canola Oil, Extra Virgin Olive Oil, Dried Garlic, Vinegar, Salt, Sugar, Thyme)], Green Lentil Blend (Organic Green Lentil [May Contain Traces Of Wheat, Soy And Mustard], Water, Diced Tomatoes, Onion, Carrot, Celery, Canola Oil, Vegetable Base [Vegetables {Carrot, Celery, Onion}, Cane Sugar, Canola Oil, Salt, Dried Potato, Yeast Extract, Natural Flavor], Rice Starch, Sea Salt, Rasam Powder [Coriander, Chili Pepper, Red Pepper, Cumin, Fenugreek], Garlic, Sugar, Turmeric), Kale, Spinach, Organic Brown Rice (Water, Organic Brown Rice), Lemon Juice)",
                        nutrition="Cal=380, Total Fat=8g, Sodium=1040mg, Total Carb=45g, Protein= 32g, Sugar= 5g")

        bowl_key = bowl.put()

        noodles = FoodItem(name="Soba Noodle Broth Bowl with Edamame Blend", dietaryRest=["Vegan"], picture="https://www.panerabread.com/content/dam/panerabread/menu/details/soba-noodle-bowl-with-edamame.jpg",
                            ingredients="Soba Noodle Broth Bowl Blend (Soba Buckwheat Noodles (Water, Enriched Wheat Flour [Wheat Flour, Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid], Buckwheat Flour, Soybean Oil, Salt), Fire Roasted Edamame Blend (Edamame [Soy], Carrot, Red Bell Pepper, Oil [Canola And Olive Oil], Salt, Black Pepper), Napa Cabbage Blend (Napa Cabbage, Green Cabbage, Carrot, Radicchio), Spinach, Fire Roasted Mushroom And Sweet Onion Blend (Fire Roasted Brown & White Mushrooms, Fire Roasted Yellow Onions, Thyme, Canola And Olive Oil Blend, Tamari Soy Sauce [Water, Soybean, Salt, Wheat], Black Pepper, Sea Salt)), Umami Broth (Water, Umami Broth Concentrate (Red Miso (Water, Soybeans, Rice, Salt, Alcohol), Hot Pepper Paste (Corn Syrup, Rice Flour, Red Pepper Paste [Red Pepper Powder, Water, Sea Salt, Garlic, Onion], Water, Sea Salt, Gelatinized Rice Flour, Soybean Paste [Water, Soybean, Fermented Soybean, Roasted Soybean Powder, Salt, Seed Malt {Contains Wheat}], Alcohol, Red Pepper Powder, Glutinous Rice, Seed Malt [Contains Wheat]), Soybean Oil, Worcestershire Sauce",
                            nutrition="Cal=330, Total Fat=11g, Sodium=1030mg, Total Carb=46g, Protein= 12g, Sugar= 6g")

        noodles_key = noodles.put()

        #Panera Vegetarian foodItems
        ciabatta = FoodItem(name="Mediterranean Egg White on Ciabatta", dietaryRest=["Vegetarian"], picture="https://i.pinimg.com/originals/15/6c/fe/156cfe3651ac34b9d99434fcf2f6ceac.jpg",
                            ingredients="Whole Grain Lahvash (Water, Whole Wheat Flour, Enriched Flour (Wheat Flour, Malted Barley Flour, Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Wrap Base (Wheat Gluten, Corn Starch, Oat Fiber, Soy Protein Isolate, Soybean Oil, Defatted Soy Flour, Sesame Flour, Whole Wheat Flour, Dextrose), Wheat Gluten, Canola Oil, Sugar, Mold Inhibitor (Cultured Wheat Flour, Vinegar), Honey, Salt, Yeast, Ascorbic Acid, Microbial Enzymes), Egg Whites (Egg Whites, Extra Virgin Olive Oil And/Or Soybean Oil), Smoked Tomato Confit (Tomatoes, Paprika, Pepper, Salt), Feta Cheese (Pasteurized Part-Skim Milk, Cheese Culture, Salt, Microbial Enzymes), Spinach, White Bean Basil Pesto Spread (White Kidney Beans (White Kidney Beans, Water, Salt, Calcium Chloride), Corn Oil, Water, Basil, Parmesan Cheese (Cultured Part Skim Milk, Bacterial Cultures, Salt, Microbial Enzymes), Garlic, Salt, Lemon Juice Concentrate, Ascorbic Acid, Citric Acid), Sea Salt And Black Pepper Blend (Sea Salt, Black Pepper, Canola Oil)",
                            nutrition="Cal=260, Total Fat=8g, Sodium=650mg, Total Carb=31g, Protein= 19g, Sugar= 3g")

        ciabatta_key = ciabatta.put()

        soup = FoodItem(name="Autumn Squash Soup", dietaryRest=["Vegetarian"], picture="https://fakeginger.com/wp-content/uploads/2016/10/29825025590_aa97592a64_c.jpg",
                        ingredients="Pumpkin, Vegetable Stock (Water, Vegetable Base [Carrots, Celery, Onions, Tomato Paste, Corn Oil, Yeast Extract, Potato Flour, Salt, Onion Powder, Garlic Powder, Natural Flavor]), Milk, Cream Cheese (Pasteurized Milk and Cream, Cheese Culture, Salt, Carob Bean Gum), Brown Sugar, Butternut Squash, Heavy Cream, Contains 2% or less of: Carrots, Onions, Butter (Cream, Salt), Apple Juice Concentrate, Sugar, Corn Starch, Salt, Ginger Puree (Ginger, Citric Acid), Honey, Lemon Juice Concentrate, Curry Powder (Spices, Turmeric, Onions), Spices and Nisin Preparation",
                        nutrition="Cal=240, Total Fat=12g, Sodium=820mg, Total Carb=30g, Protein= 3g, Sugar= 34g")

        soup_key = soup.put()

        salad2 = FoodItem(name="Modern Greek Salad with Quinoa", dietaryRest=["Vegetarian"], picture="https://www.panerabread.com/foundation/menu/details/modern-greek-salad-with-quinoa-whole.jpg/_jcr_content/renditions/modern-greek-salad-with-quinoa-whole.desktop.jpeg",
                            ingredients="Romaine Lettuce, Quinoa Sofrito Tomato Blend (Organic Quinoa (Water, Organic Golden Quinoa, Organic Red Quinoa, Sea Salt, Glucono Delta Lactone), Roasted Tomato Sofrito Blend (Tomatoes, Onion, Canola Oil, Extra Virgin Olive Oil, Dried Garlic, Vinegar, Salt, Sugar, Thyme)), Greek Dressing (Soybean Oil, Water, Distilled Vinegar, Olive Pomace Oil, Cider Vinegar, Salt, Organic Gum Blend [Organic Gum Acacia And Organic Guar Gum], Xanthan Gum, Dehydrated Garlic, Black Pepper, Lemon Juice Concentrate, Dehydrated Tarragon, Dehydrated Oregano, Citric Acid, Dehydrated Parsley, Dehydrated Rosemary, Dehydrated Thyme, Dehydrated Bay Leaves), Kale, Cucumber, Feta Cheese (Pasteurized Part-Skim Milk, Cheese Culture, Salt, Microbial Enzymes), Toasted Almonds, Kalamata Olives (Olives, Water, Red Wine Vinegar, Sea Salt, Grape Must)",
                            nutrition="Cal=520, Total Fat=43g, Sodium=880mg, Total Carb=26g, Protein= 12g, Sugar= 4g")

        salad2_key = salad2.put()

        # Panera Lactose Intolerant foodItems
        salad3 = FoodItem(name="Spicy Thai Salad with Chicken", dietaryRest=["Lactose Intolerant"], picture="https://i.pinimg.com/originals/ff/5a/c6/ff5ac6d9c4a42ec753099cdd406ab2bd.jpg",
                            ingredients="Citrus & Pepper Chicken (Boneless Skinless Chicken Breast Fillets With Rib Meat, Water, Seasoning [Lemon, Mangosteen, Natural Smoke Flavor], Sea Salt, Dehydrated Garlic, Dehydrated Onion, Sugar, Dry Lemon Peel, Spices, Dehydrated Rosemary, Dehydrated Basil, Citric Acid, Malic Acid And Paprika For Flavor, Vinegar, Rice Starch), Fire Roasted Edamame Blend (Edamame [Soy], Carrot, Red Bell Pepper, Oil [Canola And Olive Oil], Salt, Black Pepper), Romaine Lettuce, Thai Chili Vinaigrette Dressing (Water, Rice Vinegar, Sugar, Soy Sauce [Water, Wheat, Soybean, Salt, Alcohol, Distilled Vinegar, Lactic Acid], Lemongrass, Sesame Oil, Corn Starch, Lime Juice Concentrate, Red Chili Pepper, Xanthan Gum, Natural Flavors [Kimchi, Kaffir, Lime Oil]), Crispy Wonton Strips (Wheat Flour, Canola Oil, Salt [May Contain Egg]), Roasted Cashew Pieces (Cashews, Vegetable Oil [Peanut, Canola, Sunflower And/Or Soybean Oil]), Peanut Sauce (Peanut Butter [Peanut, Peanut Or Cottonseed Oil], Soy Sauce [Water, Wheat, Soybean, Salt], Water, Brown Sugar, Tamarind Puree, Rice Vinegar, Coconut Cream, Shallots, Molasses, Orange Juice Concentrate, Distilled Vinegar, Chipotle Pepper, Cultured Sugar, Corn Starch, Aged Red Cayenne Pepper, Salt, Sesame Oil, Sugar, Rosemary Extract, Dehydrated Onion, Xanthan Gum, Dehydrated Garlic), Cilantro",
                            nutrition="Cal=490, Total Fat=21g, Sodium=970mg, Total Carb=41g, Protein= 38g, Sugar= 13g")

        salad3_key = salad3.put()

        blt = FoodItem(name="Roasted Turkey & Avocado BLT", dietaryRest=["Lactose Intolerant"], picture="https://www.panerabread.com/foundation/menu/grid/roasted-turkey-and-avocado-blt-sandwich-whole.jpg/_jcr_content/renditions/roasted-turkey-and-avocado-blt-sandwich-whole.desktop.jpeg",
                        ingredients="Roasted Turkey Breast (Turkey Breast, Water, Canola Oil, Corn Starch, Salt, Black Pepper), Country Rustic Xl Loaf (Enriched Flour (Wheat Flour, Malted Barley Flour, Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Water, Coarse Whole Wheat Flour, Salt, Yeast (Yeast, Sorbitan Monostearate, Ascorbic Acid), Dough Conditioner (Ascorbic Acid, Microcrystalline Cellulose, Corn Starch)), Tomatoes, Avocado, Applewood Smoked Bacon (Pork, Water, Sea Salt, Sugar, Celery Powder), Emerald Greens (Green Leaf Lettuce Blend), Mayonnaise (Soybean Oil, Vinegar, Eggs, Egg Yolks, Salt, Sugar, Water, Lemon Juice Concentrate, Ground Red Pepper, Dried Garlic, Mustard Oil), Sea Salt And Black Pepper Blend (Sea Salt, Black Pepper, Canola Oil)",
                        nutrition="Cal=680, Total Fat=35g, Sodium=1350mg, Total Carb=52g, Protein= 42g, Sugar= 5g")

        blt_key = blt.put()

        chili = FoodItem(name="Turkey Chili", dietaryRest=["Lactose Intolerant"], picture="https://makethebestofeverything.com/wp-content/uploads/2018/02/copycat-panera-chili-d-e1518377966113.jpg",
                        ingredients="Water, Turkey Raised without Antibiotics (Turkey, Turkey Dark Meat, Turkey Broth, Rice Starch, Salt, Rosemary Extract), Garbanzo Beans, Tomatoes (Tomatoes, Tomato Puree, Salt, Citric Acid), Kidney Beans (Dark Red Kidney Beans, Water, Salt, Calcium Chloride), Onions, Carrots, Green Chiles, Edamame (Soybeans), Contains 2% or less of: Tomato Paste, Corn, Tomatillos, Cumin, Cilantro, Canola Oil, Corn Starch, Garlic, Dried Pasilla Negro & Ancho Chiles, Yeast Extract, Brown Sugar, Sea Salt, Onion Powder, Tomato Concentrate, Lime Juice, Xanthan Gum, Citric Acid and Nisin Preparation",
                        nutrition="Cal=260, Total Fat=13g, Sodium=1210mg, Total Carb=32g, Protein= 17g, Sugar= 6g")

        chili_key = chili.put()

        # Chipotle Lactose Intolerant foodItems
        carnitas = FoodItem(name="Carnitas", dietaryRest=["Lactose Intolerant"],picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/carnitas/primary/carnitas.png",
        ingredients="Bay leaf, black pepper, juniper berries, pork, salt, sunflower oil, thyme",
        nutrition="Cal=210, Total Fat=12g, Sodium=450mg, Total Carb=0g, Protein=8.5g, Sugar=0g")

        carnitas_key = carnitas.put()

        guacamole = FoodItem(name="Guacamole", dietaryRest=["Lactose Intolerant"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/guacamole/primary/guacamole@3x.png",
        ingredients="Avocado, cilantro, jalapeno, lemon juice, lime juice, red onion, salt",
        nutrition="Cal=230, Total Fat=22g, Sodium=375mg, Total Carb=8g, Protein=2g, Sugar=1g")

        guacamole_key = guacamole.put()

        barbacoa = FoodItem(name="Barbacoa", dietaryRest=["Lactose Intolerant"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/barbacoa/Primary/barbacoa.png",
        ingredients="Bay leaf, beef, black pepper, chipotle chili, cloves, cumin, garlic, oregano, rice bran oil, salt, water",
        nutrition="Cal=170, Total Fat=7g, Sodium=530mg, Total Carb=2g, Protein=24g, Sugar=0g")

        barbacoa_key = barbacoa.put()

        # Chipotle Vegetarian foodItems
        blackbeans = FoodItem(name="Black Beans", dietaryRest=["Vegetarian"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/black-beans/primary/black-beans.png",
        ingredients="Bay leaf, black beans, black pepper, chipotle chili, cumin, garlic, lemon juice, lime juice, oregano, rice bran oil, salt, water, yellow onion",
        nutrition="Cal=130, Total Fat=1.5g, Sodium=260mg, Total Carb=22g, Protein=7g, Sugar=2g")

        blackbeans_key = blackbeans.put()

        pintobeans = FoodItem(name="Pinto Beans", dietaryRest=["Vegetarian"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/pinto-beans/primary/pinto-beans.png",
        ingredients="Bay leaf, black pepper, chipotle chili, cumin, garlic, lemon juice, lime juice, oregano, pinto beans, rice bran oil, salt, water, yellow onion",
        nutrition="Cal=130, Total Fat=1.5g, Sodium=300mg, Total Carb=21g, Protein=6g, Sugar=1g")

        pintobeans_key = pintobeans.put()

        queso = FoodItem(name="Queso", dietaryRest=["Vegetarian"],picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/queso/primary/queso@3x.png",
        ingredients="Bell pepper, black pepper, cheddar cheese, cheese cultures, chipotle chili, cornstarch, cumin, distilled vinegar, garlic, jalapeno, lemon juice, lime juice, milk, oregano, poblano pepper, red wine vinegar, salt, rice bran oil, tapioca starch, tomatillo, tomato, tomato paste, vegetable rennet, water, yellow onion",
        nutrition="Cal=120, Total Fat=8g, Sodium=200mg, Total Carb=4g, Protein=6g, Sugar=1g")

        queso_key = queso.put()

        # Chipotle Lactose intolerant foodItems
        sofritas = FoodItem(name="Sofritas", dietaryRest=["Vegan"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/sofritas/primary/sofritas.png",
        ingredients="Bell pepper, black pepper, chipotle chili, cumin, garlic, gypsum, oregano, poblano pepper, red wine vinegar, rice bran oil, salt, soy beans, tomatoes, tomato paste, water, yellow onion",
        nutrition="Cal=150, Total Fat=10g, Sodium=555mg, Total Carb=9g, Protein=8g, Sugar=5g")

        sofritas_key = sofritas.put()

        fajita = FoodItem(name="Fajita Vegetables", dietaryRest=["Vegan"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/fajita-vegetables/primary/fajita_veg.png",
        ingredients="Bell pepper, oregano, red onion, salt, sunflower oil",
        nutrition="Cal=20, Total Fat=0.5g, Sodium=170mg, Total Carb=5g, Protein=1g, Sugar=2g")

        fajita_key = fajita.put()

        rice = FoodItem(name="Ciltantro-Lime Brown Rice", dietaryRest=["Vegan"], picture="https://www.chipotle.com/content/dam/chipotle/global-site-design/en/menu/menu-items/in-store/menu-items/brown-rice/primary/brown-rice@3x.png",
        ingredients="Bay leaf, brown rice, cilantro, lemon juice, lime juice, rice bran oil, salt, water",
        nutrition="Cal=210, Total Fat=6g, Sodium=195mg, Total Carb=36g, Protein=4g, Sugar=0g")

        rice_key = rice.put()

        #ChickFilA Vegan

        salad4 = FoodItem(name="Grilled market salad (no chicken, no cheese)", dietaryRest=["Vegan"], picture="https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/marketSalad_noMeat_PDP.png",
        ingredients="Romaine lettuce, red and green apples (fresh apples, calcium ascorbate [a blend of calcium and vitamin C to maintain freshness and color]), strawberries, Granola (toasted oats [whole rolled oats",
        nutrition="210 cals, 11g fat, 24g carbs, 7g protein, 170mg sodium")

        salad4_key = salad4.put()

        superFood = FoodItem(name="Superfood side", dietaryRest=["Vegan"], picture="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Sides/Sides%20PDP/_0000s_0011_%5BFeed%5D_0003s_0001_Sides_Superfood-Side-Salad.png",
        ingredients="Broccoli, kale, maple vinaigrette dressing (maple syrup, soybean oil, water, brown sugar, onion ([including dehydrated], distilled vinegar, apple cider vinegar, soy sauce [water, soybeans, salt, alcohol], balsamic vinegar, salt",
        nutrition="140 cals, 8g fat, 16g carbs, 160mg sodium")

        superFood_key = superFood.put()

        hashbrowns = FoodItem(name="Hashbrowns", dietaryRest=["Vegan"], picture="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0009_%5BFeed%5D_0000s_0028_Breakfast_Hashbrowns_2.png",
        ingredients="Potatoes (vegetable oil [canola oil, palm oil], dehydrated potato, salt, disodium dihydrogen pyrophosphate [to promote color retention], dextrose, high oleic canola oil with Dimethylpolysiloxane added as an anti-foaming agent))",
        nutrition="250 cals, 17g fat, 23g carbs, 3g protein, 380mg sodium")

        hashbrowns_key = hashbrowns.put()

        # Chick fil a Vegetarian
        salad5 = FoodItem(name="Spicy Southwest salad (no chicken)", dietaryRest=["Vegetarian"], picture="https://www.cfacdn.com/img/order/menu/Online/Salads%26wraps/sswSalad_noMeat_pdp.png",
        ingredients="Romaine lettuce, water, seasoning [maltodextrin, spice and herb, modified food starch, tapioca maltodextrin, salt, cottonseed oil, spice and color {contains paprika}, garlic powder, natural flavoring, soy lecithin], modified food starch, salt, monosodium glutamate, sugar, spices, paprika), grape tomato, roasted corn, black beans",
        nutrition="350 cals, 17g fat, 37g carbs, 14g protein, 1060mg sodium")

        salad5_key = salad5.put()

        biscuit = FoodItem(name="Buttered biscuit", dietaryRest=["Vegetarian"], picture="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Breakfast/Breakfast%20PDP/_0000s_0018_%5BFeed%5D_0000s_0020_Breakfast_Biscuit.png",
        ingredients="Biscuit (enriched bleached wheat flour [niacin, reduced iron, thiamine mononitrate, riboflavin, folic acid], vegetable oil shortening [palm and/or palm kernel oils], sugar",
        nutrition="310 cals, 14g fat, 42g carbs, 4g protein, 720mg sodium")

        biscuit_key = biscuit.put()

        parfait2 = FoodItem(name="Greek yogurt parfait", dietaryRest=["Vegetarian"], picture="https://www.cfacdn.com/img/order/COM/PDP/Breakfast/PDP%20Greek%20Yogurt%20Parfait%20Granola.png",
        ingredients="strained yogurt strained yogurt: cultured pasteurized whole organic milk, water, organic cane sugar, natural flavors, organic locust bean gum, pectin, organic vanilla beans., Strawberries, Granola (toasted oats [whole rolled oats, soybean oil, honey], soybean oil, sugar, honey",
        nutrition="270 cals, 9g fat, 34g carbs, 13g protein, 85mg sodium")

        parfait2_key = parfait2.put()

        # Chick fil a Lactose Intolerant
        nuggets2 = FoodItem(name="8 count grilled nuggets", dietaryRest=["Lactose Intolerant"], picture="https://www.cfacdn.com/img/order/menu/Online/Entrees/grilledNuggets_8ct_PDP.png",
        ingredients="Chicken (boneless skinless chicken breast, water, seasoning [yeast extract, onion powder, sea salt, garlic powder, sugar, salt, corn maltodextrin, gum arabic, natural flavor, lemon juice concentrate, vinegar solids]",
        nutrition="110 cals, 2.5g fat, 1g carbs, 21g protein, 410mg sodium")

        nuggets2_key = nuggets2.put()

        muffin = FoodItem(name="Multigrain English Muffin", dietaryRest=["Lactose Intolerant"], picture="https://www.cfacdn.com/img/order/menu/Online/Breakfast/EMuffin_PDP.png",
        ingredients="Multigrain English muffin (enriched flour [wheat flour, malted barley flour, niacin, reduced Iron, thiamin mononitrate, riboflavin, folic acid], water, whole wheat flour, yeast, grain and seed blend [oats, rye flour, rye meal, flax seed, millet, wheat flakes], degerminated yellow corn meal, degerminated yellow corn flour",
        nutrition="150 cals, 1g fat, 30g carbs, 4g protein")

        muffin_key = muffin.put()

        sandwich = FoodItem(name="Grilled Chicken Sandwich", dietaryRest=["Lactose Intolerant"], picture="https://www.cfacdn.com/img/order/COM/Menu_Refresh/Entree/Entree%20PDP/_0000s_0009_Final__0026_CFA_PDP_Grilled-Deluxe-Sandwich_1085.png",
        ingredients="Chicken (boneless skinless chicken breast, water, seasoning [yeast extract, onion powder, sea salt, garlic powder, sugar, salt, corn maltodextrin, gum arabic, natural flavor, lemon juice concentrate, vinegar solids], chicken flavor [chicken breast meat, chicken stock, salt, maltodextrin], modified corn starch)",
        nutrition="330 cals, 6g fat, 41g carbs, 29g protein, 710mg sodium")

        sandwich_key = sandwich.put()

        # Starbucks vegan
        lentils = FoodItem(name="Lentils & Vegetable Protein Bowl With Brown Rice", dietaryRest=["Vegan"], picture="https://globalassets.starbucks.com/assets/af957809c11b4e099c2962c708964cb3.jpg",
        ingredients="Cooked brown rice (water, brown rice, olive oil [refined olive oil, extra-virgin olive oil]), black lentils (water, black lentils), lemon tahini dressing (water, sesame seeds, extra virgin olive oil, lemon juice concentrate, reduced sodium tamari soy sauce [water, soybeans, salt], parsley, agave syrup, toasted sesame oil, cilantro, salt, garlic, paprika, natural flavor), kale, broccoli, butternut squash (squash, olive oil [refined olive oil, extra-virgin olive oil]), beets, cabbage, peas, roasted tomato (tomatoes, canola oil, garlic, vinegar, salt, spices), roasted sunflower seeds (roasted sunflower seeds, [sunflower, canola or cottonseed oil], salt), roasted red bell pepper, green onion",
        nutrition="650 cals, 29g fat, 80g carbs, 23g protein, 670 mg sodium")

        lentils_key = lentils.put()

        oatmeal = FoodItem(name="Hearty Blueberry Oatmeal", dietaryRest=["Vegan"], picture="https://globalassets.starbucks.com/assets/85381ce3578f4ba094eb4ffc50c6bf60.jpg",
        ingredients="Hearty Blueberry Oatmeal [Water, Whole Grain Oatmeal(Whole Grain Rolled Oats, Whole Grain Steel Cut Oats, Whole Grain Oat Flour, Salt, Calcium Carbonate, Guar Gum), Fruit, Nut And Seed Medley (Dried Figs (Figs, Rice Flour), Pepitas, Dried Cranberries (Cranberries, Sugar, Sunflower Oil), Almonds), Blueberries, Organic Agave Nectar Syrup",
        nutrition="220 cals, 2.5g fat, 5g protein, 43g protein, 125mg sodium")

        oatmeal_key = oatmeal.put()

        cookies = FoodItem(name="Emmys Organic Coconut Cookies", dietaryRest=["Vegan"], picture="https://cdn.shopify.com/s/files/1/0147/8712/products/emmys-dark-cacao-cookie-pack_1024x1024.png?v=1560448688",
        ingredients="Organic Coconut, Organic Agave Syrup, Organic Fair-Trade Cocoa Powder, Organic Almond Flour, Organic Coconut Oil, Organic Vanilla Extract, Himalayan Salt",
        nutrition="100 cals, 8g fat, 8g carbs, 1g protein, 5mg sodium")

        cookies_key = cookies.put()

        # Starbucks Vegetarian
        sandwich2 = FoodItem(name="Egg and Cheddar Breakfast Sandwich", dietaryRest=["Vegetarian"], picture="https://media1.s-nbcnews.com/j/newscms/2017_13/1204463/starbucks-egg-cheddar-breakfast-sandwich-today-170330-tease_649e357ca9a1a65653c34b8282c2578a.fit-560w.jpg",
        ingredients="Wheat english muffin (water, organic whole wheat flour, organic enriched flour [wheat flour, niacin, reduced iron, riboflavin, thiamine mononitrate, folic acid], yeast, organic corn flour, organic dried cane syrup, organic wheat gluten, organic vinegar, sea salt, organic extra virgin olive oil, ascorbic acid, enzymes), fried egg patty (egg whites, egg yolks, milk, food starch-modified, salt, citric acid), mild cheddar cheese (cultured pasteurized milk, salt, enzymes, annatto color), butter spread (pasteurized cream [derived from milk], canola oil, vitamin a palmitate, beta carotene)",
        nutrition="280 cals, 13g fat,  27g carbs,  14g protein, 460mg sodium")

        sandwich2_key = sandwich2.put()

        sandwich3 = FoodItem(name="Spinach, Feta and Egg White Sandwich", dietaryRest=["Vegetarian"], picture="https://media1.s-nbcnews.com/j/newscms/2017_13/1204464/starbucks-spinach-feta-breakfast-wrap-today-170330-tease_054b795d92014fa09890ab2660314327.fit-560w.jpg",
        ingredients="Wrap (water, whole wheat flour, enriched wheat flour [wheat flour, malted barley flour, niacin, reduced iron, thiamin mononitrate, riboflavin, folic acid], wrap base [wheat gluten, corn starch, oat fiber, soy protein isolate, soybean oil, defatted soy flour, sesame flour, 2% or less of: whole wheat flour, dextrose], wheat gluten, canola oil, sugar, mold inhibitor [cultured wheat flour, vinegar], honey, salt, yeast, ascorbic acid, enzymes), egg white omelet (cage-free egg whites, whey powder, corn starch, nonfat dry milk, salt, xanthan gum, guar gum, liquid pepper extract), spinach, feta cheese (pastuerized milk, salt, cheese culture, enzymes, potato starch), sun dried tomato cream cheese spread",
        nutrition="280 cals, 8g fat,  34g carbs,  20g protein, 830mg sodium")

        sandwich3_key = sandwich3.put()

        bowl2 = FoodItem(name="Hearty Veggie and Brown Rice Salad Bowl", dietaryRest=["Vegetarian"], picture="https://media2.s-nbcnews.com/j/newscms/2017_13/1204476/starbucks-hearty-veggie-bowl-today-170330-tease_67a66bb6d587ef99685a93e49c8337b3.fit-560w.jpg",
        ingredients="Cooked brown rice (water, brown rice, olive oil [refined olive oil, extra virgin olive oil]), lemon tahini dressing (water, sesame seed, extra virgin olive oil, lemon juice concentrate, honey, parsley, reduced sodium tamari soy sauce [water, soybeans, salt], spice, toasted sesame oil (vegetable oil), salt, garlic, natural flavors), broccoli, butternut squash (butternut squash, olive oil [refined olive oil, extra virgin olive oil]), peas, kale, red beets, cabbage, roasted tomatoes (tomatoes, canola oil, garlic, vinegar, salt, herbs)",
        nutrition="430 cals, 22g fat,  50g carbs,  10g protein, 640mg sodium")

        bowl2_key = bowl2.put()

        # Starbucks Lactose intolerant
        bagel = FoodItem(name="Cinnamon Raisin Bagel", dietaryRest=["Lactose Intolerant"], picture="https://globalassets.starbucks.com/assets/2bb03cf9642040daa2b2ff4afc848f8e.jpg",
        ingredients="Unbleached enriched flour (wheat flour, malted barley flour, niacin, reduced iron, thiamine mononitrate, riboflavin, folic acid), water, raisins, sugar, contains 2% or less of: wheat gluten, salt, yeast, cinnamon, vinegar, guar gum, sunflower oil, ascorbic acid, enzymes, monoglycerides",
        nutrition="270 cals, 1g fat,  58g carbs,  8g protein, 370mg sodium")

        bagel_key = bagel.put()

        mocha = FoodItem(name="Soy Mocha with no Whipped Cream (Grande)", dietaryRest=["Lactose Intolerant"], picture="https://globalassets.starbucks.com/assets/7e2d6987b7404f13ab8eae0b2712dde9.jpg",
        ingredients="Organic Vanilla Soymilk [Organic Soymilk (Filtered Water, Whole Organic Soybeans), Organic Evaporated Cane Juice, Calcium Carbonate, Natural Vanilla Flavor, Sea Salt, Carrageenan, Sodium Citrate, Baking Soda, Vitamin A Palmitate, Vitamin D2, Riboflavin (B2), Vitamin B12], Brewed Espresso, Mocha Sauce [Water, Sugar, Cocoa Processed With Alkali, Natural Flavor]",
        nutrition="280 cals, 7g fat,  46g carbs,  11g protein, 110mg sodium")

        mocha_key = mocha.put()

        wrap = FoodItem(name="Seared Steak, Egg & Tomatillo Wrap", dietaryRest=["Lactose Intolerant"], picture="https://globalassets.starbucks.com/assets/00dbc4c9600d482387da9a19b3582f47.jpg",
        ingredients="homestyle tortilla (enriched unbleached wheat flour (wheat flour, enzyme (added for improved baking), niacin, reduced iron, thiamne mononitrate, riboflavin, folic acid), water, palm oil, expeller pressed canola oil, leavening (wheat starch, sodium acid pyrophosphate, sodium bicarbonate, monocalcium phosphate), cane sugar, salt, yeast, sodium bicarbonate); precooked scrambled eggs (whole eggs, water, soybean oil, modified food starch, salt, xanthan gum, guar gum, citric acid)", nutrition="410 cals, 18g fat,  43g carbs,  21g protein, 780mg sodium")

        wrap_key = wrap.put()

        # Wendy's Vegan
        potato = FoodItem(name="Sour Cream and Chive Baked Potato", dietaryRest=["Vegan"], picture="https://images.eatthismuch.com/site_media/img/607672_dillonc118_ab312029-ff9d-4673-8987-3b59dd881ec7.jpg",
        ingredients="Freeze dried chives, potatoes", nutrition="340 cals, 6g fat, 65 mg sodium, 4g sugar, 64g carbs, 9g protein")

        potato_key = potato.put()

        salad6 = FoodItem(name="Garden Side Salad(no cheese)", dietaryRest=["Vegan"], picture="https://image.zmenu.com/large/3250/20140409145232118185.png",
        ingredients="Iceberg Lettuce, Tomatoes, Romaine Lettuce, Salt, Enzymes, Annatto (Vegetable Color)], Anti-Caking Blend [Potato Starch, Powdered Cellulose, Corn Starch, Calcium Sulfate], Natamycin [A Natural Mold Inhibitor]. Soybean Oil, Water, Sunflower Oil And/Or Canola Oil, Yeast, Natural Butter Flavor, Malted Barley Flour, Citric Acid And/Or Tocopherols (To Maintain Freshness)",
        nutrition="260 cals, 18g fat, 7g protein, 19g carbs, 450 mg sodium, 4g sugar")

        salad6_key = salad6.put()

        salad7 = FoodItem(name="Apple Pecan Chicken Salad(no chicken)", dietaryRest=["Vegan"], picture="http://wendysjamaica.com/wp-content/uploads/2017/08/Apple-chicken_correct.png",
        ingredients="Pomegranate Vinaigrette Dressing: Water, Sugar, Pomegranate Juice Concentrate, Shallots, Xanthan Gum, Natural Flavor, Spice. Lecithin. Roasted Pecans: Pecans, Sugar, Honey, Corn Starch, Calcium Stearate (Anti-Caking Agent), Soy Lecithin, Maltodextrin, Xanthan Gum, Soybean Oil, Sea Salt, Cayenne Pepper.",
        nutrition="570 cals, 24g fat, 39g protein, 52g carbs, 41g sugar, 1030mg sodium")

        salad7_key = salad7.put()

        # Wendys vegetarian
        fries = FoodItem(name="French fries", dietaryRest=["Vegetarian"], picture=" https://www.seriouseats.com/images/20101201-wendysfries.jpg",
        ingredients="Potatoes, Vegetable Oil (Contains One Or More Of The Following Oils: Canola, Soybean, Cottonseed, Sunflower, Corn), Dextrose, Sodium Acid Pyrophosphate (To Maintain Natural Color). Cooked In Vegetable Oil (Soybean Oil, Vegetable Oil [May Contain One Or More Of The Following: Canola, Corn, Or Cottonseed], Hydrogenated Soybean Oil, Dimethylpolysiloxane [Anti-Foaming Agent]. Salt: Sea Salt",
        nutrition="320 cals, 15g fat, 5g protein, 320 mg sodium, 0g sugar, 42g carbs")

        fries_key = fries.put()

        apples = FoodItem(name="Apple Bites", dietaryRest=["Vegetarian"], picture="https://images.eatthismuch.com/site_media/img/172595_dillonc118_f1689b2c-899a-4b92-829b-22ae18af5ca6.jpg",
        ingredients="Apples, Calcium Ascorbate", nutrition="35 cals, 0g protein, 0g fat, 8g carbs, 0mg sodium, 6g sugar")

        apples_key = apples.put()

        potato2 = FoodItem(name="Cheese Baked Potato", dietaryRest=["Vegetarian"], picture="http://wendysjamaica.com/wp-content/uploads/2017/08/Cheese-n-cheese2.png",
        ingredients="Cheddar Cheese Sauce: Water, Cheddar Cheese (Pasteurized Milk, Salt, Cultures, Enzymes), Milk, Modified Corn Starch, Butter (Cream, Salt), Canola Oil, Natural Flavor, Salt, Sodium Citrate, Whey Protein Concentrate, Soy Lecithin. Potato : Potato.",
        nutrition="450g cals, 15g protein, 14g fat, 65g carbs, 690mg sodium, 4g sugar")

        potato2_key = potato2.put()

        #Wendys Lactose intolerant
        hamburger2 = FoodItem(name="Jr Hamburger", dietaryRest=["Lactose Intolerant"], picture="https://image.zmenu.com/large/3250/20140409145309900710.png",
        ingredients="Sandwich Bun: Flour (Wheat Flour, Malted Barley Flour, Niacin, Reduced Iron, Thimain Mononitrate, Riboflavin, Folic Acid), Water, High Fructose Corn Syrup, Yeast, Soybean Oil, Ascorbic Acid, Datem, Mono- And Di-Glycerides (May Be Ethoxylated), Calcium Peroxide, Sodium Stearoyl, Jr. Hamburger Patty: Ground Beef, Salt.",
        nutrition="240 cals, 14g protein, 10g fat, 25g carbs, 5g sugar, 470mg sodium")

        hamburger2_key = hamburger2.put()

        sandwich4 = FoodItem(name="Spicy Chicken Sandwich", dietaryRest=["Lactose Intolerant"], picture="http://wendysjamaica.com/wp-content/uploads/2017/05/119.png",
        ingredients="Premium Bun: Enriched Flour (Wheat Flour, Malted Barley Flour, Niacin, Reduced Iron, Thiamine Mononitrate, Riboflavin, Folic Acid), Water, High Fructose Corn Syrup, Hydrogenated Soybean Oil, Dimethylpolysiloxane [Anti-Foaming Agent].",
        nutrition="500 cals, 19g fat, 28g protein, 990mg sodium, 5g sodium, 51g carbs")

        sandwich4_key = sandwich4.put()

        potato3 = FoodItem(name="Plain baked potato", dietaryRest=["Lactose Intolerant"], picture="https://images.eatthismuch.com/site_media/img/172386_dillonc118_2a12d78c-0bd1-4788-9ecb-de6b1c62ee57.jpg",
        ingredients="Potato", nutrition="270 cals, 7g protein, 0g fat, 61g carbs, 25mg sodium, 3g sugar")

        potato3_key = potato3.put()

        # Restaurant initialization
        mcdonalds = Restaurant(name="McDonalds", picture="https://vignette.wikia.nocookie.net/ronaldmcdonald/images/b/b5/Mcdonalds-logo-current-1024x750.png/revision/latest/scale-to-width-down/180?cb=20180730081148",
                               veganItems=[mapleOatmeal_key, sideSalad_key, fruit_key], vegetarianItems=[fruitParfait_key, mcmuffin_key, mcwrap_key], lactoseItems=[hamburger_key, mcchicken_key, nuggets_key])
        mcdonalds.put()

        chipotle = Restaurant(name="Chipotle", picture="https://1000logos.net/wp-content/uploads/2017/11/Chipotle-Logo-768x563.png", veganItems=[rice_key, fajita_key, sofritas_key],
                            vegetarianItems=[blackbeans_key, pintobeans_key, queso_key], lactoseItems=[guacamole_key, carnitas_key, barbacoa_key])
        chipotle.put()

        panera = Restaurant(name="Panera", picture="https://1000logos.net/wp-content/uploads/2017/09/Panera-Logo-768x549.png", veganItems=[oatmeal_key, bowl_key, noodles_key],
                            vegetarianItems=[ciabatta_key, soup_key, salad2_key], lactoseItems=[salad3_key, blt_key, chili_key])
        panera.put()
        self.response.write("data has been seeded")

        chickfila = Restaurant(name="Chickfila", picture="https://s3-media4.fl.yelpcdn.com/bphoto/E7oOqJWxZ9Z3gNhD97KQXw/o.jpg",
                               veganItems=[hashbrowns_key, salad4_key, superFood_key], vegetarianItems=[salad5_key, biscuit_key, parfait2_key], lactoseItems=[nuggets2_key, muffin_key, sandwich_key])
        chickfila.put()

        starbucks = Restaurant(name="Starbucks", picture="https://www.stickpng.com/assets/images/58428cc1a6515b1e0ad75ab1.png",
                               veganItems=[lentils_key, oatmeal_key, cookies_key], vegetarianItems=[sandwich2_key, sandwich3_key, bowl2_key], lactoseItems=[bagel_key, mocha_key, wrap_key])

        starbucks.put()

        wendys = Restaurant(name="Wendys", picture="http://pluspng.com/img-png/wendys-logo-png-die-besten-25-wendys-logo-ideen-auf-pinterest-lustig-disney-kunstreferenz-und-lebenstricks-webseiten-550.png",
                            veganItems=[potato_key, salad6_key, salad7_key], vegetarianItems=[fries_key, apples_key, potato2_key], lactoseItems=[hamburger2_key, sandwich4_key, potato3_key])

        wendys.put()


class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        AboutUsHandler_template = the_jinja_env.get_template('templates/aboutus.html')
        self.response.write(AboutUsHandler_template.render())

class FoodListHandler(webapp2.RequestHandler):
    def get(self):
        RestaurantHome_template = the_jinja_env.get_template('templates/foodList.html')
        restaurant_name = self.request.get("restaurant")
        restriction_name = self.request.get("restriction")
        restaurant_entity = Restaurant.query(Restaurant.name==restaurant_name).get()
        print restaurant_entity
        foodItems = []
        if restriction_name == "vegan":
            foodItems = restaurant_entity.veganItems
        elif restriction_name == "vegetarian":
            foodItems = restaurant_entity.vegetarianItems
        elif restriction_name == "lactose_intolerant":
            foodItems = restaurant_entity.lactoseItems
        print foodItems
        self.response.write(RestaurantHome_template.render(
            {"restaurant_name":restaurant_name, "restriction": restriction_name, "foodItems": foodItems}))

class FoodItemHandler(webapp2.RequestHandler):
    def get(self):
        FoodItem_template = the_jinja_env.get_template('templates/foodItem.html')
        foodId = self.request.get("foodid")
        foodItem_entity = FoodItem.get_by_id(int(foodId))
        print foodItem_entity
        self.response.write(FoodItem_template.render(
           {'foodItem': foodItem_entity}
        ))

app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/restaurants', RestaurantHandler),
    ('/seeddata', SeedDataHandler),
    ('/restaurantHome', RestaurantHomeHandler),
    ('/aboutus', AboutUsHandler),
    ('/foodList', FoodListHandler),
    ('/foodItem', FoodItemHandler),
], debug=True)
