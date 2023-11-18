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

//agregar al carrito html 
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Busca el nombre del token CSRF
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

document.getElementById('btnIrAPagar').addEventListener('click', function () {
var productos = [];

// Itera sobre cada fila de producto y recopila los datos
$('.fila-objeto').each(function () {
    var productId = $(this).data('product-id');
    var cantidad = parseInt($(this).find('.cantidad').text());
    var subtotal = parseFloat($(this).find('.subtotal').text().replace('$', ''));

    // Agrega los datos al array de productos
    productos.push({
        id: productId,
        cantidad: cantidad,
        subtotal: subtotal
    });
});

// Obtiene el token CSRF
var csrftoken = getCookie('csrftoken');

// Realiza una solicitud AJAX para enviar los datos al servidor con el token CSRF
$.ajax({
    type: 'POST',
    url: '/guardar_datos/',
    data: {
        csrfmiddlewaretoken: csrftoken,
        productos: JSON.stringify(productos)
    },
    success: function (data) {
        console.log('Datos guardados con éxito');
    },
    error: function (error) {
        console.error('Error al intentar guardar los datos:', error);
    }
});
});
