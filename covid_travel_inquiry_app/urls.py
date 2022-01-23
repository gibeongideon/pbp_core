from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import form_views, api_views


router = DefaultRouter()

router.register(r'covid_travel_permit_inquiry', api_views.TravelPermitInquiryViewSet)

app_name = "covid_inquiry"

# print("router.urls",router.urls)

urlpatterns = [
    path('', form_views.homepage, name="homepage"),#presentation_page    
    path('api/', include(router.urls)),#endp_point
    path('permit_inquiry/', form_views.travel_permit_inquiry_view, name='permit_inquiry'),#client_form_url

]
