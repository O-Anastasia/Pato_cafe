from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('date', 'time', 'people', 'name', 'phone', 'email')
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Date',
                                           'data-rule': 'minlen:4'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'id': 'time', 'placeholder': 'Time',
                                           'data-rule': 'minlen:4'}),
            'people': forms.NumberInput(attrs={'class': 'form-control', 'id': 'people', 'placeholder': '# of people',
                                               'data-rule': 'minlen:4'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name',
                                           'data-rule': 'minlen:4'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone',
                                            'data-rule': 'minlen:4'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email',
                                             'data-rule': 'minlen:4'}),
        }
        labels = {
            'date': 'Date',
            'time': 'Time',
            'people': '# of people',
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email',
        }


