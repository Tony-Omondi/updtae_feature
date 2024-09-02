# forms.py
from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=15)
    date = forms.DateField(label='Date', widget=forms.TextInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='Time', widget=forms.TextInput(attrs={'type': 'time'}))
    number_of_people = forms.IntegerField(label='Number of People')
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 4}), required=False)
