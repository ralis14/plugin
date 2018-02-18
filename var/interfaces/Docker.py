import docker
import os


'''
add the certs cert.pem and key.pem information or a tls config file with the paths, run docker-machine env on the server to view the url and paths
'''
certs = {"cert":str(os.environ['docker_client_cert']), "key":str(os.environ['docker_client_key'])}
class Docker:
    def __init__(self, url='192.168.99.100:2376', tls_config=docker.tls.TLSConfig(client_cert=(certs['cert'], certs['key']))):
        self.server = docker.from_env()
        self.client = docker.DockerClient(base_url=url, tls=tls_config)
        pass
    
    '''
    Get the list of items make them strings and check if the image
    is in the list
    '''
    def _image(self, image):
        dic = {'<':'','>':'',':':'','Image':''}
        try:
            im = self.client.images.list()
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
