from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django_tables2  import RequestConfig
from .forms import NameForm,SystemParameterForm
from asgc_resource.models import AssetInfo,PrimaryInfo,SoftwareInfo,SystemParameter
from asgc_resource.tables import AssetInfoTable,PrimaryInfoTable,SoftwareInfoTable
from asgc_resource.tables import SystemParameterTable,ColumnsSystemParameterTable
from asgc_resource.tables import ColumnsSoftwareInfoTable
from asgc_resource.serializers import PrimaryInfoSerializer
from haystack.generic_views import SearchView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""My custom search view."""
class MySearchView(SearchView):
      def index(request):
          queryset = super(MySearchView,self).get_queryset()
        
          paginator = Paginator(queryset, 5) # Show 25 contacts per page
        
          page = request.GET.get('page')
          try:
              cs = paginator.page(page)
          except PageNotAnInteger:
              # If page is not an integer, deliver first page.
              cs = paginator.page(1)
          except EmptyPage:
              # If page is out of range (e.g. 9999), deliver last page of results.
              cs = paginator.page(paginator.num_pages)
          return render(request, 'search/index.html', {'cs': cs})

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET','POST',])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
def primaryinfo_list(request):
    """
    List and Add all information if primary_info
    """

    if request.method == 'GET':
        primary_info = PrimaryInfo.objects.all()
        serializer = PrimaryInfoSerializer(primary_info, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrimaryInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE',])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
def primaryinfo_list_detail(request,hostname):
    """
    Retrieve, update or delete primary_info table
    """
    try:
        primary_info = PrimaryInfo.objects.get(hostname=hostname)
    except PrimaryInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PrimaryInfoSerializer(primary_info)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PrimaryInfoSerializer(primary_info,data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        primary_info.delete()
        return HttpResponse(status=204)

def get_software_info(request):

    if request.method == 'GET':
        form = NameForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            get_hostname = cd['HostName']
            get_softwarename = cd['SoftwareName']

            if get_softwarename == ' ':
                filters = {"hostname":"%s"%(get_hostname)}
            elif get_hostname == ' ':
                filters = {"softwarename__contains":"%s"%(get_softwarename)}
            else:
                filters = {"hostname":"%s"%(get_hostname),"softwarename__contains":"%s"%(get_softwarename)}
            matches = SoftwareInfo.objects.filter(**filters)
            table = SoftwareInfoTable(matches)

            RequestConfig(request, paginate={"per_page": 100}).configure(table)

            return render(request, 'name.html', {'form': form, 'table': table})
    get_softwareinfo = SoftwareInfo._meta.get_all_field_names()
    data = []
    for idx in range(len(get_softwareinfo)):
        data.append({ 'SoftwareInfo':get_softwareinfo[idx], })


    table = ColumnsSoftwareInfoTable(data)
    form = NameForm()
    return render(request, 'name.html', {'form': form, 'table': table})

def get_system_parameter(request):

    if request.method == 'GET':
        form = SystemParameterForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            get_hostname = cd['HostName']
            get_parametername = cd['ParameterName']
            get_parametervalue = cd['ParameterValue']

            if get_parametername == ' ' and get_parametervalue == ' ':
                filters = {"hostname__contains":"%s"%(get_hostname)}
            elif get_hostname == ' ' and get_parametervalue == ' ':
                filters = {"parametername__contains":"%s"%(get_parametername)}
            elif get_hostname == ' ' and get_parametername == ' ':
                filters = {"parametervalue":"%s"%(get_parametervalue)}
            elif get_parametervalue == ' ':
                filters = {"hostname__contains":"%s"%(get_hostname),"parametername__contains":"%s"%(get_parametername)}
            elif get_parametername == ' ':
                filters = {"hostname__contains":"%s"%(get_hostname),"parametervalue":"%s"%(get_parametervalue)}
            elif get_hostname == ' ':
                filters = {"parametername__contains":"%s"%(get_parametername),"parametervalue":"%s"%(get_parametervalue)}
            else:
                filters = {"hostname__contains":"%s"%(get_hostname),"parametername__contains":"%s"%(get_parametername),"parametervalue":"%s"%(get_parametervalue)}

            matches = SystemParameter.objects.filter(**filters)
            table = SystemParameterTable(matches)

            RequestConfig(request, paginate={"per_page": 100}).configure(table)

            return render(request, 'systemparameter.html', {'form': form, 'table': table})
    get_system_parameter = SystemParameter._meta.get_all_field_names()
    data = []
    for idx in range(len(get_system_parameter)):
        data.append({ 'SystemParameter':get_system_parameter[idx], })


    table = ColumnsSystemParameterTable(data)
    form = SystemParameterForm()
    return render(request, 'systemparameter.html', {'form': form, 'table':table})

