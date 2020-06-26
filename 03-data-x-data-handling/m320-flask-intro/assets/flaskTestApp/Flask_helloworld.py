## -------------------------------------------------------------------- ##
# Import Flask Class
from flask import Flask

# create instance of class '__name__' since we are using a single module
app = Flask(__name__)

## routing binds urls to functions via decorators ##
@app.route('/')
def hello_world():
    return 'Hello World!'
## -------------------------------------------------------------------- ##