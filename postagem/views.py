from .models import Postagem
from .forms import PostagemForm
from django.views import generic
from django.contrib.messages import views
from django.urls import reverse_lazy


class PostagemCreateView(generic.CreateView, views.SuccessMessageMixin):
    model = Postagem
    form_class = PostagemForm
    success_url = reverse_lazy("core:home")
    success_message = "Postagem cadastrada com sucesso!"


class PostagemUpdateView(generic.UpdateView, views.SuccessMessageMixin):
    model = Postagem
    form_class = PostagemForm
    success_url = reverse_lazy("core:home")
    success_message = "Postagem atualizada com sucesso!"


class PostagemDeleteView(generic.DeleteView):
    model = Postagem
    success_url = reverse_lazy("core:home")
