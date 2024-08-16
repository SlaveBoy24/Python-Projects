from django import forms
from .models import *

def createChoices(objects):
        dict = {"0": "Выберите значение"}

        for obj in objects:
            dict[str(obj.id)] = obj.getSelectName()
        return dict

def getUpdateForm(pk, num):
    if num==1:
        return UpdateTypeRecord(pk)
    elif num==2:
        return UpdateDeviceRecord(pk)
    elif num==3:
        return UpdateOfficeRecord(pk)
    elif num==4:
        return UpdateClientRoleRecord(pk)
    elif num==5:
        return UpdateClientRecord(pk)
    elif num==6:
        return UpdateEntryRecord(pk)
    else:
        return None

class UpdateTypeRecord(forms.Form):
    def __init__(self, pk_id, *args, **kwargs):
         super().__init__(*args, **kwargs)
         init_val = None
         if (pk_id != 0):
            obj = Type.objects.get(pk=pk_id)
            init_val = obj.name
         self.fields['type_name_field'] = forms.CharField(initial=init_val)
    
    type_name_field = forms.CharField()

class UpdateDeviceRecord(forms.Form):
    def __init__(self, pk_id, *args, **kwargs):
         super().__init__(*args, **kwargs)
         init_val = None
         if (pk_id != 0):
            obj = Device.objects.get(pk=pk_id)
            init_val = obj.name
         self.fields['device_name_field'] = forms.CharField(initial=init_val)
         type_choices = createChoices(Type.objects.all())
         if (pk_id != 0):
             init_val = obj.type_id.id
         self.fields['type_choice_field'] = forms.ChoiceField(widget=forms.Select, choices=type_choices.items(), initial=init_val)
         office_choices = createChoices(Office.objects.all())
         if (pk_id != 0):
             init_val = obj.office_id.id
         self.fields['office_choice_field'] = forms.ChoiceField(widget=forms.Select, choices=office_choices.items(), initial=init_val)
    
    device_name_field = forms.CharField()
    type_choice_field = forms.ChoiceField()
    office_choice_field = forms.ChoiceField()

class UpdateOfficeRecord(forms.Form):
    def __init__(self, pk_id, *args, **kwargs):
         super().__init__(*args, **kwargs)
         init_val = None
         if (pk_id != 0):
            obj = Office.objects.get(pk=pk_id)
            init_val = obj.adress
         self.fields['office_adress_field'] = forms.CharField(initial=init_val)
    
    office_adress_field = forms.CharField()

class UpdateClientRoleRecord(forms.Form):
    def __init__(self, pk_id, *args, **kwargs):
         super().__init__(*args, **kwargs)
         init_val = None
         if (pk_id != 0):
            obj = ClientRole.objects.get(pk=pk_id)
            init_val = obj.name
         self.fields['client_role_name_field'] = forms.CharField(initial=init_val)
    
    client_role_name_field = forms.CharField()

class UpdateClientRecord(forms.Form):
    def __init__(self, pk_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        init_val = None
        if (pk_id != 0):
            obj = Client.objects.get(pk=pk_id)
            init_val = obj.full_name
        self.fields['full_name_field'] = forms.CharField(initial=init_val)
        client_roles_choices = createChoices(ClientRole.objects.all())
        if (pk_id != 0):
             init_val = obj.client_role_id.id
        self.fields['client_role_choice_field'] = forms.ChoiceField(widget=forms.Select, choices=client_roles_choices.items(), initial=init_val)
        if (pk_id != 0):
             init_val = obj.adress
        self.fields['adress_field'] = forms.CharField(initial=init_val)
        if (pk_id != 0):
             init_val = obj.passport
        self.fields['passpord_field'] = forms.CharField(initial=init_val)
    
    full_name_field = forms.CharField()
    client_role_choice_field = forms.ChoiceField()
    adress_field = forms.CharField()
    passpord_field = forms.CharField()

class UpdateEntryRecord(forms.Form):
    def __init__(self, pk_id, *args, **kwargs):
         super().__init__(*args, **kwargs)
         init_val = None
         if (pk_id != 0):
            obj = Entry.objects.get(pk=pk_id)
            init_val = obj.device_id.id
         device_choices = createChoices(Device.objects.all())
         self.fields['device_choice_field'] = forms.ChoiceField(widget=forms.Select, choices=device_choices.items(), initial=init_val)
         client_choices = createChoices(Client.objects.all())
         if (pk_id != 0):
             init_val = obj.client_id.id
         self.fields['client_choice_field'] = forms.ChoiceField(widget=forms.Select, choices=client_choices.items(), initial=init_val)
         office_choices = createChoices(Office.objects.all())
         if (pk_id != 0):
             init_val = obj.office_id.id
         self.fields['office_choice_field'] = forms.ChoiceField(widget=forms.Select, choices=office_choices.items(), initial=init_val)
    
    device_choice_field = forms.ChoiceField()
    client_choice_field = forms.ChoiceField()
    office_choice_field = forms.ChoiceField()



    
    
