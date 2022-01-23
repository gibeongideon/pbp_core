from rest_framework import serializers
from .models import TravelPermitInquiry


class TravelPermitInquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = TravelPermitInquiry
        fields = ('__all__')
        
        read_only_fields = ('inquiry_status','reason_for_denial',)


    

