# simple-bot-for-tourism
### Source Code
The code for Simple_Bot_for_tourism.ipynb is taken (inspired) mostly from  
[Tutorial - Building a Simple Bot with the Rasa Stack](https://colab.research.google.com/drive/11RXiVVURaxrTdf7wYjbe3qDq5XtntqMO)
with the following additions:
* Custom actions are used to retrieve data from Tourism Information & Services Hub (TIH) API  
https://tih-dev.stb.gov.sg/content-api/apis
* Custom Entity extraction and synonym

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
**MANDATORY**  
***Pls replace apikey in actions.py with a valid one and upload actions.py to Colab /content root folder,  
otherwise action server will not work !!***  
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 

[Register as a developer](https://tih.stb.gov.sg/content/tih/en/profile/register.html) to receive apikey required to run custom action server  

### Possible improvements
- Denoted as TODO within code
  Error handling when result is not found / multiple results found
- Improve the wording of reponse / template
- More complex story flow
- More training examples
- More stories & actions

### Useful Resources:
https://rasa.com/docs/  
https://github.com/RasaHQ/rasa-demo
https://github.com/RasaHQ/rasa_core_sdk  
https://github.com/RasaHQ/rasa_core_sdk/tree/master/examples/moodbot  
https://tih-dev.stb.gov.sg/content-api/apis  
