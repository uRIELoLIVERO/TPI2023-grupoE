/* navbar */
const menuNavbar = document.querySelector('#burgerMenu')
const menuInfo = document.querySelector('#infoMenu')
/* menu */
const buttonFilter = document.querySelector('#filter-options')
const menuFilter = document.querySelector('#filter-form')
const containerFind = document.querySelector('#containerFind')
/* detalle de entrega */
const botonObtenerPedido = document.querySelector('#boton-continuar-pedido')

menuNavbar.addEventListener('click', toggleMenu)
buttonFilter.addEventListener('click', toggleFilter)
botonObtenerPedido.addEventListener('click', obtenerData)

function toggleMenu (){
    menuInfo.classList.toggle('inactive')
    menuNavbar.classList.toggle('superponer')
}
function toggleFilter(){
    menuFilter.classList.toggle('inactive')
    containerFind.classList.toggle('margin-largo')
    containerFind.classList.toggle('margin-corto')
}

function obtenerData(){
  const fechaYHoraPedido = document.querySelector('#input-date-detalleEntrega').value
  const ubicacionEntregaPedido = document.querySelector('#ubicacionEntrega').value
  const aclaracionPedido = document.querySelector('#textArea-Entrega').value
  const detallePagoPedido = document.querySelector('#tipoCuenta').value
  const AreaDePago = document.querySelector('#areas').value
  console.log(fechaYHoraPedido)
  console.log(ubicacionEntregaPedido)
  console.log(aclaracionPedido)
  console.log(detallePagoPedido)
  console.log(AreaDePago)
}
//obtener datos de EntregaYPago


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
