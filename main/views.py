from django.contrib import messages
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import LocationForm, PersonForm, CrimeCategoryForm, CrimeForm, VictimForm, SuspectForm, CrimesCommittedForm
from .models import Location, CrimesCommitted, Victim, Suspect, CrimeCategory, Crime


def create_view_location_person(request):
    template = "create-view-location-person.html"
    location_form = LocationForm(request.POST or None)
    person_form = PersonForm(request.POST or None)
    context = {
        "location_form": location_form,
        "person_form": person_form
    }
    if request.method == "POST":
        location_valid = location_form.is_valid()
        person_valid = person_form.is_valid()
        if location_valid and person_valid:
            location = location_form.save()
            person = person_form.save(commit=False)
            person.location = location
            person.save()
            messages.success(request, "Thanks!")
            return HttpResponseRedirect(
                "http://127.0.0.1:8000/main/detail/{locid}".format(locid=location.location_id))
    return render(request, template, context)


def list_view_location_person(request):
    template = "list-view-location-person.html"
    locations = Location.objects.all()
    context = {
        "locations": locations
    }
    return render(request, template, context)


def detail_view_location_person(request, id=None):
    template = "detail-view-location-person.html"
    location = get_object_or_404(Location, location_id=id)
    context = {
        "location": location
    }
    return render(request, template, context)


def create_view_crime_committed(request):
    template = "create-view-crime-committed.html"
    crime_form = CrimeForm(request.POST or None)
    crime_category_form = CrimeCategoryForm(request.POST or None)
    victim_form = VictimForm(request.POST or None)
    suspect_form = SuspectForm(request.POST or None)
    crimes_committed_form = CrimesCommittedForm(request.POST or None)

    context = {
        "crime_category_form": crime_category_form,
        "crime_form": crime_form,
        "victim_form": victim_form,
        "suspect_form": suspect_form,
        "crime_committed_form": crimes_committed_form
    }
    if request.method == "POST":
        category_valid = crime_category_form.is_valid()
        crime_valid = crime_form.is_valid()
        victim_valid = victim_form.is_valid()
        suspect_valid = suspect_form.is_valid()
        if category_valid and crime_valid and victim_valid and suspect_valid:
            category = crime_category_form.save()
            crime = crime_form.save(commit=False)
            crime.category = category
            crime.save()
            victim = victim_form.save()
            suspect = suspect_form.save()
            crimes_committed = crimes_committed_form.save(commit=False)
            crimes_committed.victim = victim
            crimes_committed.suspect = suspect
            crimes_committed.crime = crime
            crimes_committed.save()
    return render(request, template, context)


def list_view_crime_committed(request):
    template = "list-view-crime-committed.html"
    crimes = CrimesCommitted.objects.all()
    context = {
        "crimes": crimes
    }
    return render(request, template, context)


def list_view_victim(request):
    template = "list-view-victim.html"
    victims = Victim.objects.all()
    context = {
        "victims": victims
    }
    return render(request, template, context)


def list_view_suspect(request):
    template = "list-view-suspect.html"
    suspects = Suspect.objects.all()
    context = {
        "suspects": suspects
    }
    return render(request, template, context)


def list_view_crime_category(request):
    template = "list-view-crime-category.html"
    crime_categories = CrimeCategory.objects.all()
    context = {
        "crime_categories": crime_categories
    }
    return render(request, template, context)


def list_view_crime(request):
    template = "list-view-crime.html"
    crimes = Crime.objects.all()
    context = {
        "crimes": crimes
    }
    return render(request, template, context)

