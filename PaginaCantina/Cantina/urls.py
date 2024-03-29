from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from . import views
from . import views as cantina_views
urlpatterns = [
    path('a', mysite),
    path('', login_view, name='login'),
    
    # Password reset views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword.html'), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='resetPasswordDone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetPasswordConfirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='resetPasswordComplete.html'), name='password_reset_complete'),
    
    # Cart and product views
    path('miCarrito/', views.miCarrito, name='miCarrito'),
    path('productos/', views.consultarProductos, name='consultarProductos'),
    path('detalleDeEntregaYPago/', detalleDeEntregaYPago, name='detalleDeEntregaYPago'),
    path('detalledePago/', detalledePago, name='detalledePago'),
    path('detalledeEntrega/', detalledeEntrega, name='detalledeEntrega'),
    path('productosCarrito/', productos_en_carrito, name='productosCarrito'),
    path('actualizar_carrito/<int:product_id>/', actualizar_carrito, name='actualizar_carrito'),
    path('quitarProducto/<int:product_id>/', quitarProducto, name='quitarProducto'),
    path('actualizar_subtotal/', actualizar_subtotal, name='actualizar_subtotal'),
    
    # Other views
    path('verCtaCte/', views.verCtaCte, name='verCtaCte'),
    path('resetPassword2/', views.resetPassword2, name='resetPassword2'),
    path('consultarPedidos/', views.consultarPedido, name='consultarPedido'),
    path('revisionPedido/', views.revisionPedido, name='revisionPedido'),
    path('detallePagoFinal/', views.detallePagoFinal, name='detallePagoFinal'),
    path('guardar_datos/', guardar_datos, name='guardar_datos'),
    path('obtener_areas/', obtener_areas, name='obtener_areas'),
    path('detalle_pedido/', detalle_pedido, name='detalle_pedido'),
    path('calcular_total/', calcular_total, name='calcular_total'),

    path('pedidos/', cantina_views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pedido_id>/', cantina_views.detalles_pedido, name='detalles_pedido'),
    path('obtener_pedidos/', cantina_views.obtener_pedidos, name='obtener_pedidos'),
]
