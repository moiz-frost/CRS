from django.shortcuts import render
from .forms import LocationForm, PersonForm


def home(request):
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
    return render(request, "home.html", context)
