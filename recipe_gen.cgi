#!/usr/bin/python3

import json
import io
import cgi, cgitb


# Get id from field

query = cgi.FieldStorage()
recipeId = query.getvalue('id')

#for test
#recipeId = 'id278'

dbFile = open('db-recipes.json','r')
db = json.loads(dbFile.read())

recipe = db[recipeId]

#build webpage
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>{}</title>".format(recipe['name']))
print('<link rel="stylesheet" href="recipe.css" type="text/css">')
print("</head>")
print("<body>")
print("<h1>{}</h1>".format(recipe['name']))
#make list of ingredients
qty = recipe['servings']
if qty == 1:
    print("<h3>Ingredients and quantities for 1 portion</h3>")
elif qty > 1:
    print("<h3>Ingredients and quantities for {} portions</h3>".format(qty))
else:
    print(print("<h3>Ingredients and quantities</h3>"))

print('<ul>')
for ingredient in recipe['ingredients']:
    print('<li>{}</li>'.format(ingredient.rstrip()))
print('</ul>')

#instructions
print('<h3>Instructions</h3>')
print('<p>{}</p>'.format(recipe['instructions'].replace('\r\n\r\n','<br>')))
print("</body>")
print("</html>")
