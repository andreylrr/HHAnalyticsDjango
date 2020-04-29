from sqlalchemy import Column, Integer, String, DateTime
from Helpers.ParserHHApi.parsers.database import Base
from datetime import datetime

class Request(Base):
    __tablename__ = "hhrequest_requests"

    id = Column(Integer, primary_key=True)
#    user_id = Column(Integer, ForeignKey("users.id"))
    region = Column(String(150))
    text_request = Column(String(150))
    file_name = Column(String(250))
    status = Column(Integer)
    created = Column(DateTime(), default=datetime.now)
    updated = Column(DateTime(), default=None)
    vacancy_number = Column(Integer)
#    user = relationship("User", backref="requests")

    def __init__(self, user_id=None, region=None, text_request=None, file_name=None, status=None,
                 created=None, updated=None, vacancy_number=None):
#        self.user_id = user_id
        self.region = region
        self.text_request = text_request
        self.file_name = file_name
        self.status = status
        self.created = created
        self.updated = updated
        self.vacancy_number = vacancy_number

    def __repr__(self):
        return f'Request {self.region} {self.text_request}'
