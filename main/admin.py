from django.contrib import admin
from .models import Location, Victim, Suspect, CrimeCategory, CrimesCommitted, Crime
from .forms import LocationForm


# Register your models here.
class Loc(admin.ModelAdmin):
    list_display = ['location_id', 'state', 'city']
    form = LocationForm


admin.site.register(Location, Loc)
admin.site.register(Victim)
admin.site.register(Suspect)
admin.site.register(CrimeCategory)
admin.site.register(CrimesCommitted)
admin.site.register(Crime)
