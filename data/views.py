from django.shortcuts import render
from . models import Club
# Create your views here.
def clubs(request):
  clubs = Club.objects.all()
  context = {
    "clubs": clubs
  }
  return render(request, "clubs.html", context)