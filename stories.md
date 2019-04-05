
## search attraction
* search_attraction{"attraction": "Sentosa Merlion"}
  - action_get_attraction_entity
  - slot{"attraction": "Sentosa Merlion"}
  - utter_search_attraction
  - action_search_attraction
  - slot{"search_result": "Ticket prices are $X(adult) & $Y*(child)"}
  - utter_search_result
* check_info{"info_field": "nearestMrtStation"}
  - action_get_info_field_entity
  - slot{"info_field": "nearestMRTStation"}
  - utter_check_info
  - action_check_info
  - slot{"info_result": "Holland Village"}
  - utter_info_result
* no_other_request
  - utter_no_other_request
 

## search_hotel
* search_hotel{"hotel": "Hotel Royal"}
  - action_get_hotel_entity
  - slot{"hotel": "Hotel Royal"}
  - utter_search_hotel
  - action_search_hotel
  - slot{"search_result": "5-star hotel located in Orchard area"}
  - utter_search_result
* check_info
  - action_get_info_field_entity
  - slot{"info_field": "amenaties"}
  - utter_check_info
  - action_check_info
  - slot{"info_result": "swimming pool"}
  - utter_info_result
* no_other_request
  - utter_no_other_request

