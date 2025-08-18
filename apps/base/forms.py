from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.CharField(max_length=255)   # было: forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=4000)

    # опционально можете подчистить пробелы:
    def clean_email(self):
        return self.cleaned_data['email'].strip()