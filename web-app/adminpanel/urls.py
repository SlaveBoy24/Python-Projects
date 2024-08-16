from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='index'),
    path('showTable/<int:num>', views.showTable, name='showTable'),
    path('updateRecord/<int:num>/<int:pk>', views.updateRecord, name='updateRecord'),
    path('updateStatus/<int:num>/<int:pk>', views.updateStatus, name='updateStatus'),
    path('deleteRecord/<int:num>/<int:pk>', views.deleteRecord, name='deleteRecord')
]