from django import forms
from .models import Location, User, Person, STATE_CHOICES, GENDER_CHOICES


class DateInput(forms.DateInput):
    input_type = 'date'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_id',
                  'address',
                  'zip_code',
                  'state',
                  'city'
                  ]
        widgets = {
            'address': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your address',
                    'rows': 1,
                    'cols': 30
                }
            ),
            'state': forms.Select(
                choices=STATE_CHOICES
            ),
            'zip_code': None
        }
        labels = {
            'address': 'Address'
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields["address"].initial = ""


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['nic',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'phone',
                  'profession',
                  'gender']

        labels = {
            'nic': 'NIC'
        }

        widgets = {
            'date_of_birth': DateInput(),
            'gender': forms.Select(
                choices=GENDER_CHOICES
            )
        }

    # def clean_nic(self, *args, **kwargs):
    #     nic = self.cleaned_data.get("nic")
    #     if len(nic) != 13:
    #         raise forms.ValidationError("NIC must be of 13 digits")
    #     return nic