from django.shortcuts import render
from .models import Person

# Create your views here.

def person_list(request):
    person = Person.objects.all()
    context = {'person': person}
    return render(request, 'person_list.html', context)