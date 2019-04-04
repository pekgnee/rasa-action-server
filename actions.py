from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests
import json
import urllib.parse
from urllib.parse import urljoin

apikey = 'E1Ju3RkMboFwowRN0IcVnJdZ3Grk8kEu'
attraction = urllib.parse.quote('Sentosa Merlion')

class ActionSearchAttraction(Action):
   def name(self):
      # type: () -> Text
      return "action_search_attraction"

   def run(self, dispatcher, tracker, domain):
      # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

      keyword_url = urllib.parse.quote(attraction)
      url_params = {'apikey': apikey, 'keyword': keyword_url}
      url_path = 'https://tih-api.stb.gov.sg/content/v1/attractions/search'
      r = requests.get(url_path, params=url_params)
      
      # Check if r.status_code successful
      json_data = json.loads(r.text)      
      data_list = json_data['data']
      result = next((data_item for data_item in data_list if keyword.lower() in data_item['name'].lower()), None)      
      return [SlotSet("search_result", result if result is not None else [])]
