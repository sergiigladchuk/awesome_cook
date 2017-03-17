#!/usr/bin/python3
import json
import io
import re
import cgi, cgitb

# Get id from field
query = cgi.FieldStorage()
ingJson = query.getvalue('json-ingredients')
ingredients = json.loads(ingJson)

ingredRegex = re.compile('.*(' + '|'.join(ingredients) + ').*', re.I)

dbFile = open('db-recipes.json','r')
db = json.loads(dbFile.read())

#loop through each recipe and find best matching
selectedRecipes = []
for recipeId in db:

    #loop through ingreadients and count matche vs input igradients
    recipeScore = 0
    recipe = db[recipeId]
    for checkIngredientStr in recipe['ingredients']:

        #check with input
        if re.match(ingredRegex, checkIngredientStr) != None:
            recipeScore += 1

    if recipeScore > 0:
        recipe['score'] = recipeScore
        selectedRecipes.append(recipe)

#sort the recipes based on score
sortedRecipes = sorted(selectedRecipes, key=lambda k: k['score'], reverse=True)

#build html content for top 10 hits
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Recipes</title>")
print('<link rel="stylesheet" href="output.css" type="text/css">')
print('<script src="jquery-3.1.1.min.js"></script>')
print('<script type="text/javascript" src="ajax.js"></script>')
print("</head>")
print("<body>")
print('<section class="main">')
print("<h1>Your recipes</h1>")

limCount = 0
for recipeOut in sortedRecipes:
    #<a href="./cgi-bin/run_script.cgi?param=value">Query</a>
    print('<div class="recipe-line" name="{}">'.format(recipeOut['id']))
    print('<a href="recipe_gen.cgi?id={}">{}</a>'.format( recipeOut['id'], recipeOut['name']) )
    print('<div class="pop-up"></div>')
    print('</div>')
    limCount += 1
    if limCount == 10:
        break
print('</section>')
print("</body>")
print("</html>")
