from django.shortcuts import render, get_object_or_404
from .forms import LocationForm, PersonForm
from .models import Location


def home_view(request):
    template = "home.html"
    location_form = LocationForm(request.POST or None)
    person_form = PersonForm(request.POST or None)
    context = {
        "location_form": location_form,
        "person_form": person_form
    }
    if request.method == "POST":
        a_valid = location_form.is_valid()
        b_valid = person_form.is_valid()
        if a_valid:
            a = location_form.save()
            if b_valid:
                b = person_form.save(commit=False)
                b.location = a
                b.save()
    return render(request, template, context)


def list_view(request):
    template = "list-view.html"
    locations = Location.objects.all()
    context = {
        "locations": locations
    }
    return render(request, template, context)


def detail_view(request, id=None):
    template = "detail-view.html"
    location = get_object_or_404(Location, location_id=id)
    context = {
        "location": location
    }
    return render(request, template, context)