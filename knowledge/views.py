from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def view_title(request):
    template = loader.get_template("title.html") 
    return HttpResponse(template.render())  
