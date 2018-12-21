"""app initializer """

import os

from api import create_app

config_name = os.getenv("APP_SETTINGS")

app = create_app(config_name)

@app.route('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()