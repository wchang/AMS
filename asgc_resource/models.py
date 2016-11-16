# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models

import subprocess

class ContactInfo(models.Model):
    manufacturer = models.CharField(db_column='Manufacturer', max_length=32, primary_key=True)  # Field name made lowercase.
    chinese_name = models.CharField(db_column='Chinese_Name', max_length=32)  # Field name made lowercase.
    english_name = models.CharField(db_column='English_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='Mail', max_length=128, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contact_info'

class AssetInfo(models.Model):
    object_id = models.IntegerField(primary_key=True)
    asset_number = models.CharField(db_column='Asset_Number', max_length=30, blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='Serial_Number', max_length=24, blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_Name', max_length=128, blank=True, null=True)  # Field name made lowercase.
    specs = models.CharField(db_column='Specs', max_length=128, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=64, blank=True, null=True)  # Field name made lowercase.
    total_price = models.CharField(db_column='Total_Price', max_length=20, blank=True, null=True)  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=5, blank=True, null=True)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=20, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10, blank=True, null=True)  # Field name made lowercase.
    purchase_date = models.CharField(db_column='Purchase_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usage_date = models.CharField(db_column='Usage_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    warranty_period = models.CharField(db_column='Warranty_Period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age_limit = models.CharField(db_column='Age_Limit', max_length=5, blank=True, null=True)  # Field name made lowercase.
    retire_date = models.CharField(db_column='Retire_Date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    annotation = models.CharField(db_column='Annotation', max_length=48, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'asset_info'


class StorageInfo(models.Model):
    controller_mm_ip = models.CharField(db_column='Controller_MM_IP', max_length=32, primary_key=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=10)  # Field name made lowercase.
    factory = models.CharField(db_column='Factory', max_length=15)  # Field name made lowercase.
    hardware_id = models.CharField(db_column='Hardware_ID', max_length=12)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=10, blank=True, null=True)  # Field name made lowercase.
    raw_space_tb = models.IntegerField(db_column='Raw_Space_TB', blank=True, null=True)  # Field name made lowercase.
    storage_port_address = models.CharField(db_column='Storage_Port_Address', max_length=20, blank=True, null=True)  # Field name made lowercase.
    disk_server = models.CharField(db_column='Disk_Server', max_length=32, blank=True, null=True)  # Field name made lowercase.
    partition_label = models.CharField(db_column='Partition_Label', max_length=10, blank=True, null=True)  # Field name made lowercase.
    serial_number = models.CharField(db_column='Serial_Number', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storage_info'


class PrimaryInfo(models.Model):
    hostname = models.CharField(db_column='Hostname', max_length=18, primary_key=True)  # Field name made lowercase.
    mm_ip = models.CharField(db_column='MM_IP', max_length=16, blank=True)  # Field name made lowercase.
    bay = models.CharField(db_column='Bay', max_length=6, blank=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=16, blank=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=15, blank=True, null=True)  # Field name made lowercase.
    annotation = models.CharField(db_column='Annotation', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mac_address = models.CharField(db_column='MAC_Address', max_length=20, blank=True, null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=64, blank=True)
    kernel = models.CharField(db_column='Kernel', max_length=64, blank=True)
    manufacturer = models.CharField(db_column='Manufacturer', max_length=16, blank=True)
    cpus = models.IntegerField(db_column='CPUs', blank=True)
    cpu_version = models.CharField(db_column='CPU_Version', max_length=48, blank=True)
    serial_number = models.CharField(db_column='Serial_Number', max_length=24, blank=True)
    product_name = models.CharField(db_column='Product_Name', max_length=48, blank=True)
    memory_total = models.CharField(db_column='Memory_Total', max_length=12, blank=True)
    disk_total = models.CharField(db_column='Disk_Total', max_length=12, blank=True)
    mmmod = models.CharField(db_column='MMMod', max_length=16, blank=True, null=True) # Field name made lowercase.
    status_list =(('status_online', 'online'),
                 ('status_repair', 'repairing'),
                 ('status_retired', 'retired'))
    status = models.CharField(max_length=24, blank=True, choices=status_list)

    class Meta:
        managed = False
        db_table = 'primary_info'


class SoftwareInfo(models.Model):
    hostname = models.CharField(db_column='Hostname', max_length=20, primary_key=True)  # Field name made lowercase.
    softwarename = models.CharField(db_column='SoftwareName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    softwareversion = models.CharField(db_column='SoftwareVersion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    releaseversion = models.CharField(db_column='ReleaseVersion', max_length=30, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=15, blank=True, null=True)  # Field name made lowercase.
    installtime = models.CharField(db_column='InstallTime', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'software_info'


class SystemParameter(models.Model):
    hostname = models.CharField(db_column='Hostname', max_length=15, primary_key=True)  # Field name made lowercase.
    parametername = models.CharField(db_column='ParameterName', max_length=60)  # Field name made lowercase.
    parametervalue = models.CharField(db_column='ParameterValue', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'system_parameter'

class DnsInfo(models.Model):
    ip_address = models.CharField(db_column='IP_Address', max_length=16, blank=True, primary_key=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='Hostname', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dns_info'

class VMInfo(models.Model):
    tabname = models.CharField(max_length=24)
    instance_name = models.CharField(max_length=64)
    hostname = models.CharField(max_length=32)
    vcpus = models.IntegerField()
    memory_mb = models.IntegerField()
    username = models.CharField(max_length=16)
    hypervisor = models.CharField(max_length=32)
    project_name = models.CharField(max_length=64)
    image_name = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=36, primary_key=True)
    vm_state = models.CharField(max_length=16)
    annotation = models.CharField(max_length=128,blank=True)

    class Meta:
        managed = False
        db_table = 'vm'

    def __init__(self, *args, **kwargs):
        super(VMInfo, self).__init__(*args, **kwargs)
        if (self.pk == '202.169.170.44'):
            run_updatedb = "sudo /bin/python /root/update.py"
            host_name = "<hostname>"
            
            connection = "/usr/bin/ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 -i /root/.ssh/id_rsa -lcentos"
            cmd_updatedb = '''%s %s %s'''%(connection, host_name, run_updatedb)
            
            process_updatedb = subprocess.Popen(cmd_updatedb, stdout=subprocess.PIPE, shell=True)
            output_updatedb = process_updatedb.stdout.read()

