$( document ).ready(function() {
    $( ".square" ).on( "click", function() {
        alert($(this).attr("id"));
    } );
});