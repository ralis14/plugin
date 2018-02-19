import docker
import os
from pathlib import Path
root_dir = str(Path.cwd())
root_dir +='../..'

'''
add the certs cert.pem and key.pem information or a tls config file with the paths, run docker-machine env on the server to view the url and paths
'''
certs = {"cert":str(os.environ['docker_client_cert']), "key":str(os.environ['docker_client_key'])}
class DockerApi:
    def __init__(self, url='192.168.99.100:2376', tls_config=docker.tls.TLSConfig(client_cert=(certs['cert'], certs['key']))):
        self.server = docker.from_env()
        self.client = docker.DockerClient(base_url=url, tls=tls_config)
        self.client_params = {'tty':False, 'exec':'/bin/bash', 'auto_remove':False, 'detach':False, 'name':'default','stdin_open':False, 'volumes':{}}
        pass
    def ping(self):
        print(self.client.ping())
    def tty(self):
        self.client_params['tty']=True
        return self
    def stdinOpen(self):
        self.client_params['stdin_open']= True
        return self
    def detach(self):
        self.client_params['detach']=True
        return self
    def image(self, image):
        self.client_params['image']= image
        return self
    def volumes(self, host_path=root_dir, docker_path='/plugin', mode=''):
        volumes={host_path:{'bind':docker_path, 'mode':mode}}
        self.client_params['volumes']=volumes
        return self
    def container_name(self, name):
        self.client_params['name']=name
        return self
    def auto_remove(self):
        self.client_params['auto_remove']=True
        return self
    def execute(self, command):
        self.client_params['exec']=command
        return self
    def run(self):
        cont = self.client.containers.run(self.client_params['image'], auto_remove=True, command=self.client_params['exec'], detach=self.client_params['detach'], tty=self.client_params['tty'], name=self.client_params['name'], stdin_open=self.client_params['stdin_open'], volumes=self.client_params['volumes'])

    '''
    Get the list of items make them strings and check if the image
    is in the list
    '''
    def _image(self, image):
        dic = {'<':'','>':'',':':'','Image':''}
        try:
            im = self.server.images.list()
        except:
            print("There was an Error")
        for x in im:
            x =str(x)
        for x in im:
            for i,j in dic.items():
                x = x.replace(i,j)
        if image in im:
            return True
        return False

class Docker_String():
    def __init__(self):
        self.start = "docker run"
    def container(self, container):
        self._container = "{}",format(container)
    def interactive(self):
        self._interactive = "-it"
        return self
    def name(self, name):
        self._name = "--name {}".format(name)
        return self
    def remove_after(self):
        self._remove = "--rm"
        return self
    def volume(self):
        self._volume = "-v"
        return self
    def detach(self):
        self._detach = "-d"
        return self
    def combine(self):
        li = self.__dict__.values()
        print(' '.join(li))



d = DockerApi()
#d.ping();
cont = d.image('rula018/practicum').detach().tty().stdinOpen().volumes().execute('/bin/zsh').run()
