
from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [ 
    path('add/', CreateProdutoView.as_view(), name="add"),
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/update', UpdateProdutoView.as_view(), name="update"),
    path('<int:pk>/delete', DeleteProdutoView.as_view(), name="delete"),
]