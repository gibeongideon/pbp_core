# from django.conf import settings
import json
from .exceptions import DataFetchException
 
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


from .testdata import response,resp # test

class Covid19Api(object):

    def __init__(self):
        """ Initialize wit url setup/create/build"""
        self.baseurl='https://api.covid19api.com'


    def get_json_response(self,url):
        """
        Return a dictionary that return json data from any endpoint
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
        from .models import Country#fix_circular import
        # url=self.baseurl+"/countries/"
        url='https://api.covid19api.com/countries'

        fetched_countries = self.get_json_response(url)
        response_list=fetched_countries

        for covid_summary_dic in response_list:
            country=covid_summary_dic["Country"]
            slug=covid_summary_dic["Slug"]
            ISO2=covid_summary_dic["ISO2"]
  
            Country.objects.update_or_create(name=country,slug=slug,ISO2=ISO2)
         
                            
    def latest_confirmed_cases_for(self,country):
        # url=self.baseurl+"/summary/"
        url='https://api.covid19api.com/summary'
        world_covid_summary_dict=self.get_json_response(url)
        counties_summary_list=world_covid_summary_dict["Countries"]
        
        for each_country_covid_summary_dic in counties_summary_list:
            if str((each_country_covid_summary_dic.get('Country')))==str(country):
                return float(each_country_covid_summary_dic.get('TotalConfirmed'))
        else:
            return 0#add smart exception handling #TODO
            
            
            
            
