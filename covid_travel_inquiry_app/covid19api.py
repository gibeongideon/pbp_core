from django.conf import settings
import json
from .exceptions import DataFetchException, CountrySaveException
 
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


from .testdata import response # test

class Covid19Api(object):

    def __init__(self):
        """ Initialize wit url setup/create/build"""
        self.baseurl='https://api.covid19api.com'


    def get_json_response(self,url):
        """
        Return a dictionary that 
        """      
        try:
            data = urlopen(url).read().decode("utf-8")
            return json.loads(data)#['rates']

        except Exception as e:

            raise DataFetchException(f"Error fetching rates:{e}")
  

    def save_countries_in_db(self):
        """
        Creates countries  and save for future reference
        """ 
        fetch_countries = self.get_json_response()

        for country,slug ,ISO2 in fetch_countries.items():
        
            try:
                from .models import Country#TravelPermitInquiry,
                currency, _ = Country.objects.get_or_create(name=country,slug=slug,ISO2=ISO2)

            except Exception as e:
                raise CountrySaveException(f"Error saving rates:{e}")
                pass ### 

            
                            
    def latest_confirmed_cases_for(self,country):
        url=self.baseurl+"/summary/"
        response_list=response#get_json_response(url)
        #return 18888
        
        for covid_summary_dic in response_list:
            if str((covid_summary_dic.get('Country')))==str(country):
                return float(covid_summary_dic.get('cases'))
        else:
            return 0#add smart exception handling #TODO
            
            
            
            
