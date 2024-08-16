from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)

    def getSelectName(self):
        return self.name
    
    def updateRecord(self, pk_id, arr_of_vals):
        o = self.objects.get(pk=pk_id)
        o.name = arr_of_vals[0]
        o.save()

    def insertData(self, arr_of_vals):
        o = Type(name=arr_of_vals[0])
        o.save()

class Office(models.Model):
    adress = models.CharField(max_length=200)

    def getSelectName(self):
        return self.adress
    
    def updateRecord(self, pk_id, arr_of_vals):
        o = self.objects.get(pk=pk_id)
        o.adress = arr_of_vals[0]
        o.save()

    def insertData(self, arr_of_vals):
        o = Office(adress=arr_of_vals[0])
        o.save()

class Device(models.Model):
    name = models.CharField(max_length=100)
    type_id = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    office_id = models.ForeignKey(Office, on_delete=models.DO_NOTHING)
    state = models.BooleanField()

    def getSelectName(self):
        return self.name

    def updateState(self, value):
        self.state = value

    def updateRecord(self, pk_id, arr_of_vals):
        o = self.objects.get(pk=pk_id)
        o.name = arr_of_vals[0]
        o.type_id = Type.objects.get(pk=arr_of_vals[1])
        o.office_id = Office.objects.get(pk=arr_of_vals[2])
        o.save()

    def insertData(self, arr_of_vals):
        o = Device(name=arr_of_vals[0], type_id=Type.objects.get(pk=arr_of_vals[1]), 
                    office_id=Office.objects.get(pk=arr_of_vals[2]), state=False)
        o.save()

class ClientRole(models.Model):
    name = models.CharField(max_length=50)

    def getSelectName(self):
        return self.name
    
    def updateRecord(self, pk_id, arr_of_vals):
        o = self.objects.get(pk=pk_id)
        o.name = arr_of_vals[0]
        o.save()

    def insertData(self, arr_of_vals):
        o = ClientRole(name=arr_of_vals[0])
        o.save()

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    client_role_id = models.ForeignKey(ClientRole, on_delete=models.DO_NOTHING)
    adress = models.CharField(max_length=200)
    passport = models.CharField(max_length=11)

    def getSelectName(self):
        return self.full_name
    
    def updateRecord(self, pk_id, arr_of_vals):
        o = self.objects.get(pk=pk_id)
        o.full_name = arr_of_vals[0]
        o.client_role_id = ClientRole.objects.get(pk=arr_of_vals[1])
        o.adress = arr_of_vals[2]
        o.passport = arr_of_vals[3]
        o.save()

    def insertData(self, arr_of_vals):
        o = Client(full_name=arr_of_vals[0], client_role_id=ClientRole.objects.get(pk=arr_of_vals[1]), 
                    adress=arr_of_vals[2], passport=arr_of_vals[3])
        o.save()

class Entry(models.Model):
    device_id = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    office_id = models.ForeignKey(Office, on_delete=models.DO_NOTHING)
    create_date = models.DateField(default=timezone.now)
    close_date = models.DateField(null=True, blank=True)

    def create(self):
        self.create_date = timezone.now()
        self.save()
        Device.objects.get(id = self.device_id).updateState(True)

    def close(self):
        self.close_date = timezone.now()
        self.save()
        Device.objects.get(id = self.device_id).updateState(False)

    def updateRecord(self, pk_id, arr_of_vals):
        o = self.objects.get(pk=pk_id)
        o.device_id = Device.objects.get(pk=arr_of_vals[0])
        o.client_id = Client.objects.get(pk=arr_of_vals[1])
        o.office_id = Office.objects.get(pk=arr_of_vals[2])
        o.save()

    def insertData(self, arr_of_vals):
        o = Entry(device_id=Device.objects.get(pk=arr_of_vals[0]), 
                  client_id=Client.objects.get(pk=arr_of_vals[1]), 
                  office_id=Office.objects.get(pk=arr_of_vals[2]))
        o.save()

# other functions

def getModel(num):
    if num==1:
        return Type
    elif num==2:
        return Device
    elif num==3:
        return Office
    elif num==4:
        return ClientRole
    elif num==5:
        return Client
    elif num==6:
        return Entry
    else:
        return None