from django.contrib import admin
from django.http import HttpResponse,HttpResponseRedirect
from models import PrimaryInfo
from models import SoftwareInfo
from models import DnsInfo
from models import AssetInfo
from models import ContactInfo
from models import StorageInfo
from forms import AssetInfoForm
from models import VMInfo
from django.forms import TextInput
from attachments.admin import AttachmentInlines
import json
import reversion
import mysql.connector as mariadb
from django.db import models
from django.core import serializers


def select_product(mmip, bay, product_name):
    mod = __import__(product_name, globals(), locals(),[],-1)
    mod = getattr(mod, "Default")
    product = mod(mmip=mmip, bay=bay)
    return product

class PrimaryInfoAdmin(reversion.VersionAdmin):
    search_fields = ('hostname', 'mm_ip', 'location', 'purpose', 'mac_address', 'manufacturer','serial_number','product_name','annotation', 'status')
    list_display = ('hostname', 'connect_mm', 'bay', 'location', 'purpose', 'mac_address', 'manufacturer','serial_number','annotation', 'status', )
    actions = ('export_csv', 'export_hostname', 'uidon', 'uidoff', 'poweron', 'poweroff', 'powerrestart', 'status', 'repair', )

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'style': 'width:360px'})},
    }

    def repair(modeladmin, request, queryset):
        data = HttpResponse()
        serializers.serialize("json", queryset, stream=data)
        data = serializers.serialize('json', queryset, fields=('model', 'pk', 'mm_ip', "bay", "location", "manufacturer", "serial_number", "product_name"))
        jdata = data.strip("[").strip("]")
        j=json.loads(jdata)
      
        return HttpResponseRedirect("<asgc_url>/?model=%sname=%sip=%sloc=%smf=%spn=%ssn=%sbay=%s" %(j['model'], j['pk'], j['fields']['mm_ip'], j['fields']['location'], j['fields']['manufacturer'],
                                    j['fields']['product_name'], j['fields']['serial_number'], j['fields']['bay']))

    def connect_mm(self, obj):
         return '<a href="http://%s">%s</a>' % (obj.mm_ip, obj.mm_ip)
    connect_mm.allow_tags = True

    def export_csv(modeladmin, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=primary_info.csv'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow([
            smart_str(u"Hostname"),
            smart_str(u"MM_IP"),
            smart_str(u"Bay"),
            smart_str(u"Location"),
            smart_str(u"Purpose"),
            smart_str(u"MAC_Address"),
            smart_str(u"Annotation"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.hostname),
                smart_str(obj.mm_ip),
                smart_str(obj.bay),
                smart_str(obj.location),
                smart_str(obj.purpose),
                smart_str(obj.mac_address),
                smart_str(obj.annotation),
            ])
        return response
    export_csv.short_description = u"Export CSV"

    def export_hostname(modeladmin, request, queryset):
        import csv
        from django.utils.encoding import smart_str
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=hostname.txt'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
        for obj in queryset:
            writer.writerow([
                smart_str(obj.hostname)
            ])
        return response
    export_hostname.short_description = u"Export Hostname"

    def poweron(modeladmin, request, queryset):
        for obj in queryset:
            mmip=obj.mm_ip
            bay=obj.bay
            product_name=obj.mmmod
            product = select_product(mmip=mmip, bay=bay, product_name=product_name)
            product.poweron()

    poweron.short_description = u"POWER_ON"

    def poweroff(modeladmin, request, queryset):
        for obj in queryset:
            mmip=obj.mm_ip
            bay=obj.bay
            product_name=obj.mmmod
            product = select_product(mmip=mmip, bay=bay, product_name=product_name)
            product.poweroff()

    poweroff.short_description = u"POWER_OFF"

    def powerrestart(modeladmin, request, queryset):
        for obj in queryset:
            mmip=obj.mm_ip
            bay=obj.bay
            product_name=obj.mmmod
            product = select_product(mmip=mmip, bay=bay, product_name=product_name)
            product.powerrestart()

    powerrestart.short_description = u"POWER_RESTART"

    def powerstatus(modeladmin, request, queryset):
        db_connection = mariadb.connect(host='as-wn143.euasiagrid.org', user='root', passwd='hellomaria', db='asgc_resource')
        cursor = db_connection.cursor()
        for obj in queryset:
            mmip=obj.mm_ip
            bay=obj.bay
            product_name=obj.mmmod
            product = select_product(mmip=mmip, bay=bay, product_name=product_name)
            status = product.powerstatus()
            cmd = "update primary_info set powerstatus=\'%s\' where hostname=\'%s\'"%(status, obj.hostname)
            cursor.execute(cmd)
        db_connection.commit()
        db_connection.close()
            
    powerstatus.short_description = u"POWER_STATUS"

    def uidon(modeladmin, request, queryset):
        for obj in queryset:
            mmip=obj.mm_ip
            bay=obj.bay
            product_name=obj.mmmod
            product = select_product(mmip=mmip, bay=bay, product_name=product_name)
            product.uidon()

    uidon.short_description = u"UID_ON"
 
    def uidoff(modeladmin, request, queryset):
        for obj in queryset:
            mmip=obj.mm_ip
            bay=obj.bay
            product_name=obj.mmmod
            product = select_product(mmip=mmip, bay=bay, product_name=product_name)
            product.uidoff()

    uidoff.short_description = u"UID_OFF"

