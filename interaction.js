
//global list of ingredients
var ingredients = [];

$(document).ready(function(){
  //add listners to buttons
  $('#igredient-btn').click(onIngredientAdd);

  $('#rm-1').click(onIngredientRemove);
  $('#rm-2').click(onIngredientRemove);
  $('#rm-3').click(onIngredientRemove);
  $('#rm-4').click(onIngredientRemove);
  $('#rm-5').click(onIngredientRemove);
  $('#rm-6').click(onIngredientRemove);
  $('#rm-7').click(onIngredientRemove);
  $('#rm-8').click(onIngredientRemove);
  $('#rm-9').click(onIngredientRemove);
  $('#rm-last').click(onIngredientRemove);

  //$('#get-recipes-btn').click(getRecipes);
  $('#get-clear-all-btn').click(resetAll);

  //hook enter to ingredient
  $("#ingredient-text").keyup(function(event){
    if(event.keyCode == 13){
        $("#igredient-btn").click();
    }
});

  //update fridge
  updateFrig();

} );

//functions for buttons
function onIngredientAdd() {

  var ingredient = $('#ingredient-text').val().trim().toLowerCase();
  if (ingredient != '') {
    if (ingredients.length == 10) {
      window.alert('10 ingredients is maximum');

    } else {
      ingredients.push(ingredient)
      //update refrigerator
      updateFrig();
    }
    //clear the field
    $('#ingredient-text').val('');
  }
}

function updateFrig(){
  //clear all previous text in blocks, remove inner block and collapse fridge
  for (var i = 1; i < 10; i++){
    //remove text
    $('#ing-text-' + i).text('');
    //hide the block
    $('#ing-' + i).hide();
    //hide section of ref if needed
    if (i > 2) {
      $('#insert-' + (i - 2)).hide();
    }
  }
  //clear and hide bottom section
  $('#ing-text-last').text('');
  $('#ing-last').hide();

  //update fridge with new values
  var updateLimit = ingredients.length > 2 ? ingredients.length - 1 : ingredients.length;
  for (var i = 0; i < updateLimit; i++) {
    $('#ing-text-' + (i + 1)).text(ingredients[i]);
    $('#ing-' + (i + 1)).show();
    //add new fer section if i bigger then 2
    if (i > 1){
      $('#insert-' + (i - 1)).show();
    }
  }
  //update last section if len is bigger then 2
  if (ingredients.length > 2) {
    $('#ing-text-last').text(ingredients[ingredients.length - 1]);
    $('#ing-last').show();
  }

  //update JSON of hiddent form input
  var ingJson = JSON.stringify(ingredients)

  $('#json-ingradients').val(ingJson);

}

function onIngredientRemove() {
  //this id
  var position = this.id.replace('rm-','');
  if (position == 'last') {
    ingredients.pop();
  } else {
    ingredients.splice(+position - 1, 1);
  }
  //update fridge
  updateFrig();
}

function getRecipes() {

}

function resetAll() {
  ingredients = [];
  updateFrig();
}
