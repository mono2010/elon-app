#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/elon-app')
from flaskapp import app as application
**3. Enable mod_wsgi.**
The apache server displays html pages by default but to serve dynamic content from a Flask app we’ll have to make a few changes. In the apache configuration file located at /etc/apache2/sites-enabled/000-default.conf, add the following block just after the DocumentRoot /var/www/html line:
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi
<Directory flaskapp>
    WSGIProcessGroup flaskapp
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>