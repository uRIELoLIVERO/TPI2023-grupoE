
    $(document).ready(function() {
      // Manejar el evento de cambio en el input de búsqueda
      $('.input-interno').on('input', function() {
        var searchTerm = $(this).val().toLowerCase();

        // Filtrar los productos por nombre
        $('#product-list-container .product-card').each(function() {
          var productName = $(this).find('.product-name').text().toLowerCase();
          if (productName.includes(searchTerm)) {
            $(this).show();
          } else {
            $(this).hide();
          }
        });
      });
    });