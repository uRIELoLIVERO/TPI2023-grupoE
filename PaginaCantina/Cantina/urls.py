from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('a', mysite),
    path('', login_view, name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword.html'), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='resetPasswordDone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetPasswordConfirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='resetPasswordComplete.html'), name='password_reset_complete'),
    path('miCarrito/', views.miCarrito, name='miCarrito'),
    path('detallePago/',views.detallePago, name='detallePago'),
    path('productos/', consultarProductos, name='consultarProductos'),
    path('detalledePago/', detalledePago, name='detalledePago'),
    path('detalledeEntrega/', detalledeEntrega, name='detalledeEntrega'),
]