admin.site.register(PrimaryInfo, PrimaryInfoAdmin)

class AssetInfoAdmin(reversion.VersionAdmin):
    search_fields = ('asset_number', 'serial_number', 'product_name', 'manufacturer', 'owner', 'user', 'location', 'annotation', 'purchase_date', 'usage_date',)
    list_display = ('object_id', 'asset_number', 'serial_number', 'product_name', 'total_price', 'show_manufacturer', 'owner', 'user', 'location', 'purchase_date', 'usage_date',)

    inlines = [AttachmentInlines]
    form = AssetInfoForm

    def show_manufacturer(self, obj):
         return '<a href="<asgc_url>/%s/">%s</a>' % (obj.manufacturer, obj.manufacturer)
    show_manufacturer.allow_tags = True

admin.site.register(AssetInfo, AssetInfoAdmin)

class ContactInfoAdmin(reversion.VersionAdmin):
    search_fields = ('manufacturer', 'chinese_name', 'english_name', 'mail', 'phone_number', )
    list_display = ('manufacturer', 'chinese_name', 'english_name', 'mail', 'phone_number', )
admin.site.register(ContactInfo, ContactInfoAdmin)

class DnsInfoAdmin(admin.ModelAdmin):
    search_fields = ('ip_address', 'hostname') 
    readonly_fields = ('ip_address', 'hostname')
    list_display = ('ip_address', 'hostname')

admin.site.register(DnsInfo, DnsInfoAdmin)

class StorageInfoAdmin(reversion.VersionAdmin):
    search_fields = ('controller_mm_ip', 'location', 'factory', 'spec', 'storage_port_address', 'disk_server', 'serial_number', 'partition_label', )
    list_display = ('controller_mm_ip', 'location', 'factory', 'spec', 'raw_space_tb_f', 'disk_server', 'serial_number', 'partition_label', )

    actions = ('repair', )

    def raw_space_tb_f(self, obj):
        return obj.raw_space_tb
    raw_space_tb_f.short_description = 'Raw Space(TB)' 

    def repair(modeladmin, request, queryset):
        data = HttpResponse()
        serializers.serialize("json", queryset, stream=data)
        data = serializers.serialize('json', queryset, fields=('model', 'pk', 'disk_server', 'location', 'factory', 'hardware_id', 'serial_number',))
        jdata = data.strip("[").strip("]")
        j=json.loads(jdata)

        return HttpResponseRedirect("<asgc_url>?model=%sname=%sip=%sloc=%smf=%spn=%ssn=%s" %(j['model'], j['fields']['disk_server'], j['pk'], j['fields']['location'], j['fields']['factory'],
                                    j['fields']['hardware_id'], j['fields']['serial_number']))

admin.site.register(StorageInfo, StorageInfoAdmin)

class VMInfoAdmin(admin.ModelAdmin):
    list_display = ('instance_name','hostname','username','show_hypervisor','project_name','image_name','ip_address','tabname','vm_state','annotation')
    readonly_fields = ('instance_name','hostname','vcpus','memory_mb','username','hypervisor','project_name','image_name','ip_address','tabname','vm_state')
    search_fields = ('instance_name','hostname','username','hypervisor','project_name','image_name','ip_address','tabname','vm_state','annotation')
    def show_hypervisor(self,obj):
        return '<a href="<asgc_url>?q=%s">%s</a>' % (obj.hypervisor, obj.hypervisor)
    show_hypervisor.allow_tags = True
admin.site.register(VMInfo, VMInfoAdmin)
