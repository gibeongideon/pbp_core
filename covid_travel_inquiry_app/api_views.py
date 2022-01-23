from rest_framework import viewsets
from .models import TravelPermitInquiry
from .serializers import TravelPermitInquirySerializer

class TravelPermitInquiryViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating a TravelPermitInquiry."""
    queryset = TravelPermitInquiry.objects.all()
    serializer_class = TravelPermitInquirySerializer

    
    
