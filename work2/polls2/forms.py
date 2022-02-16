from django import forms
class ContactForm(forms.Form):
  name =forms.CharField(max_length=77)
  email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  password = forms.CharField(widget=forms.PasswordInput())
  address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
  address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
  city = forms.CharField()
  zip_code = forms.CharField(label='Zip')
  check_me_out = forms.BooleanField(required=False)