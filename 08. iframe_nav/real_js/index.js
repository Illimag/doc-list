









$("#link2").click(function(){


parent.proFunction();

});

   
$("#link3").click(function(){


parent.proFunction();

});

   





$('.navdown ul li').on('click', function(){
    $('ul li.active1').removeClass('active1');
    $(this).addClass('active1');
});












$("#test1").on('click', function() {
  


var src = $(this).data('src'),
        width = $(this).data('width'),
        height = $(this).data('height');
    $('#iframe1').css({
        width: width,
        height: height
    }).attr('src', src);



});




$("#test2").on('click', function() {
  


var src = $(this).data('src'),
        width = $(this).data('width'),
        height = $(this).data('height');
    $('#iframe1').css({
        width: width,
        height: height
    }).attr('src', src);



});





$("#test3").on('click', function() {
  


var src = $(this).data('src'),
        width = $(this).data('width'),
        height = $(this).data('height');
    $('#iframe1').css({
        width: width,
        height: height
    }).attr('src', src);



});





