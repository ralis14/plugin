from pathlib import Path
import json

class Native_Plugin:
    def __init__(self):
        #read the json file and set up to call docker
        with open('../Plugin.json') as json_data:
            data = json.load(json_data)
        self.location = Path.cwd()
        self.tool_info = data['Tool']
        pass
    def session_start(self):
        pass
    def session_end(self):
        pass
    def tool_options(self):
        pass
