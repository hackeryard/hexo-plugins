import os
from wsgiref.simple_server import make_server
import re
import logging

WWW_PATH = '/usr/share/nginx/html'
def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    match = re.search("^deploy/?$", path)
    if match is not None:
        logging.warning("触发部署")

        command = [
            "cd {0}".format(WWW_PATH),
            "git pull"
        ]
        final_cmd = '&&'.join(command)
        os.system(final_cmd)

        start_response('200 OK', [('Content-Type', 'text/plain')])    
        return ["Deploy Done.".encode("utf-8")]
    else:
        logging.fatal("非hook触发")
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])    
        return ["NOT FOUND".encode("utf-8")]


if __name__ == "__main__":
    httpd = make_server('', 2233, application)
    print('Serving HTTP on port 2233...') 
    httpd.serve_forever()