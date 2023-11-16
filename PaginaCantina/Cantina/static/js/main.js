const menuNavbar = document.querySelector('#burgerMenu')
const menuInfo = document.querySelector('#infoMenu')
const buttonFilter = document.querySelector('#filter-options')
const menuFilter = document.querySelector('#filter-form')
const containerFind = document.querySelector('#containerFind')

menuNavbar.addEventListener('click', toggleMenu)
buttonFilter.addEventListener('click', toggleFilter)

function toggleMenu (){
    menuInfo.classList.toggle('inactive')
    menuNavbar.classList.toggle('superponer')
}
function toggleFilter(){
    menuFilter.classList.toggle('inactive')
    console.log('hola')
    containerFind.classList.toggle('margin-largo')
    containerFind.classList.toggle('margin-corto')
}

//*==========Scroll Up Logo===============*//

var initialSrc = "{ % static 'images/logo_horizontal_blanco_utn.png'% }";
var scrollSrc = "{ % static 'images/logo_horizontal_blanco_utn.png'% }";

var initialSrc2 = "{ % static 'images/logo_horizontal_blanco_utn.png'% }";
var scrollSrc2 = "{ % static 'images/logo_horizontal_blanco_utn.png'% }";

$(window).scroll(function() {
   var value = $(this).scrollTop();
   if (value > 50)
      $(".top-logo").attr("src", scrollSrc),
      $(".top-logo2").attr("src", scrollSrc2);
   else
      $(".top-logo").attr("src", initialSrc),
      $(".top-logo2").attr("src", initialSrc2);
});


//**===================Scroll UP ===================**//

$(document).ready(function () {

  $(window).scroll(function () {
      if ($(this).scrollTop() > 150) {
          $('.scrollup-icon').fadeIn();
      } else {
          $('.scrollup-icon').fadeOut();
      }
  });

  $('.scrollup-icon').click(function () {
      $("html, body").animate({
          scrollTop: 0
      }, 1000);
      return false;
  });

});
