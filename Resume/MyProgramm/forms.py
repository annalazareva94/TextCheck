from. models import Text
from. models import TextFormat
from. models import Word
from django.forms import ModelForm, Textarea, TextInput

class TextForm (ModelForm):
    class Meta:
        model = Text
        fields = ['full_text']

        widgets = {
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Сюда'
            })
        }


class TextFormatForm (ModelForm):
    class Meta:
        model = TextFormat
        fields = ['format_text']

        widgets = {
            'format_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }

class WordForm (ModelForm):
    class Meta:
        model = Word
        fields = ['full_word']

        widgets = {
            "full_word": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Слово'
            })
        }