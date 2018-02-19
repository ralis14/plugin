import json
from pathlib import Path

class Docker_Plugin:
    def __init__(self):
        with open('test.json') as json_data:
            data = json.load(json_data)
        self.location = Path.cwd()
        self.tool_info = data['Tool']
        self.docker_info = data['Docker']
        pass
    def session_start(self):
        #call the build docker
        #run the image
        #start gui
        #capture commands
        #pass into container
        pass
    def build_docker(self):
        #assert the is a plugin.json file to read and build docker image
        #use the flags from the json object to build the docker string
        #store the string
        pass
    def session_end(self):
        #stop the image
        pass
