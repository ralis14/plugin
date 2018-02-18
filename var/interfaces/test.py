import docker
from pprint import pprint
import json
from pathlib import Path
from Docker import Docker_String



a = Docker_String()
a.interactive().remove_after()
a.combine()


with open('../Plugin.json') as json_data:
    data= json.load(json_data)
docker = data['Docker']
tool = data['Tool']
pprint(docker['dependencies'])
pprint(tool['input'])
import pathlib
file_dir = pathlib.Path.cwd()
print(file_dir)
