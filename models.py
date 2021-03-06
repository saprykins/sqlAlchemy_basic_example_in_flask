from database import session #
from sqlalchemy import Column, Integer, String
from database import Base
from database import init_db

"""
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'
"""


class Pdf(Base):
    __tablename__ = 'pdfs'

    id = Column(Integer, primary_key=True)
    author = Column(String)
    creation_date = Column(String)
    modification_date = Column(String)
    creator = Column(String)
    status = Column(String)
    text = Column(String)

    def __repr__(self):
        return "<Pdf(author='%s', creation_date='%s', modification_date='%s', creator='%s', status='%s', text='%s')>" % (
            self.author, self.creation_date, self.modification_date, self.creator, self.status, self.text)

init_db()


def get_doc_text_in_dictionary():
    file_path = 'C:\_My_Files\_FA\_ETUDES\Python\py-code\sqlAlchemy_basic_example_in_python\carhovchadjijffq_text.txt'
    with open(file_path) as feed:
        text = feed.read()
        # doc_text_in_dictionary = {"text": text, }
        return text


msg_f = get_doc_text_in_dictionary()


session.add_all([
    Pdf(author='wendy', creation_date='Wendy Williams',
        modification_date='windy', creator='me', status='ok', text='bla'),
    Pdf(author='mary', creation_date='Mary Contrary',
        modification_date='mary', creator='me', status='ok', text=msg_f),
    Pdf(author='fred', creation_date='Fred Flintstone',
        modification_date='freddy', creator='me', status='ok', text='bla')
])
session.commit()

our_pdf = session.query(Pdf).filter_by(author='fred').first()
print(our_pdf.creation_date)

"""
u = User('admin', 'admin@localhost')
session.add(u)
session.commit()
User.query.all()
"""
