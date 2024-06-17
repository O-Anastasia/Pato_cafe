from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    """
    Class for creating and updating reservations
    """

    class Meta:
        model = Reservation
        fields = ('date', 'time', 'people', 'name', 'phone', 'email')
        widgets = {
            'date': forms.TextInput(attrs={'class': 'my-calendar bo-rad-10 sizefull txt10 p-l-20', 'id': 'date',
                                           }),
            'time': forms.TextInput(attrs={'id': 'time',
                                           }),
            'people': forms.NumberInput(attrs={'id': 'people',
                                               }),
            'name': forms.TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'id': 'name', 'placeholder': 'Name',
                                           }),
            'phone': forms.TextInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'id': 'phone', 'placeholder': 'Phone',
                                            }),
            'email': forms.EmailInput(attrs={'class': 'bo-rad-10 sizefull txt10 p-l-20', 'id': 'email', 'placeholder': 'Email',
                                             }),
        }
        labels = {
            'date': 'Date',
            'time': 'Time',
            'people': '# of people',
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email',
        }


