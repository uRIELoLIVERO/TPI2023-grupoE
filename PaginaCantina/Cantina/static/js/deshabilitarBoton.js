document.addEventListener("DOMContentLoaded", function() {

    var buttons = document.querySelectorAll('.btn-cancelarPedido');

    buttons.forEach(function(button) {
        var status = button.closest('.accordion-item').querySelector('.status-request .titulos-principal').textContent.trim();

        if (status === "Entregado" || status === "Cancelado") {
            button.disabled = true;
        } else {
            button.addEventListener('click', cancelarPedido);
        }
    });

    function cancelarPedido(event) {
        var clickedButton = event.target;
        var statusElement = clickedButton.closest('.accordion-item').querySelector('.status-request .titulos-principal');
        statusElement.textContent = "Cancelado";

        var statusIcon = statusElement.nextElementSibling.querySelector('img.status-request-image');
        statusIcon.src = "/static/images/crossed.png"; 
        
        clickedButton.disabled = true;
    }
});