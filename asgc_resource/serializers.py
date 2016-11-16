from models import PrimaryInfo
from rest_framework import serializers

class PrimaryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryInfo
        fields = ('hostname', 'mm_ip', 'bay', 'location', 'purpose', 'annotation', 'mac_address','os','kernel','manufacturer','cpus','cpu_version',
                  'serial_number','product_name','memory_total','disk_total','status')
