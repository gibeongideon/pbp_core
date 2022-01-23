from django.contrib import admin
from .models import TravelPermitInquiry,Country

admin.site.register(Country)

class TravelPermitInquiryAdmin(admin.ModelAdmin):
    list_display = (
            "id",
            "date_of_travel",
            "date_of_return",
            "origin_country",
            "destination_country",
            "age_of_traveler",
            "adult_present",
            "inquiry_status",
            "reason_for_denial"
        )

    
    list_display_links = ('id', )
    search_fields = ('di', )
    list_editable = (
            # "date_of_travel",
            #"date_of_return",
            "origin_country",
            "destination_country",
            "age_of_traveler",
            "adult_present",
        )

admin.site.register(TravelPermitInquiry, TravelPermitInquiryAdmin)
