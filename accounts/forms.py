from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return name.strip()

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        return email.strip()

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) > 2000:
            raise forms.ValidationError('Message is too long (max 2000 characters).')
        return message
