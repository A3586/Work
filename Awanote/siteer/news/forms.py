from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'text','who']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заметки',

            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'rows': '5',
                'placeholder': 'Текст заметки'

            }),
            'who': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Чья заметка',
                'type':'number'
            }),
        }
