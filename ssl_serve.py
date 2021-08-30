# sys module to get command line args.
import socket
# SETUP DJANGO
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve()
os.environ["DJANGO_SETTINGS_MODULE"] = 'rAsset.settings'
import django
# start the django framework
django.setup()
# import necessary django modules
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
# SETUP CHERRYPY SERVER TO SERVE DJANGO APP.
import cherrypy
import sys
from rAsset.wsgi import application
class DjangoApplication():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 443
    def mount_static(self, url, root):
        """
        :param url: Relative url
        :param root: Path to static files root
        """
        config = {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': root,
            'tools.expires.on': True,
            'tools.expires.secs': 86400
        }
        cherrypy.tree.mount(None, url, {'/': config})
    def run(self):
        #Quick check to ensure proper argument list.
        if  len(sys.argv) != 3:
            print('Wrong number of args. Proper usage : python server.py [host] [port]')
            exit(1)
        if sys.argv[1] == "localhost":
            self.HOST = '127.0.0.1'
        else:
            self.HOST = sys.argv[1] 
        try:
            self.PORT = int ( sys.argv[2] )
        except:
            print('Supplied port is not a valid port number.')
            exit(1)
        cherrypy.config.update({'global':{
            'server.socket_host': self.HOST,
            'server.socket_port': self.PORT,
            'engine.autoreload_on': True,
            'log.screen': False,
            'log.error_file': os.getcwd() + './logs.txt',
            'log.error_file': os.getcwd() + './error_log.txt',
            'log.access_file':os.getcwd()+ './access_log.txt',
            'server.ssl_certificate' : "cert.pem",
            'server.ssl_private_key' : "privkey.pem",
            'server.ssl_module' : "builtin",
        }})
        self.mount_static(settings.STATIC_URL, settings.STATIC_ROOT)
        cherrypy.tree.graft(WSGIHandler())
        cherrypy.engine.start()
        print("Server running at https://" + self.HOST + ":" + str (self.PORT) + " with pid " + str ( os.getpid() ) + ". Kill this process to shut down server." )
        cherrypy.engine.block()
if __name__ == "__main__":
    DjangoApplication().run()
