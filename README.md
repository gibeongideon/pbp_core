# pbp_core

QUERIES(GET)


[
    {
        "id": 1,
        "date_of_travel": "2022-01-24T18:51:00Z",
        "date_of_return": null,
        "age_of_traveler": 24,
        "adult_present": false,
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 2,
        "date_of_travel": "2022-01-27T18:51:00Z",
        "date_of_return": null,
        "age_of_traveler": 45,
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 3,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "age_of_traveler": 12,
        "adult_present": false,
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 4,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "age_of_traveler": 17,
        "adult_present": false,
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 5,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": "2022-07-24T18:53:00Z",
        "age_of_traveler": 45,
        "origin_country": 1,
        "destination_country": 2
    }

{

    "date_of_travel": "2022-01-27T19:01:00Z",
    "date_of_return": "2022-02-09T19:01:00Z",
    "age_of_traveler": 34,
    "origin_country": 2,
    "destination_country": 1
}

]





RESPECTIVE RESPONSES





HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept



[
    {
        "id": 1,
        "date_of_travel": "2022-01-24T18:51:00Z",
        "date_of_return": null,
        "age_of_traveler": 24,
        "adult_present": false,
        "inquiry_status": "Denied",
        "reason_for_denial": "Date of travel is between the next 2 and 5 following working days from 2022-01-24 15:51:54.004925+00:00",
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 2,
        "date_of_travel": "2022-01-27T18:51:00Z",
        "date_of_return": null,
        "age_of_traveler": 45,
        "adult_present": false,
        "inquiry_status": "Denied",
        "reason_for_denial": "Traveller destination_country has less Covid19 cases( 2000.0) than origin_country with 9000.0 cases",
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 3,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "age_of_traveler": 12,
        "adult_present": false,
        "inquiry_status": "Denied",
        "reason_for_denial": "Traveller of age between 21 & 65 are only allowed to apply permit.Yet traveler is just 12 years old",
        "origin_country": 1,
        "destination_country": 2
    },
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
    {
        "id": 5,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": null,
        "age_of_traveler": 18,
        "adult_present": true,
        "inquiry_status": "Denied",
        "reason_for_denial": "Traveller destination_country has less Covid19 cases( 2000.0) than origin_country with 9000.0 cases",
        "origin_country": 1,
        "destination_country": 2
    },
    {
        "id": 6,
        "date_of_travel": "2022-01-27T18:52:00Z",
        "date_of_return": "2022-07-24T18:53:00Z",
        "age_of_traveler": 45,
        "adult_present": false,
        "inquiry_status": "Denied",
        "reason_for_denial": "Date of return is not within 2 months of the Date of travel from date_of_travel(2022-01-24 15:54:08.801849+00:00)",
        "origin_country": 1,
        "destination_country": 2
    }


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

]