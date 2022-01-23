# TESTS FIRST! 
#I love TDD/Testing everything is the key to great apps

from django.test import TestCase  # ,Client

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import TravelPermitInquiry,Country
from datetime import datetime, timedelta ,timezone


#test         
class TravelPermitInquiryTestCase(TestCase):

    def setUp(self):
        self.origin_country=Country.objects.create(name="Rwanda")
        self.dest_country=Country.objects.create(name="Kenya")
        
        today = datetime.now(timezone.utc)   
        self.right_time_to_travel = today + timedelta(days=3)#i.e b/w 2-5
        self.wrong_time_to_travel  = today + timedelta(days=7)
        self.another_wrong_time_to_travel  = today + timedelta(days=1)
        
        self.right_date_of_return = today + timedelta(days=45)#within two months
        self.wrong_date_of_return  = today + timedelta(days=90)#more than two months
      
        
    #__________________________________________________TRAVEL DATE SIMPLE TESTS_______________________________________________#  
    
          
    def test_correct_date_of_travel_right_time(self):
        """
        Date of travel is between the next 2 and 5 following working days from the date of request. Otherwise, the travel permit must be denied.
        """
     
        
        #________________________________________________________________________#
        #with correct date_of_travel
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 39,
            adult_present= False,  
        )
        
        self.assertEqual(1,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        print(TravelPermitInquiry.objects.get(id=1).reason_for_denial)
        print(self.right_time_to_travel)
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D3')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        
        
        if  covid_cases_in_origin_country>covid_cases_in_destination_country:
            self.assertEqual("Denied", inquiry_status)
        else:
            self.assertEqual("Allowed", inquiry_status)
         
         
         
    def test_correct_date_of_travel_wrong_time(self):
        """
        Date of travel is between the next 2 and 5 following working days from the date of request. Otherwise, the travel permit must be denied.
        """
        #________________________________________________________________________#
        #with wrong date_of_travel
        print('WWWT', self.right_time_to_travel)
        TravelPermitInquiry.objects.create(
            date_of_travel =self.wrong_time_to_travel,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 39,
            adult_present= False,  
        )
        
        
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D1')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        print(self.wrong_time_to_travel)
        
        self.assertEqual("Denied", inquiry_status)
        
        
        #________________________________________________________________________#
        #with Another wrong date_of_travel
        print('WWWT', self.right_time_to_travel)
        TravelPermitInquiry.objects.create(
            date_of_travel = self.another_wrong_time_to_travel,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 34,
            adult_present= False,  
        )
        
        self.assertEqual(2,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=2).inquiry_status
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D2')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        print(self.wrong_time_to_travel)
        
        self.assertEqual("Denied", inquiry_status)
        
        
        
        
        
    #__________________________________________________RETURN DATE SIMPLE TESTS_______________________________________________#        
        
        
        
    def test_right_time_of_return(self):
        """
        Date of return is not within 2 months of the Date of travel.
        """
            
        #________________________________________________________________________#
        #with correct date_of_return
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            date_of_return=self.right_date_of_return,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 43,
            adult_present= False,  
        )
        
        self.assertEqual(1,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        print(TravelPermitInquiry.objects.get(id=1).reason_for_denial)
        print(self.right_time_to_travel)
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D3')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        
        
        if  covid_cases_in_origin_country>covid_cases_in_destination_country:
            self.assertEqual("Denied", inquiry_status)
        else:
            self.assertEqual("Allowed", inquiry_status)        
        
    def test_wrong_time_to_return(self):
        """
        Date of return is not within 2 months of the Date of travel.wrong_time
        """
        #________________________________________________________________________#
        #with wrong date_of_travel
        print('WWWTdd', self.right_time_to_travel)
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            date_of_return=self.wrong_date_of_return,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 39,
            adult_present= False,  
        )
        
                
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D1')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        print(self.wrong_time_to_travel)
        
        self.assertEqual("Denied", inquiry_status)
  
  
      
    #__________________________________________________RETURN TRAVELER AGE LIMITS REQUIREMENTS_______________________________________#  
    
    def test_feedback_for_under_over_age(self):
        """
        Traveller of within 16-21 of age travel with the supervision of an adult.Requirement
        """
            
        #________________________________________________________________________#
        #Under_AGE<15
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            date_of_return=self.right_date_of_return,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 11,
            adult_present= False,  
        )
        
        self.assertEqual(1,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        print(TravelPermitInquiry.objects.get(id=1).reason_for_denial)
        print(self.right_time_to_travel)
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D3')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
               

        self.assertEqual("Denied", inquiry_status)
        
    
        #________________________________________________________________________#
        #AGE>65
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            date_of_return=self.right_date_of_return,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 77,
            adult_present= False,  
        )
        
        self.assertEqual(2,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        print(TravelPermitInquiry.objects.get(id=1).reason_for_denial)
        print(self.right_time_to_travel)
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D3')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        

        self.assertEqual("Denied", inquiry_status)

        
    
    

 #__________________________________________________RETURN TRAVELER of15-21 REQUIREMENTS_______________________________________#  
    
    def test_feedback_for_16_21_years_old(self):
        """
        Traveller of within 16-21 of age travel with the supervision of an adult.Requirement
        """
            
        #________________________________________________________________________#
     
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            date_of_return=self.right_date_of_return,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 17,
            adult_present= False,  
        )
        
        self.assertEqual(1,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=1).inquiry_status
        print(TravelPermitInquiry.objects.get(id=1).reason_for_denial)
        print(self.right_time_to_travel)
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D8')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
               

        self.assertEqual("Denied", inquiry_status)
        
    
        #________________________________________________________________________#
   
        TravelPermitInquiry.objects.create(
            date_of_travel =self.right_time_to_travel,
            date_of_return=self.right_date_of_return,
            origin_country = self.origin_country,
            destination_country = self.dest_country,
            age_of_traveler = 17,
            adult_present= True,  
        )
        
        self.assertEqual(2,TravelPermitInquiry.objects.count())
        
        inquiry_status = TravelPermitInquiry.objects.get(id=2).inquiry_status
        print(TravelPermitInquiry.objects.get(id=1).reason_for_denial)
        print(self.right_time_to_travel)
        
        covid_cases_in_origin_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_origin_country
        covid_cases_in_destination_country = TravelPermitInquiry.objects.get(id=1).covid_cases_in_destination_country
        
        print('CASES O_D9')
        print(covid_cases_in_origin_country,covid_cases_in_destination_country)
        

        if  covid_cases_in_origin_country>covid_cases_in_destination_country:
            self.assertEqual("Denied", inquiry_status)
        else:
            self.assertEqual("Allowed", inquiry_status)  
            
            
            
    
    
    
# Endpoint tests

# class TravelPermitInquiryApiTest(APITestCase):


#     def setUp(self):
#         self.origin_country=Country.objects.create(name="Kenya")
#         self.dest_country=Country.objects.create(name="Rwanda")

#     def test_create_iage_of_travelernaccount(self):
#         """
#         Ensure we can create a new TravelPermitInquiry object through endpoint.
        
#         """
#         # url = reverse('travelpermitinquiry-list')
#         url='/api/covid_travel_permit_inquiry/'
#         data = {"date_of_travel":"2022-01-253T00:00:00Z",
#             "date_of_return":"2022-02-24T00:00:00Z",
#             "origin_country":self.origin_country,
#             "destination_country":self.dest_country,
#             "age_of_traveler":39,
#             "adult_present":"",
        
#         }
        
        
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(TravelPermitInquiry.objects.count(), 1)
#         self.assertEqual(TravelPermitInquiry.objects.get().age_of_traveler, 39)

    
    
          
                                       
    
    
          
                                   
