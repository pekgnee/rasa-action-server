from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests
import json
import urllib.parse

# Custom action server using rasa_core_sdk https://github.com/RasaHQ/rasa_core_sdk
# Register as a developer at https://tih.stb.gov.sg/content/tih/en/profile/register.html 
# and replace apikey below in order to run action server
# Run with command:
#     python -m rasa_core_sdk.endpoint --actions actions
# Action endpoint uses DEFAULT_SERVER_PORT = 5055
apikey = '<<REPLACE-WITH-VALID-API-KEY>>'

# Store attraction entity in slot
class ActionGetAttractionEntity(Action):
   def name(self):
      # type: () -> Text
      return "action_get_attraction_entity"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
      result = next(tracker.get_latest_entity_values('attraction'), None)
      
      # TODO: Alternative if attraction entity was not extracted
      return [SlotSet("attraction", result if result is not None else 'Sentosa Merlion')]      

# Call Tourism Info Hub - Content API searchAttractionsByKeyword
# https://tih-dev.stb.gov.sg/content-api/apis/get/v1/attractions/search
class ActionSearchAttraction(Action):
   def name(self):
      # type: () -> Text
      return "action_search_attraction"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      keyword = '{}'.format(tracker.get_slot('attraction'))
      keyword_url = urllib.parse.quote(keyword)
      url_params = {'apikey': apikey, 'keyword': keyword_url}
      url_path = 'https://tih-api.stb.gov.sg/content/v1/attractions/search'
      r = requests.get(url_path, params=url_params)
      
      # TODO: Check if r.status_code successful
      json_data = json.loads(r.text)      
      data_list = json_data['data']
      
      # TODO: Improve logic to get best result among items in data_list
      # For now just take first data_item whose name matches keyword
      result = next((data_item for data_item in data_list if keyword.lower() in data_item['name'].lower()), None)      
      return [SlotSet("search_result", result if result is not None else [])]

# Store info_field entity in slot
class ActionGetInfoFieldEntity(Action):
   def name(self):
      # type: () -> Text
      return "action_get_info_field_entity"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
      result = next(tracker.get_latest_entity_values('info_field'), None)
      
      # TODO: Alternative handling if info_field entity was not extracted
      return [SlotSet("info_field", result if result is not None else 'nearestMRTStation')]
 
# Look up specific info_field from previous search_result
class ActionCheckInfo(Action):
   def name(self):
      # type: () -> Text
      return "action_check_info"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      info_field = tracker.get_slot('info_field')
      search_result = tracker.get_slot('search_result')

      # TODO: Alternative handling if search_result does not contain info_field
      return [SlotSet("info_result", search_result[info_field] if info_field in search_result else 'INFO NOT FOUND')]

# Store hotel entity in slot
class ActionGetHotelEntity(Action):
   def name(self):
      # type: () -> Text
      return "action_get_hotel_entity"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
      result = next(tracker.get_latest_entity_values('hotel'), None)
      
      # TODO: Alternative if hotel entity was not extracted
      return [SlotSet("hotel", result if result is not None else 'The Fullerton Hotel Singapore')]

# Call Tourism Info Hub - Content API searchAccommodationByKeyword
# https://tih-dev.stb.gov.sg/content-api/apis/get/v1/accommodation/search
class ActionSearchHotel(Action):
   def name(self):
      # type: () -> Text
      return "action_search_hotel"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      keyword = '{}'.format(tracker.get_slot('hotel'))
      keyword_url = urllib.parse.quote(keyword)
      url_params = {'apikey': apikey, 'keyword': keyword_url}
      url_path = 'https://tih-api.stb.gov.sg/content/v1/accommodation/search'
      r = requests.get(url_path, params=url_params)
      
      # TODO: Check if r.status_code successful
      json_data = json.loads(r.text)      
      data_list = json_data['data']
      
      # TODO: Improve logic to get best result among items in data_list
      # For now just take first data_item whose name matches keyword
      result = next((data_item for data_item in data_list if keyword.lower() in data_item['name'].lower()), None)      
      return [SlotSet("search_result", result if result is not None else [])]

