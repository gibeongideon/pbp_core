# pbp_core
Demo
No authentication required

https://travelguide22.herokuapp.com/
https://travelguide22.herokuapp.com/api/covid_travel_permit_inquiry/


QUERY1:


{

    "date_of_travel": "2022-01-27T19:01:00Z",
    "date_of_return": "2022-02-09T19:01:00Z",
    "age_of_traveler": 34,
    "origin_country": 2,
    "destination_country": 1
}




RESPECTIVE RESPONSE


{
    "id": 7,
    "date_of_travel": "2022-01-27T19:01:00Z",
    "date_of_return": "2022-02-09T19:01:00Z",
    "age_of_traveler": 34,
    "adult_present": false,
    "inquiry_status": "Allowed",
    "reason_for_denial": "NONE",
    "origin_country": 2,
    "destination_country": 1
}


_____________________________________
QUERY2


    {
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "age_of_traveler": 17,
        "adult_present": false,
        "origin_country": 1,
        "destination_country": 2
    },

    RESPONSE


    {
        "id": 4,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "age_of_traveler": 17,
        "adult_present": false,
        "inquiry_status": "Denied",
        "reason_for_denial": "Traveler is 17 years old without an adult yet all travelers within 16-21 of age travel with the supervision of an adult",
        "origin_country": 1,
        "destination_country": 2
    },




24/01/2022
App Building Time  Plan
________________________
2hours-Think hard
1hour-Paper Works
3hours(spread_time)-Test-Driven-Development/CICD
1hour-GO YELL AT MY NEIGHBOUR SAM!