from django.urls import path
from . import views

urlpatterns = [
  # path("", views.home, name="home"),
  # path("comunidades/", views.comunidades, name="comunidades"),
  # path("comunidad/<int:pk>", views.comunidad, name="comunidad"),
  # path("delegadas/", views.delegadas, name="delegadas"),
  # path("delegada/<int:pk>", views.delegada, name="delegada"),
  # path("productos/", views.productos, name="productos"),
  # path("producto/<int:pk>", views.producto, name="producto"),
  # path("pedidos/", views.pedidos, name="pedidos"),
  # path("pedido/<int:pk>", views.pedido, name="pedido"),
# path(comur'^nidades/$', views.comunidades_lista),
  # path(r'^comunidades/(?P<pk>[0-9]+)/$', views.comunidad_individual),
  path('comunidades/', views.comunidades_lista),
  path('comunidad/<int:pk>', views.comunidad_individual),
  path('delegadas/', views.delegadas_lista),
  path('delegada/<int:pk>', views.delegada_individual),
  path('productos/', views.productos_lista),
  path('producto/<int:pk>', views.producto_individual),
  path('pedidos/', views.pedidos_lista),
  path('pedido/<int:pk>', views.pedido_individual),
]
