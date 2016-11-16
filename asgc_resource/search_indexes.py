from haystack import indexes
from models import PrimaryInfo
from models import VMInfo
from models import StorageInfo
from repair.models import Request

class PrimaryInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='hostname')
    mm_ip = indexes.CharField(model_attr='mm_ip')
    bay = indexes.CharField(model_attr='bay')
    location = indexes.CharField(model_attr='location')
    purpose = indexes.CharField(model_attr='purpose') 
    annotation = indexes.CharField(model_attr='annotation')
    mac_address = indexes.CharField(model_attr='mac_address')
    mmmod = indexes.CharField(model_attr='mmmod')
    status = indexes.CharField(model_attr='status')
  
    def get_model(self):
        return PrimaryInfo

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects

class VMInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    instance_name = indexes.CharField(model_attr='instance_name')
    hostname = indexes.CharField(model_attr='hostname')
    vcpus = indexes.CharField(model_attr='vcpus')
    memory_mb = indexes.CharField(model_attr='memory_mb')
    username = indexes.CharField(model_attr='username') 
    hypervisor = indexes.CharField(model_attr='hypervisor')
    project_name = indexes.CharField(model_attr='project_name')
    image_name = indexes.CharField(model_attr='image_name')
    ip_address = indexes.CharField(model_attr='ip_address')
    vm_state = indexes.CharField(model_attr='vm_state')

    def get_model(self):
        return VMInfo
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects

class StorageInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    controller_mm_ip = indexes.CharField(model_attr='controller_mm_ip')
    location = indexes.CharField(model_attr='location')
    factory = indexes.CharField(model_attr='factory')
    hardware_id = indexes.CharField(model_attr='hardware_id')
    spec = indexes.CharField(model_attr='spec')  
    raw_space_tb = indexes.CharField(model_attr='raw_space_tb')
    storage_port_address = indexes.CharField(model_attr='storage_port_address')
    disk_server = indexes.CharField(model_attr='disk_server')
    partition_label = indexes.CharField(model_attr='partition_label')
    serial_number = indexes.CharField(model_attr='serial_number')
    
    def get_model(self):
        return StorageInfo
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects

class RequestIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    serial_number = indexes.CharField(model_attr='serial_number')
    hdd_sn = indexes.CharField(model_attr='hdd_sn')
    hdd_type = indexes.CharField(model_attr='hdd_type')
    hostname = indexes.CharField(model_attr='hostname')
    manufacture = indexes.CharField(model_attr='manufacture')
    product_name = indexes.CharField(model_attr='product_name')
    ip = indexes.CharField(model_attr='ip')
    location = indexes.CharField(model_attr='location')
    tag = indexes.CharField(model_attr='tag')
    description = indexes.CharField(model_attr='description')
    report_time = indexes.CharField(model_attr='report_time')
    status = indexes.CharField(model_attr='status')

    def get_model(self):
        return Request
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects

