from django.shortcuts import render, redirect#, reverse
# from django.contrib.auth.decorators import login_required

from .models import TravelPermitInquiry
from .forms import TravelPermitInquiryForm


def homepage(request):
    return render(request, "covid_travel_inquiry_app/home_page.html")

#@login_required#not must 
def travel_permit_inquiry_view(request):
    form = TravelPermitInquiryForm(request.POST)
    latest_queriz = TravelPermitInquiry.objects.order_by("-id")[:5]
    if request.method == 'POST':
        # form = TravelPermitInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/permit_inquiry/')
        else:
            return redirect('/permit_inquiry/') 
    else:
        form = TravelPermitInquiryForm()
        return render(request, 'covid_travel_inquiry_app/covid_travel_inquiry_form.html',{'form':form, "latest_queriz": latest_queriz})




