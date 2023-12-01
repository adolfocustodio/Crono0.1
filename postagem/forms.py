from django import forms
from django.forms import ModelForm
from .models import Postagem


class PostagemForm(ModelForm):
    
    class Meta:
        model = Postagem
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'})
        }
