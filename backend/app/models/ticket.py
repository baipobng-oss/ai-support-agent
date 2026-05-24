from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from app.db.database import Base

class Ticket(Base):

    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    subject = Column(String)

    message = Column(Text)

    status = Column(String)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )