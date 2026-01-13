from flask import Flask,Blueprint
from auth import auth
from admin import admin
from users import users
import os
from dotenv import load_dotenv
from database.db import initialize_db

load_dotenv()

app = Flask(__name__)
app.secret_key=os.getenv('secret_key')
        
app.config['SESSION_PERMANENT']=False 
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(users)
initialize_db()  



if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True,host='0.0.0.0')

