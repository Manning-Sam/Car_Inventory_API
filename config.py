import os
class Config():
    Flask_app = os.environ.get('flask_app')
    Flask_env = os.environ.get('Flask_env')
    