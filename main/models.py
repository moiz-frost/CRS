from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models

PROFESSION_CHOICES = (

)

GENDER_CHOICES = [
    ('Male'       , 'Male'),
    ('Female'     , 'Female'),
    ('Unspecified', 'Cannot Specify')
]

CAST_CHOICES = [
    ('Punjabi'    ,   'Punjabi'),
    ('Pashtun'    ,   'Pashtun'),
    ('Sindhi'     ,   'Sindhi'),
    ('Seraiki'    ,   'Seraiki'),
    ('Muhajir'    ,   'Muhajir'),
    ('Baloch'     ,   'Baloch'),
    ('Unspecified',   'Others'),
]

COMPLEXION_CHOICES = [
    ('Fair'         ,   'Fair'),
    ('Wheatish'     ,   'Wheatish'),
    ('Dark'         ,   'Dark'),
]

STATE_CHOICES = (
    ('Sindh'                , 'Sindh'),
    ('Punjab'               , 'Punjab'),
    ('Gilgit'               , 'Gilgit'),
    ('Baltistan'            , 'Baltistan'),
    ('Jammu and Kashmir'    , 'Jammu and Kashmir'),
    ('FATA'                 , 'FATA')
)

CITY_CHOICES = (
    ('Karachi'      , 'Karachi'),
    ('Islamabad'    , 'Islamabad')
)

PHYSIQUE_CHOICES = (
    ('Assault','Assault'),
    ('False Imprisonment', 'False Imprisonment'),
    ('Kidnapping', 'Kidnapping'),
    ('Homicide', 'Homicide'),
    ('Murder', 'Murder'),
    ('Vehicular Homicide', 'Vehicular Homicide'),
    ('Rape', 'Rape')
)

CRIME_CATEGORIES_CHOICES = (

)

THREAT_LEVELS_CHOICES = [
    ('High', 'High')
    ('Medium', 'Medium')
    ('Low', 'Low')
]

PENALTIES_CHOICES = [
    ('Death', 'Death')
]

class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    address = models.TextField(max_length=200, blank=True)
    zip_code = models.CharField(max_length=5,
                                validators=[RegexValidator(r'^\d{5}$', message="Invalid zip code")])
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.location_id)


class Person(models.Model):
    nic = models.CharField(primary_key=True, max_length=13,
                           validators=[RegexValidator(r'^\d{13}$', message="Must be 13 digits")])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=17,
                             validators=[RegexValidator(r'^\d{11,14}$', message="Invalid Phone Number")])
    profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES)
    gender = models.CharField(max_length=20)
    location = models.OneToOneField(Location, null=False, default=None, blank=True)

    def __str__(self):
        return str(self.nic)


class User(models.Model):
    user_name = models.CharField(max_length=200, primary_key=True, unique=True)
    password = models.CharField(max_length=200)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, blank=False, null=False, default=None)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user_name


class Victim(models.Model):
    victim_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True)
    cast = models.CharField(max_length=50, choices=CAST_CHOICES)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    complexion = models.CharField(max_length=10, choices=COMPLEXION_CHOICES)
    profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES)


class Suspect(models.Model):
    suspect_id = models.AutoField(primary_key=True)
    physique = models.CharField(max_length=50, choices=PHYSIQUE_CHOICES)
    complexion = models.CharField(max_length=10, choices=COMPLEXION_CHOICES)
    cast = models.CharField(max_length=50, choices=CAST_CHOICES)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)


class CrimeCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=CRIME_CATEGORIES_CHOICES)
    threat_level = models.CharField(max_length=50, choices=THREAT_LEVELS_CHOICES, default='High')
    penalty = models.CharField(max_length=50, choices=PENALTIES_CHOICES, default='Death')


class Crime(models.Model):
    crime_id = models.IntegerField(primary_key=True)
    details = models.TextField(max_length=500)
    category = models.ForeignKey(CrimeCategory)


class CrimesCommitted(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True)
    victim = models.ForeignKey(Victim)
    crime = models.ForeignKey(Crime)
    suspect = models.ForeignKey(Suspect)
