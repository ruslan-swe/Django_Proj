from django import forms
from .models import ContactData


class FooterForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(
        attrs={'autocomplete': 'email'}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactData
        include = "__all__"
        exclude = []
        fields = []
        labels = {
            "full_name": "Ad",
            "email": "Email",
            "message": "Mesaj",
            "phone": "Mobil Nömrə"
        }
