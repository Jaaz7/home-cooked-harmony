from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home_cooked_harmony/index.html')