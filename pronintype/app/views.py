from django.shortcuts import render
from . import models
from . import logic
# Create your views here.

def main(request, level = None):
    if (level == None):
        level = models.Level.objects.first()
    else:
        level = models.Level.objects.get(pk=level)

    generatedString = logic.GenerateString(level)

    return render(request, "index.html", {'quest': generatedString})