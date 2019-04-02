# rasa-action-server

From Console Home Create Project

Run commands from Cloud Shell
```
git clone https://github.com/pekgnee/rasa-action-server
cd rasa-action-server
virtualenv --python python3 ~/envs/rasa_action_server
source ~/envs/rasa_action_server/bin/activate
pip install -r requirements.txt
python main.py
```

Preview app with "Web preview"
Terminating the preview instance with Ctrl+C

```
gcloud app create
gcloud app deploy app.yaml --project {{project-id}}
```

### Resources:
https://cloud.google.com/community/tutorials/python-gae-quickstart  
https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard_python37/hello_world  

https://github.com/RasaHQ/rasa_core_sdk/tree/master/examples/moodbot  
https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app  
https://cloud.google.com/cloud-build/docs/quickstart-docker
