from database import init_db
from flask import Flask
from database import db_session
# from database import init_db
# from models import User

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


"""
init_db()
u = User('admin', 'admin@localhost')
db_session.add(u)
db_session.commit()
User.query.all()
"""

if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
