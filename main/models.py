from django.core.validators import RegexValidator
from django.db import models

PROFESSION_CHOICES = [
    ('Terrorist', 'Terrorist')
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unspecified', 'Cannot Specify')
]

CAST_CHOICES = [
    ('Punjabi', 'Punjabi'),
    ('Pashtun', 'Pashtun'),
    ('Sindhi', 'Sindhi'),
    ('Seraiki', 'Seraiki'),
    ('Muhajir', 'Muhajir'),
    ('Baloch', 'Baloch'),
    ('Unspecified', 'Others'),
]

COMPLEXION_CHOICES = [
    ('Fair', 'Fair'),
    ('Wheatish', 'Wheatish'),
    ('Dark', 'Dark'),
]

STATE_CHOICES = (
    ('Sindh', 'Sindh'),
    ('Punjab', 'Punjab'),
    ('Gilgit', 'Gilgit'),
    ('Baltistan', 'Baltistan'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('FATA', 'FATA')
)

CITY_CHOICES = (
    ('Karachi', 'Karachi'),
    ('Islamabad', 'Islamabad')
)

CRIME_CATEGORIES_CHOICES = (
    ('Assault', 'Assault'),
    ('False Imprisonment', 'False Imprisonment'),
    ('Kidnapping', 'Kidnapping'),
    ('Homicide', 'Homicide'),
    ('Murder', 'Murder'),
    ('Vehicular Homicide', 'Vehicular Homicide'),
    ('Rape', 'Rape')
)

PHYSIQUE_CHOICES = [
    ('Ectomorph', 'Ectomorph'),
    ('Mesomorph', 'Mesomorph'),
    ('Endomorph', 'Endomorph')
]

THREAT_LEVELS_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]

PENALTIES_CHOICES = [
    ('Death', 'Death')
]


class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    address = models.TextField(max_length=200, blank=True)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.location_id)


# class Person(models.Model):
#     nic = models.CharField(primary_key=True, max_length=13,
#                            validators=[RegexValidator(r'^\d{13}$', message="Must be 13 digits")])
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     phone = models.CharField(max_length=17,
#                              validators=[RegexValidator(r'^\d{11,14}$', message="Invalid Phone Number")])
#     profession = models.CharField(max_length=50)
#     gender = models.CharField(max_length=20)
#     location = models.OneToOneField(Location, null=False, blank=False)
#
#     def __str__(self):
#         return str(self.nic)


# class User(models.Model):
#     user_name = models.CharField(max_length=200, primary_key=True, unique=True)
#     password = models.CharField(max_length=200)
#     person = models.OneToOneField(Person, on_delete=models.CASCADE, blank=False, null=False, default=None)
#     created = models.DateTimeField(default=datetime.now, blank=True)
#
#     def __str__(self):
#         return str(self.user_name)


class Victim(models.Model):
    victim_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True)
    cast = models.CharField(max_length=50)
    age = models.CharField(max_length=5, blank=True,
                           validators=[RegexValidator(r'^\d{1,3}$', message="Invalid Age")])
    gender = models.CharField(max_length=30)
    complexion = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)

    def __str__(self):
        return str(self.victim_id)


class Suspect(models.Model):
    suspect_id = models.BigAutoField(primary_key=True)
    physique = models.CharField(max_length=50)
    complexion = models.CharField(max_length=20)
    cast = models.CharField(max_length=50)
    age = models.CharField(max_length=5, blank=True,
                           validators=[RegexValidator(r'^\d{1,3}$', message="Invalid Age")])
    gender = models.CharField(max_length=10)

    def __str__(self):
        return str(self.suspect_id)


class CrimeCategory(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=25)
    threat_level = models.CharField(max_length=25)
    penalty = models.CharField(max_length=25)

    def __str__(self):
        return str(self.category_id)


class Crime(models.Model):
    crime_id = models.BigAutoField(primary_key=True)
    details = models.TextField(max_length=1500)
    category = models.ForeignKey(CrimeCategory, null=False, blank=False)

    def __str__(self):
        return str(self.crime_id)


class CrimesCommitted(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.ForeignKey(Location, null=False)
    victim = models.ForeignKey(Victim, null=False)
    crime = models.ForeignKey(Crime, null=False)
    suspect = models.ForeignKey(Suspect, null=False)
    date = models.DateField()

    def __str__(self):
        return str(self.id)
