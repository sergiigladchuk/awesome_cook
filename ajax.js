$(document).ready(function(){

    $('a').hover(function(){
        //variable for popUp
        var popUp = $(this).parent().children('.pop-up');
        var recipeId = $(this).parent().attr('name');
        //check if pop-up is empty
        if (popUp.html() == '') {
          //call server
          $.ajax({
                'type': 'GET',
                'url': 'hover.cgi?id=' + recipeId,
                'dataType': 'html',
                'success': function (data) {
                    console.log(data);
                    popUp.html(data);
                    //show box
                    popUp.show();
                }
            });
        } else {
          //just show box
          popUp.show();
        }
      }, function(){
        //This function is for unhover.
        $(this).parent().children('.pop-up').hide()
     });


 });
