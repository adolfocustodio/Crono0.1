from django.urls import path
from . import views


app_name = "postagem"
urlpatterns = [
    path('postagem/criar/', views.PostagemCreateView.as_view(), name='postagem-criar'),
    path('postagem/editar/<int:pk>/', views.PostagemUpdateView.as_view(), name='postagem-editar'),
    path('postagem/remover/<int:pk>/', views.PostagemDeleteView.as_view(), name='postagem-remover'),
]
