from .models import SystemParameter
from django import forms

class NameForm(forms.Form):
    
     HostName = forms.CharField(label='HostName', max_length=50)
     SoftwareName = forms.CharField(label='SoftwareName', max_length=50)

class SystemParameterForm(forms.Form):

     HostName = forms.CharField(label='Hostname', max_length=20)
     ParameterName = forms.CharField(label='ParameterName', max_length=50)  
     ParameterValue = forms.CharField(label='ParameterValue', max_length=80)


from .models import AssetInfo, ContactInfo

class AssetInfoForm(forms.ModelForm):

    class Meta:
        model = AssetInfo
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(AssetInfoForm, self).__init__(*args, **kwargs)

        query = ContactInfo.objects.all()
        manufacturer_list = []
        for items in query:
            manufacturer_list.append((items.manufacturer, items.manufacturer))
        self.fields['manufacturer'] = forms.ChoiceField(choices=manufacturer_list)

