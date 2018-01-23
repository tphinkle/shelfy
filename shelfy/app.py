'''
INCLUDE THIS IF RUNNING VIA
flask run (or, through compile.sh)
'''

# Imports
import flask
import os
from werkzeug.utils import secure_filename    # Needed for image upload
import sys
import shelfy


# Configure app
app = flask.Flask(__name__)





app.config.from_object(__name__) # Load config from thsie file (permit_generator.py)

app.config.update(dict(
SECRET_KEY = 'key',
USERNAME = 'admin',
PASSWORD = 'default'
))


# Register view blueprints
import shelfy.views
app.register_blueprint(shelfy.views.views)







'''
ONLY INCLUDE THIS IF RUNNING VIA
python shelfy.py
'''
'''
# Imports
import flask
import os
from werkzeug.utils import secure_filename    # Needed for image upload


# Flask location


# Base path for project
SHELFY_BASE_PATH = os.path.dirname(__file__)



# Configure app
app = flask.Flask(__name__)





app.config.from_object(__name__) # Load config from thsie file (permit_generator.py)

app.config.update(dict(
SECRET_KEY = 'key',
USERNAME = 'admin',
PASSWORD = 'default'
))





# Register view blueprints

import views


app.register_blueprint(views.views)


if __name__ == 'main':
    app.run(host='0.0.0.0', port=80)'''