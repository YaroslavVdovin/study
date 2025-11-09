from django import forms
from .models import Contact, Review


class Feedback(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message'
        )

class ProductRevForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rev_text',
                  'email']