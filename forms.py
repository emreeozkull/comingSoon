from django import forms
from .models import MailList



class NameForm(forms.Form):
    email = forms.EmailField(label="", error_messages= None,widget=forms.EmailInput(attrs={
        'id' : 'input' , 
        'autocomplete': 'off',
        'placeholder': ('E-posta adresinizi girin.'),
    }))


    class Meta:
        model = MailList 
        fields = ['email']