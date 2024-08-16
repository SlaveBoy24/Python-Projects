from django.db import models
from app.models import Level, Words
import random

def GenerateString(level = None):
    if level == None:
        return ''

    words = Words.objects.filter(level_id = level).values_list('word', flat=True)
    arr = []
    for i in range(100):
        arr.append(words[random.randrange(len(words))])

    result = ' '.join(arr)
    return result
        