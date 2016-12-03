import re
from django import forms
from .models import Location, Crime, CrimeCategory, Victim, Suspect, CrimesCommitted, STATE_CHOICES, GENDER_CHOICES, \
    CRIME_CATEGORIES_CHOICES, THREAT_LEVELS_CHOICES, PENALTIES_CHOICES, CAST_CHOICES, COMPLEXION_CHOICES, \
    PROFESSION_CHOICES, PHYSIQUE_CHOICES


class DateInput(forms.DateInput):
    input_type = 'date'


class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['crime_id',
                  'details',
                  ]
        widgets = {
            'details': forms.Textarea(
                attrs={
                    'placeholder': 'A full description of the scenario',
                    'rows': 6,
                    'cols': 70
                }
            ),
        }


class CrimeCategoryForm(forms.ModelForm):
    class Meta:
        model = CrimeCategory
        fields = ['category_id',
                  'category',
                  'threat_level',
                  'penalty'
                  ]
        widgets = {
            'category': forms.Select(
                choices=CRIME_CATEGORIES_CHOICES
            ),
            'threat_level': forms.Select(
                choices=THREAT_LEVELS_CHOICES
            ),
            'penalty': forms.Select(
                choices=PENALTIES_CHOICES
            )
        }


class VictimForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = ['victim_id',
                  'name',
                  'cast',
                  'age',
                  'gender',
                  'complexion',
                  'profession']
        widgets = {
            'cast': forms.Select(
                choices=CAST_CHOICES
            ),
            'gender': forms.Select(
                choices=GENDER_CHOICES
            ),
            'complexion': forms.Select(
                choices=COMPLEXION_CHOICES
            ),
            'profession': forms.Select(
                choices=PROFESSION_CHOICES
            )
        }

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if not re.search('[a-zA-Z]', name):
            raise forms.ValidationError("Invalid Name")
        return name


class CrimesCommittedForm(forms.ModelForm):
    class Meta:
        model = CrimesCommitted
        fields = ['id',
                  'date']
        widgets = {
            'date': DateInput()
        }


class SuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = ['suspect_id',
                  'physique',
                  'cast',
                  'age',
                  'gender',
                  'complexion']
        widgets = {
            'cast': forms.Select(
                choices=CAST_CHOICES
            ),
            'gender': forms.Select(
                choices=GENDER_CHOICES
            ),
            'complexion': forms.Select(
                choices=COMPLEXION_CHOICES
            ),
            'physique': forms.Select(
                choices=PHYSIQUE_CHOICES
            )
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_id',
                  'address',
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
            )
        }
        labels = {
            'address': 'Address'
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields["address"].initial = ""


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ['nic',
#                   'first_name',
#                   'last_name',
#                   'date_of_birth',
#                   'phone',
#                   'profession',
#                   'gender']
#
#         labels = {
#             'nic': 'NIC'
#         }
#
#         widgets = {
#             'date_of_birth': DateInput(),
#             'gender': forms.Select(
#                 choices=GENDER_CHOICES
#             )
#         }
#
#         # def clean_nic(self, *args, **kwargs):
#         #     nic = self.cleaned_data.get("nic")
#         #     if len(nic) != 13:
#         #         raise forms.ValidationError("NIC must be of 13 digits")
#         #     return nic
