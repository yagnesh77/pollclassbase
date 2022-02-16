from django import forms
class ContactForm(forms.Form):
  name =forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
  email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
  address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Address'})
    )
  address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, or floor'})
    )
  city = forms.CharField()
  zip_code = forms.CharField(label='Zip')
  check_me_out = forms.BooleanField(required=False)