from django.http import HttpResponse
from django.shortcuts import render

from matrimony.forms import MatrimonyApplicationForm
from matrimony.models import MatrimonyApplication


def index(request):
    form = MatrimonyApplicationForm()

    return render(request, 'index.html', {'form': form})


def save_application(request):
    form = MatrimonyApplicationForm(request.POST)
    ma = MatrimonyApplication(
        name=form.data['name'],
        place=form.data['place'],
        origin=form.data['origin'],
        gothram=form.data['gothram'],
        family_name=form.data['family_name'],
    )
    ma.save()
    return HttpResponse("Application Saved")