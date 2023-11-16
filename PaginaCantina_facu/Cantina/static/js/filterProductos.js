document.addEventListener("DOMContentLoaded", function () {
    var filterToggle = document.getElementById("toggle-filter");
    var filterDropdown = document.getElementById("filter-dropdown");

    filterToggle.addEventListener("click", function (event) {
        event.preventDefault();
        filterDropdown.style.display = (filterDropdown.style.display === "none" || filterDropdown.style.display === "") ? "block" : "none";
    });

    document.getElementById("filter-price-max-to-min").addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "{% url 'consultarProductos' %}?tipo_orden=mayor-menor";
    });

    document.getElementById("filter-price-min-to-max").addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "{% url 'consultarProductos' %}?tipo_orden=menor-mayor";
    });

    document.getElementById("filter-alphabetical-a-z").addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "{% url 'consultarProductos' %}?tipo_orden=A-Z";
    });

    document.getElementById("filter-alphabetical-z-a").addEventListener("click", function (event) {
        event.preventDefault();
        window.location.href = "{% url 'consultarProductos' %}?tipo_orden=Z-A";
    });
});