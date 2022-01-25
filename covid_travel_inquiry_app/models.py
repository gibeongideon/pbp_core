
from django.db import models
from datetime import datetime, timedelta ,timezone
from .covid19api import Covid19Api
covid19api = Covid19Api()
       
#class Setting(models.Model):
 #   name = models.CharField(
 #       max_length=100,
 #       blank=True,
 #       null=True
  #  )  
    
  #  def __str_(self):
  #      return str(self.name)        
               
               
class Country(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    slug = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )      
    ISO2 = models.CharField(
        max_length=100,
        blank=True,
        null=True
    ) 

    class Meta: 
        verbose_name_plural = "Countries"    

    def __str__(self):
        return str(self.name)
              
        
class TravelPermitInquiry(models.Model):
    """
    Represent user's travelPermitInquiry instance.
    Define fields to store date_of_travel, date_of_return,origin_country,
    destination_country,age_of_traveler,inquiry_status,and,reason_for_denial.
        
    """
    
    date_of_travel = models.DateTimeField(blank=True, null=True) 
    date_of_return = models.DateTimeField(blank=True, null=True)#optional
    
    origin_country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="origin_countries",
    
    )
    destination_country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="destination_countries",
    
    )
                
    age_of_traveler = models.IntegerField()
    
        
    adult_present= models.BooleanField(blank=True, null=True)   
    
    inquiry_status = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    
    reason_for_denial= models.TextField(
        max_length=300,
        default='NONE',
        blank=True,
        null=True
    )#additional_feature_reason_is_
    
    
    #support_fields/enables_efficient_tests
    #origin_country_cases= models.IntegerField(blank=True, null=True)
    #destination_country_cases= models.IntegerField(blank=True, null=True)
      
      
    class Meta:
        db_table = "travel_permit_inquiry"  
        verbose_name_plural = "Covid19 Travel Permit Inquiries"


    def __str__(self):
        return 'Inquiry-'+str(self.id)        
        
    @staticmethod
    def covid_cases_in(country):
        try:
            # covid19api = Covid19Api()
            return covid19api.latest_confirmed_cases_for(country)

        except Exception as e:
            print('API_ERR',e)#debu
            return 0
            
    @property    
    def covid_cases_in_origin_country(self):
        origin_country=self.origin_country
        return self.covid_cases_in(origin_country)

    @property    
    def covid_cases_in_destination_country(self):
        destination_country=self.destination_country
        return self.covid_cases_in(destination_country)  
              

    def process_inquiry(self):
            today = datetime.now(timezone.utc)            
            earliest_date_to_travel = today + timedelta(days=2)
            latest_date_to_travel  = today + timedelta(days=5)
                        
            if self.date_of_travel > latest_date_to_travel  or self.date_of_travel < earliest_date_to_travel:                        
                 self.inquiry_status="Denied"
                 self.reason_for_denial = f"Date of travel is between the next 2 and 5 following working days from {today}"
                        
            if self.date_of_return and not self.inquiry_status=="Denied":
                allowed_travel_days=60 #bad code #refactor#hard_coded_can_be_place_in_seetings_model_to_allow_quick changes#TODO
                latest_alowed_return_day = latest_date_to_travel + timedelta(days=allowed_travel_days)
 
            
                if  latest_alowed_return_day < self.date_of_return:
                    self.inquiry_status="Denied"
                    self.reason_for_denial = f"Date of return is not within 2 months of the Date of travel from date_of_travel({today})"
       
            if not self.inquiry_status=="Denied":
                if  self.age_of_traveler > 15 and self.age_of_traveler<=21:#bad code #refactor#hard_coded_can_be_place_in_seetings_model_to_allow_quick changes#TODO
                    if not self.adult_present:
                        self.inquiry_status="Denied"
                        self.reason_for_denial = f"Traveler is {self.age_of_traveler} years old without an adult yet all travelers within 16-21 of age travel with the supervision of an adult" 
                        
                if  self.age_of_traveler < 16 or self.age_of_traveler > 64 :#bad code #refactor#hard_coded_can_be_place_in_seetings_model_to_allow_quick changes#TODO
                    self.inquiry_status="Denied"
                    self.reason_for_denial = f"Traveller of age between 21 & 65 are only allowed to apply permit.Yet traveler is just {self.age_of_traveler} years old"
                    
                                                                                   
            if not self.inquiry_status=="Denied":      
               if  self.covid_cases_in_origin_country > self.covid_cases_in_destination_country :
                   self.inquiry_status="Denied"
                   self.reason_for_denial = f"Traveller destination_country({self.destination_country.name}) has less Covid19 cases( {self.covid_cases_in_destination_country}) than origin_country({self.origin_country.name}) with {self.covid_cases_in_origin_country} cases"
            
            if not self.inquiry_status:
               self.inquiry_status="Allowed"        
                     

            
    def save(self, *args, **kwargs):
        try:
            self.process_inquiry()                  
            super(TravelPermitInquiry, self).save(*args, **kwargs)    
               
        except Exception as e:
            print('ERR',e)#debu
            #super(TravelPermitInquiry, self).save(*args, **kwargs)
            pass 




#TODO-move to view level
class CountryListUpdate(models.Model):   
    def __str__(self):
        return 'Countries-List-Update '+str(self.id)
    class Meta: 
        verbose_name_plural = "Countries-List-Updates"
                             
    def save(self, *args, **kwargs):
        try:
            # covid19api = Covid19Api()
            covid19api.save_countries_in_db()                
            super(CountryListUpdate, self).save(*args, **kwargs)    
               
        except Exception as e:
            return#i.e dont create update at all

       


       
       