from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse
import logging
#import messages
from django.contrib import messages
from django.views.generic import TemplateView
import operator


from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

def index(request):
    # return the Main site page
    return render(request, 'index.html')

