from database import init_db
from flask import Flask
from database import session

# from models import User

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()



if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
