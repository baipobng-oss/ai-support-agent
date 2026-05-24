from app.db.database import Base
from app.db.database import engine

from app.models.user import User
from app.models.chat import ChatHistory
from app.models.organization import Organization
from app.models.document import Document
from app.models.ticket import Ticket

Base.metadata.create_all(bind=engine)

print("Database created")