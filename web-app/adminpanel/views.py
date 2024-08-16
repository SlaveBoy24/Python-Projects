import math
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import models
from .forms import *
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.

def mainPage(request):
    return render(request, 'adminpanel/index.html', {})

@requires_csrf_token
def showTable(request, num, bool = False):
    page = 1
    if (request.method == 'POST' and bool == False):
        page = int(request.POST.get('page_num'))
    else:
        page = 1
             
    i = 10 * (page-1)
    k = 10 * page
    
    model = getModel(num)
    if (model == None):
        return render(request, 'adminpanel/index.html')
    
    print((model.__name__ + 'Table.html'))
    objects = model.objects.all()

    if (objects.count() == 0):
           maxPages = 1
    else:
        if ((objects.count()/10).is_integer() == False):
            maxPages = math.floor(objects.count()/10 + 1)
        else:
            maxPages = math.floor(objects.count()/10)

    objects = model.objects.all()[i:k]

    return render(request, 'adminpanel/' + (model.__name__ + 'Table.html'), {'data': objects,
                                                             'numPage': page,
                                                             'maxPages': maxPages})

@requires_csrf_token
def updateRecord(request, num, pk):
    model = getModel(num)
    print ('HERE HERE HERE')
    if (model == None):
        return render(request, 'adminpanel/index.html')
    
    form = getUpdateForm(pk, num)

    return render(request, 'adminpanel/EntryUpdate.html', {"form": form, 
                                                            "num_val": num,
                                                            "pk_id": pk})

@requires_csrf_token
def updateStatus(request, num, pk):
    arr_vals = []
    for key, value in request.POST.items():
        if (key != 'csrfmiddlewaretoken'):
            arr_vals.append(value)

    print(arr_vals)
    model = getModel(num)
    if (pk == 0):
        model.insertData(model, arr_vals)
    else:
        model.updateRecord(model, pk, arr_vals)
    status = 'Успешно!'
    return render(request, 'adminpanel/UpdateStatus.html', {'status': status})

def deleteRecord(request, num, pk):
    model = getModel(num)
    model.objects.get(id=pk).delete()
    status = 'Успешно!'
    return render(request, 'adminpanel/UpdateStatus.html', {'status': status})