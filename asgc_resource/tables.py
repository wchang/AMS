import django_tables2 as tables
from asgc_resource.models import AssetInfo
from asgc_resource.models import PrimaryInfo
from asgc_resource.models import SoftwareInfo
from asgc_resource.models import SystemParameter

class PrimaryInfoTable(tables.Table):
    class Meta:
        model = PrimaryInfo
        attrs = {"class": "paleblue"}

class SoftwareInfoTable(tables.Table):
    class Meta:
        model = SoftwareInfo
        attrs = {"class": "paleblue"}

class SystemParameterTable(tables.Table):
    class Meta:
        model = SystemParameter
        attrs = {"class": "paleblue"}

class AssetInfoTable(tables.Table):
    class Meta:
        model = AssetInfo
        attrs = {"class": "paleblue"}

class ColumnsSoftwareInfoTable(tables.Table):
    SoftwareInfo = tables.Column()
    class Meta:
        attrs = {"class":"paleblue"}

class ColumnsSystemParameterTable(tables.Table):
    SystemParameter = tables.Column()
    class Meta:
        attrs = {"class":"paleblue"}

