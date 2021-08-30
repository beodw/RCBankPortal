# socket module to get ip of hosting server.
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
class DjangoApplication():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 80
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
        cherrypy.config.update({
            'server.socket_host': self.HOST,
            'server.socket_port': self.PORT,
            'engine.autoreload_on': True,
            'log.screen': False,
            'log.error_file': os.getcwd() + './logs.txt',
            'log.error_file': os.getcwd() + './error_log.txt',
            'log.access_file':os.getcwd()+ './access_log.txt',
        })
        self.mount_static(settings.STATIC_URL, settings.STATIC_ROOT)
        cherrypy.tree.graft(WSGIHandler())
        cherrypy.engine.start()
        cherrypy.log("Server running at http://" + self.HOST + ":" + str (self.PORT) + " with pid " + str ( os.getpid() ) + ". Kill this process to shut down server." )
        cherrypy.engine.block()
if __name__ == "__main__":
    DjangoApplication().run()
