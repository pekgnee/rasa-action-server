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

      url_params = {'apikey': apikey}
      url_path = urljoin('https://tih-api.stb.gov.sg/content/v1/attractions/name/', attraction)
      r = requests.get(url_path, params=url_params)
      
      # Check if r.status_code successful
      json_data = json.loads(r.text)      
      result = json_data["data"]["admissionInfo"]

      return [SlotSet("admission", result if result is not None else [])]