#!/usr/bin/python3

import json
import io
import re

import cgi, cgitb

# Get id from field

query = cgi.FieldStorage()
recipeId = query.getvalue('id')


#get recipe
dbFile = open('db-recipes.json','r')
db = json.loads(dbFile.read())

recipe = db[recipeId]

#otput ingredients into pop-up
print("Content-type:text/html\r\n\r\n")
print('<b>Ingredients:</b><br>');


for ingredient in recipe['ingredients']:
    if ingredient.rstrip() == '<hr>':
      print('<hr>')
    else:
      print('{};'.format(ingredient.rstrip()))
