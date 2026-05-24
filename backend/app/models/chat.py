from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from app.db.database import Base

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id = Column(String)

    message = Column(Text)

    response = Column(Text)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )