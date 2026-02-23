from django import forms
from .models import Contatto

# class FormContatto(forms.Form):
#     nome = forms.CharField()
#     cognome = forms.CharField()
#     email = forms.EmailField()
#     contenuto = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Scrivi qui il tuo messaggio'}))


class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"