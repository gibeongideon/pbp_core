from django import forms
from .models import TravelPermitInquiry


class TravelPermitInquiryForm(forms.ModelForm):

    class Meta:
        model = TravelPermitInquiry
        fields = (
            "date_of_travel",
            "date_of_return",
            "origin_country",
            "destination_country",
            "age_of_traveler",
            "adult_present",
        )


