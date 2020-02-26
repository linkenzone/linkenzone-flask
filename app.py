from flask import Flask
from configmodule.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def hello_world():
    print(app.config['WWW'])
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

