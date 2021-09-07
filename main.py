from project import db, create_app
import os
db.create_all(app=create_app()) # pass the create_app result so Flask-SQLAlchemy gets the configuration.
os.system('cmd /k "set FLASK_APP=project"')
os.system('cmd /c "set FLASK_DEBUG=1"')
