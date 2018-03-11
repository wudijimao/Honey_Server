from base.config import DevConfig
from base.app import app
from base.basemodel import db


app.config.from_object(DevConfig)

@app.route('/')
def home():
    return "Hello World"

@app.route('/register')
def register():
    return "Hello World"

if __name__ == "__main__":
    db.create_all()
    app.run()