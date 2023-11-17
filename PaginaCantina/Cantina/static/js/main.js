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

/* muesta un metodo, detalleDeENtregaYPago */
function mostrarOcultar() {
    var tipoCuenta = document.getElementById("tipoCuenta");
    var cvuContainer = document.getElementById("cvuContainer");
    var areasSelect = document.getElementById("areasSelect");

    if (tipoCuenta.value === "transferencia") {
      cvuContainer.style.display = "block";
      areasSelect.style.display = "none";
    } else if (tipoCuenta.value === "cuentaCorriente") {
      cvuContainer.style.display = "none";
      areasSelect.style.display = "block";
    } else {
      cvuContainer.style.display = "none";
      areasSelect.style.display = "none";
    }
  }