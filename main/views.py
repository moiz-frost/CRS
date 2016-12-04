from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import LocationForm, CrimeCategoryForm, CrimeForm, VictimForm, SuspectForm, CrimesCommittedForm
from .models import Location, CrimesCommitted, Victim, Suspect, CrimeCategory, Crime


# Create Views
def create_view_crime_committed(request):
    template = "create-view-crime-committed.html"
    crime_form = CrimeForm(request.POST or None)
    crime_category_form = CrimeCategoryForm(request.POST or None)
    victim_form = VictimForm(request.POST or None)
    suspect_form = SuspectForm(request.POST or None)
    location_form = LocationForm(request.POST or None)
    crimes_committed_form = CrimesCommittedForm(request.POST or None)
    context = {
        "crime_category_form": crime_category_form,
        "crime_form": crime_form,
        "victim_form": victim_form,
        "suspect_form": suspect_form,
        "crime_committed_form": crimes_committed_form,
        "location_form": location_form
    }
    if request.method == "POST":
        category_valid = crime_category_form.is_valid()
        crime_valid = crime_form.is_valid()
        victim_valid = victim_form.is_valid()
        suspect_valid = suspect_form.is_valid()
        location_valid = location_form.is_valid()
        if category_valid and crime_valid and victim_valid and suspect_valid and location_valid:
            location = location_form.save()
            category = crime_category_form.save()
            victim = victim_form.save()
            crime = crime_form.save(commit=False)
            crime.category = category
            crime.save()
            suspect = suspect_form.save()
            crimes_committed = crimes_committed_form.save(commit=False)
            crimes_committed.location = location
            crimes_committed.victim = victim
            crimes_committed.crime = crime
            crimes_committed.suspect = suspect
            crimes_committed.save()
    return render(request, template, context)


# List Views
def list_view_location(request):
    template = "list-view-location.html"
    locations = Location.objects.all()
    context = {
        "locations": locations
    }
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


# Detail Views
def detail_view_location(request, id=None):
    template = "detail-view-location.html"
    location = get_object_or_404(Location, location_id=id)
    context = {
        "location": location
    }
    return render(request, template, context)


def detail_view_victim(request, id=None):
    template = "detail-view-victim.html"
    victim = get_object_or_404(Victim, victim_id=id)
    context = {
        "victim": victim
    }
    return render(request, template, context)


def detail_view_suspect(request, id=None):
    template = "detail-view-suspect.html"
    suspect = get_object_or_404(Suspect, suspect_id=id)
    context = {
        "suspect": suspect
    }
    return render(request, template, context)


def detail_view_crime(request, id=None):
    template = "detail-view-crime.html"
    crime = get_object_or_404(Crime, crime_id=id)
    context = {
        "crime": crime
    }
    return render(request, template, context)


def detail_view_crime_category(request, id=None):
    template = "detail-view-crime-category.html"
    category = get_object_or_404(CrimeCategory, category_id=id)
    context = {
        "category": category
    }
    return render(request, template, context)


# Update Views
def update_view_location(request, id=None):
    template = "update-view-location.html"
    obj = get_object_or_404(Location, location_id=id)
    location_form = LocationForm(request.POST or None, instance=obj)
    context = {
        "location_form": location_form
    }
    if request.method == "POST" and location_form.is_valid():
        obj = location_form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/main/location-list/details/{id}".format(id=id))
    return render(request, template, context)


def update_view_crime(request, id=None):
    template = "update-view-crime.html"
    obj = get_object_or_404(Crime, crime_id=id)
    crime_form = CrimeForm(request.POST or None, instance=obj)
    context = {
        "crime_form": crime_form
    }
    if request.method == "POST" and crime_form.is_valid():
        obj = crime_form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/main/crime-list/details/{id}".format(id=id))
    return render(request, template, context)


def update_view_crime_category(request, id=None):
    template = "update-view-crime-category.html"
    obj = get_object_or_404(CrimeCategory, category_id=id)
    category_form = CrimeCategoryForm(request.POST or None, instance=obj)
    context = {
        "category_form": category_form
    }
    if request.method == "POST" and category_form.is_valid():
        obj = category_form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/main/crime-category-list/details/{id}".format(id=id))
    return render(request, template, context)


def update_view_victim(request, id=None):
    template = "update-view-victim.html"
    obj = get_object_or_404(Victim, victim_id=id)
    victim_form = VictimForm(request.POST or None, instance=obj)
    context = {
        "victim_form": victim_form
    }
    if request.method == "POST" and victim_form.is_valid():
        obj = victim_form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/main/victim-list/details/{id}".format(id=id))
    return render(request, template, context)


def update_view_suspect(request, id=None):
    template = "update-view-suspect.html"
    obj = get_object_or_404(Suspect, suspect_id=id)
    suspect_form = SuspectForm(request.POST or None, instance=obj)
    context = {
        "suspect_form": suspect_form
    }
    if request.method == "POST" and suspect_form.is_valid():
        obj = suspect_form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/main/suspect-list/details/{id}".format(id=id))
    return render(request, template, context)
