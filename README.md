# CHATGPT BB
https://chatgpt.com/share/6a0feea9-464c-83ec-9387-c4c53abf1664
AI Customer Support Agent(Production MVP / SaaS Architecture)
mkdir ai-support-agent
cd ai-support-agent
mkdir backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

SaaS Folder Structure
ai-support-agent/
│
├── frontend/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── services/
│   │   ├── ai/
│   │   ├── models/
│   │   ├── workers/
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── .env

Backend Requirements
requirements.txt
pip install -r requirements.txt

ENV Variables
.env

# INSTALL POSTGRESQL
PostgreSQL Setup(ref)
PS C:\Users\carol\ai-outreach-platform> psql -U postgres -h localhost

Password for user postgres:postgres

psql (17.9)

postgres=# CREATE DATABASE ai_outreach;

Result:
CREATE DATABASE

Verify Database Exists
Type:
\l

You will see something like:

List of databases
   Name
-------------------
 ai_outreach
 postgres
 template0
 template1


Connect To The Database
Type:
C:\Users\carol\ai-outreach-platform> psql -U postgres -h localhost
Password for user postgres:postgres
postgres=#\c ai_outreach

Result:
You are now connected to database "ai_outreach"

Prompt changes to:
ai_outreach=#
Create Tables

Example:
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    company VARCHAR(255),
    email VARCHAR(255),
    niche VARCHAR(100)
);
See Tables
\dt
Exit PostgreSQL
\q

Create database:
CREATE DATABASE roofing_ai;

# Load ENV Variables & test
pip install python-dotenv
backend/test_env.py
python test_env.py

# OUTPUT
![alt text](<Screenshot (221).png>)
-----------------------------

FastAPI Main App
app/main.py

AI Chat Endpoint
app/api/chat.py

LangChain Support Agent
app/ai/support_chain.py

Shopify Order Lookup
app/api/shopify.py

PDF Training System
app/services/pdf_loader.py

Vector Database Upload
app/services/vector_store.py

RAG Retrieval
app/ai/rag_chat.py

Ticket Classification
app/services/ticket_classifier.py

Human Escalation
app/services/escalation.py

Slack Integration
app/services/slack_notify.py

Combine Everything
app/api/support.py

Frontend Chat UI
frontend/src/App.jsx

create Frontend
npm create vite@latest frontend
React
Variant:
JavaScript
cd frontend
npm install
npm run dev

# Run Backend
uvicorn app.main:app --reload
Run Frontend
npm run dev

# fix problem
pip install langchain-core langchain-openai
python -m uvicorn app.main:app --reload
npm install tailwindcss @tailwindcss/vite

# Test Tailwind
npm run dev
Replace App.jsx temporarily:
export default function App() {
  return (
    <div className="bg-black text-white p-10 text-4xl">
      Tailwind Works
    </div>
  )
}
If screen becomes black with white text → fixed.
# OUTPUT
![alt text](<Screenshot (222).png>)
![alt text](<Screenshot (224).png>)
![alt text](<Screenshot (223).png>)

# --------------------------------------------------
# --------------------------------------------------

#  Real SaaS Upgrades code

1. JWT Authentication
Install
pip install python-jose passlib[bcrypt] python-multipart

Create Auth Utilities
backend/app/core/security.py

User Model
backend/app/models/user.py

Register/Login API
backend/app/api/auth.py

Add Router
backend/app/main.py

2. Conversation Memory
Chat History Model
backend/app/models/chat.py

Save Conversations
backend/app/services/chat_memory.py

3. Stripe SaaS Billing
Install
pip install stripe
backend/app/services/stripe_service.py

Billing API
backend/app/api/billing.py

4. Multi-Tenant SaaS
Each company gets isolated data.
Organization Model
backend/app/models/organization.py
Add organization_id Everywhere
backend/app/models/organization.py
backend/app/models/user.py
backend/app/models/chat.py
backend/app/models/document.py
backend/app/models/ticket.py
backend/create_db.py
Delete:
backend/support.db
Recreate Database
Inside backend:
# python create_db.py
# OUTPUT 
[text](backend/support.db)

Expected:
Database created
Create Document Model
Example:
organization_id = Column(Integer)
Add organization_id To User Table

5. AI Ticket Routing
Automatically route tickets.
backend/app/services/router.py

6. AI Suggested Replies
backend/app/services/reply_generator.py

7. Admin Dashboard Metrics
backend/app/api/analytics.py

8. Usage Limits
backend/app/services/usage.py

9. Human Handoff System
backend/app/services/handoff.py

10. Production Database Setup
backend/app/db/database.py
Create Tables
backend/create_db.py

11. Production Deployment
Backend
Deploy to:
Railway
Render
Frontend
Deploy to:
Vercel

12. SaaS Features That Increase Value
Add:
Team inbox
AI confidence score
AI auto-close tickets
AI voice support
WhatsApp integration
Gmail integration
Shopify app
CRM integration
Agent analytics
Customer sentiment tracking
AI workflow automation


# ----------------------------------------------------
# ---------------------------------------------------

# NEXT UPGRADE Production Deployment (Railway + Vercel)
Architecture:
Frontend (React/Vercel)
        ↓
Backend API (FastAPI/Railway)
        ↓
PostgreSQL/Supabase

PART 1 — Deploy Backend To Railway
STEP 1 — Create Procfile
backend/Procfile

STEP 2 — Create runtime.txt
backend/runtime.txt

STEP 3 — Update requirements.txt
Inside backend:
pip freeze > requirements.txt

STEP 4 — Add CORS
backend/app/main.py

STEP 6 — Push Code
Inside project root:
Connect GitHub:
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main

STEP 7 — Deploy Railway
Go to:
Railway Dashboard

Create Project
New Project
→ Deploy from GitHub repo
Select:
ai-support-agent

You accidentally mixed Tailwind v3 + Tailwind v4 setup.

Simplest fix: remove PostCSS config completely.

FIX STEP-BY-STEP
1. Delete These Files

Inside frontend/ delete:

postcss.config.mjs

AND if exists:

tailwind.config.js

OR

tailwind.config.cjs
2. Install Correct Tailwind v4 Packages

Inside frontend terminal:

npm install tailwindcss @tailwindcss/vite
3. Replace vite.config.js
frontend/vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
})
4. Replace index.css
frontend/src/index.css
@import "tailwindcss";

ONLY that line.

5. Stop Vite Server

Press:

CTRL + C
6. Restart Frontend
npm run dev
7. Test Tailwind

Replace App.jsx temporarily:

export default function App() {
  return (
    <div className="bg-black text-white p-10 text-4xl">
      Tailwind Works
    </div>
  )
}

If screen becomes black with white text → fixed.

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\carol\ai-support-agent\backend\venv\Scripts\uvicorn.exe\__main__.py", line 7, in <module>
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 1524, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 1445, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 1308, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 877, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\main.py", line 441, in main
    run(
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\main.py", line 609, in run
    config.load_app()
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\config.py", line 415, in load_app
    return import_from_string(self.app)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\importer.py", line 22, in import_from_string
    raise exc from None
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Users\carol\ai-support-agent\backend\app\main.py", line 3, in <module>
    from app.api.chat import router as chat_router
  File "C:\Users\carol\ai-support-agent\backend\app\api\chat.py", line 3, in <module>
    from app.ai.support_chain import support_agent
  File "C:\Users\carol\ai-support-agent\backend\app\ai\support_chain.py", line 2, in <module>
    from langchain.prompts import ChatPromptTemplate
ModuleNotFoundError: No module named 'langchain.prompts'

You still have OLD code in:

backend/app/ai/support_chain.py

It STILL says:

from langchain.prompts import ChatPromptTemplate

You must REPLACE it.

OPEN THIS FILE
backend/app/ai/support_chain.py
DELETE EVERYTHING

Replace entire file with this:

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

SYSTEM_PROMPT = """
You are an AI customer support agent.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}")
])

chain = prompt | llm

def support_agent(message: str):

    result = chain.invoke({
        "input": message
    })

    return result.content
IMPORTANT

The correct import is:

from langchain_core.prompts import ChatPromptTemplate

NOT:

from langchain.prompts import ChatPromptTemplate
THEN INSTALL

Inside backend terminal:

pip install langchain-core langchain-openai
THEN RUN
python -m uvicorn app.main:app --reload
QUICK CHECK

You can verify file saved correctly:

type app\ai\support_chain.py

If terminal still shows:

from langchain.prompts

then file was NOT saved correctly.

Real SaaS Upgrades code
Production SaaS Upgrades (Real Architecture + Code)

These upgrades turn your AI support chatbot into an actual SaaS product.

1. JWT Authentication
Install

Inside backend:

pip install python-jose passlib[bcrypt] python-multipart
Create Auth Utilities
backend/app/core/security.py
from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = "SUPER_SECRET_KEY"

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):

    return pwd_context.hash(password)

def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=7)

    to_encode.update({
        "exp": expire
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
User Model
backend/app/models/user.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    email = Column(
        String,
        unique=True
    )

    password = Column(String)
Register/Login API
backend/app/api/auth.py
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(prefix="/auth")

fake_db = {}

class AuthRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(req: AuthRequest):

    fake_db[req.email] = hash_password(
        req.password
    )

    return {
        "message": "User created"
    }

@router.post("/login")
def login(req: AuthRequest):

    hashed = fake_db.get(req.email)

    if not hashed:
        return {
            "error": "User not found"
        }

    valid = verify_password(
        req.password,
        hashed
    )

    if not valid:
        return {
            "error": "Invalid password"
        }

    token = create_access_token({
        "sub": req.email
    })

    return {
        "access_token": token
    }
Add Router
backend/app/main.py
from app.api.auth import router as auth_router

app.include_router(auth_router)
2. Conversation Memory
Chat History Model
backend/app/models/chat.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.db.database import Base

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True
    )

    customer_id = Column(String)

    message = Column(Text)

    response = Column(Text)
Save Conversations
backend/app/services/chat_memory.py
memory_store = []

def save_chat(
    customer_id,
    message,
    response
):

    memory_store.append({
        "customer_id": customer_id,
        "message": message,
        "response": response
    })

def get_history(customer_id):

    history = []

    for item in memory_store:

        if item["customer_id"] == customer_id:
            history.append(item)

    return history
3. Stripe SaaS Billing
Install
pip install stripe
backend/app/services/stripe_service.py
import stripe

stripe.api_key = "YOUR_STRIPE_SECRET"

def create_checkout():

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],

        line_items=[
            {
                "price": "price_xxxxx",
                "quantity": 1
            }
        ],

        mode="subscription",

        success_url=
        "http://localhost:5173/success",

        cancel_url=
        "http://localhost:5173/cancel"
    )

    return session.url
Billing API
backend/app/api/billing.py
from fastapi import APIRouter

from app.services.stripe_service import (
    create_checkout
)

router = APIRouter(prefix="/billing")

@router.get("/checkout")
def checkout():

    url = create_checkout()

    return {
        "checkout_url": url
    }
4. Multi-Tenant SaaS

Each company gets isolated data.

Organization Model
backend/app/models/organization.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base

class Organization(Base):

    __tablename__ = "organizations"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    plan = Column(String)
Add organization_id Everywhere

Example:

organization_id = Column(Integer)

Tables:

users
chats
documents
tickets
5. AI Ticket Routing

Automatically route tickets.

backend/app/services/router.py
def route_ticket(category):

    if category == "refund":
        return "billing-team"

    if category == "technical":
        return "engineering"

    if category == "shipping":
        return "logistics"

    return "general-support"
6. AI Suggested Replies
backend/app/services/reply_generator.py
from openai import OpenAI

client = OpenAI()

def generate_reply(ticket):

    prompt = f"""
    Write a professional support reply.

    Ticket:
    {ticket}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
7. Admin Dashboard Metrics
backend/app/api/analytics.py
from fastapi import APIRouter

router = APIRouter(prefix="/analytics")

@router.get("/")
def analytics():

    return {

        "tickets_today": 152,

        "ai_resolved": 124,

        "human_escalations": 28,

        "avg_response_time": "12 sec"
    }
8. Usage Limits
backend/app/services/usage.py
usage = {}

LIMIT = 500

def check_limit(user_id):

    current = usage.get(user_id, 0)

    if current >= LIMIT:
        return False

    usage[user_id] = current + 1

    return True
9. Human Handoff System
backend/app/services/handoff.py
def handoff_to_human(ticket):

    return {
        "status": "queued",
        "assigned_to": "support-agent-1"
    }
10. Production Database Setup
backend/app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///./support.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
Create Tables
backend/create_db.py
from app.db.database import Base
from app.db.database import engine

from app.models.user import User
from app.models.chat import ChatHistory
from app.models.organization import Organization

Base.metadata.create_all(bind=engine)

print("Database created")

Run:

python create_db.py
11. Production Deployment
Backend

Deploy to:

Railway
Render
Frontend

Deploy to:

Vercel
12. SaaS Features That Increase Value
Add:
Team inbox
AI confidence score
AI auto-close tickets
AI voice support
WhatsApp integration
Gmail integration
Shopify app
CRM integration
Agent analytics
Customer sentiment tracking
AI workflow automation
Real SaaS Roadmap
Phase 1
Chatbot
RAG
PDF upload
Support AI
Phase 2
Billing
Auth
Teams
Dashboard
Phase 3
AI agents
Tool calling
Voice AI
Omnichannel support
High-Income Niches

Best industries:

Ecommerce
Clinics
Legal firms
SaaS startups
Agencies
Real estate
Education
Insurance
Add organization_id Everywhere

Example:

organization_id = Column(Integer)

Tables:

users
chats
documents
tickets                        HOW TO DO THAT?
Goal

Each company/account gets its own isolated data.

Example:

Company A cannot see Company B chats
Company A documents stay private
Company A tickets separated

This is called multi-tenant SaaS.

STEP 1 — Create Organization Model
backend/app/models/organization.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base

class Organization(Base):

    __tablename__ = "organizations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    plan = Column(String)
STEP 2 — Add organization_id To User Table
backend/app/models/user.py

Replace with:

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String,
        unique=True
    )

    password = Column(String)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )
STEP 3 — Add organization_id To Chat Table
backend/app/models/chat.py
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
STEP 4 — Create Document Model
backend/app/models/document.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base

class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(String)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )
STEP 5 — Create Ticket Model
backend/app/models/ticket.py
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
STEP 6 — Import Models In create_db.py
backend/create_db.py
from app.db.database import Base
from app.db.database import engine

from app.models.user import User
from app.models.chat import ChatHistory
from app.models.organization import Organization
from app.models.document import Document
from app.models.ticket import Ticket

Base.metadata.create_all(bind=engine)

print("Database created")
STEP 7 — Delete Old Database

If using SQLite:

Delete:

backend/support.db

because schema changed.

STEP 8 — Recreate Database

Inside backend:

python create_db.py

Expected:

Database created
STEP 9 — Confirm Tables

You should now have tables:

organizations
users
chat_history
documents
tickets
HOW MULTI-TENANT FILTERING WORKS

Example:

organization_id = 1

When querying chats:

db.query(ChatHistory).filter(
    ChatHistory.organization_id == 1
)

This ensures only that company's data appears.

Example Chat Save
new_chat = ChatHistory(
    customer_id="123",
    message="Hello",
    response="Hi there",
    organization_id=1
)
Real SaaS Flow
Organization
Nike
ID = 1
Users
admin@nike.com
support@nike.com

Both:

organization_id = 1
Why This Matters

Without organization_id:

❌ All customer data mixed together.

With organization_id:

✅ Secure SaaS isolation.

Critical for:

Stripe billing
Teams
Dashboards
Permissions
Enterprise SaaS
GDPR/security compliance
NEXT UPGRADE Production Deployment
Backend
Railway
Frontend
Vercel              CODE?
Production Deployment (Railway + Vercel)

Architecture:

Frontend (React/Vercel)
        ↓
Backend API (FastAPI/Railway)
        ↓
PostgreSQL/Supabase
PART 1 — Deploy Backend To Railway
STEP 1 — Create Procfile
backend/Procfile
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT

NO .txt

File name must be exactly:

Procfile
STEP 2 — Create runtime.txt
backend/runtime.txt
python-3.11.9
STEP 3 — Update requirements.txt

Inside backend:

pip freeze > requirements.txt
STEP 4 — Add CORS
backend/app/main.py

Replace with:

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "AI Support Agent Running"
    }
STEP 5 — Create GitHub Repo

Go to:

GitHub

Create repo:

ai-support-agent
STEP 6 — Push Code

Inside project root:

git init
git add .
git commit -m "initial commit"

Connect GitHub:
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main

STEP 7 — Deploy Railway
Go to:
Railway Dashboard

Create Project
New Project
→ Deploy from GitHub repo

Select:
ai-support-agent

IMPORTANT
Set Root Directory:

backend
Railway must deploy backend folder only.

STEP 8 — Add ENV Variables

STEP 9 — Deploy
Railway auto-builds.
Expected:
Deployment successful

STEP 10 — Get Backend URL
Example:
https://ai-support-agent-production.up.railway.app
Save this.

PART 2 — Deploy Frontend To Vercel
STEP 1 — Add Production API URL
frontend/.env
VITE_API_URL=https://YOUR-RAILWAY-URL.up.railway.app

STEP 2 — Update App.jsx
Replace fetch URL.

STEP 3 — Push Changes
git add .
git commit -m "production deployment"
git push

STEP 4 — Deploy Vercel
Go to:
Vercel Dashboard
Import Project
Add New
→ Project
→ Import GitHub Repo
Select:
ai-support-agent

STEP 5 — Add Frontend ENV Variable
Vercel:

STEP 6 — Deploy
Click:
Deploy

FINAL RESULT
Frontend
Example:
https://ai-support-agent.vercel.app
Backend
Example:
https://ai-support-agent-production.up.railway.app

You accidentally mixed Tailwind v3 + Tailwind v4 setup.

Simplest fix: remove PostCSS config completely.

FIX STEP-BY-STEP
1. Delete These Files

Inside frontend/ delete:

postcss.config.mjs

AND if exists:

tailwind.config.js

OR

tailwind.config.cjs
2. Install Correct Tailwind v4 Packages

Inside frontend terminal:

npm install tailwindcss @tailwindcss/vite
3. Replace vite.config.js
frontend/vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
})
4. Replace index.css
frontend/src/index.css
@import "tailwindcss";

ONLY that line.

5. Stop Vite Server

Press:

CTRL + C
6. Restart Frontend
npm run dev
7. Test Tailwind

Replace App.jsx temporarily:

export default function App() {
  return (
    <div className="bg-black text-white p-10 text-4xl">
      Tailwind Works
    </div>
  )
}

If screen becomes black with white text → fixed.

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\carol\ai-support-agent\backend\venv\Scripts\uvicorn.exe\__main__.py", line 7, in <module>
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 1524, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 1445, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 1308, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\click\core.py", line 877, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\main.py", line 441, in main
    run(
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\main.py", line 609, in run
    config.load_app()
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\config.py", line 415, in load_app
    return import_from_string(self.app)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\importer.py", line 22, in import_from_string
    raise exc from None
  File "C:\Users\carol\ai-support-agent\backend\venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1147, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "C:\Users\carol\ai-support-agent\backend\app\main.py", line 3, in <module>
    from app.api.chat import router as chat_router
  File "C:\Users\carol\ai-support-agent\backend\app\api\chat.py", line 3, in <module>
    from app.ai.support_chain import support_agent
  File "C:\Users\carol\ai-support-agent\backend\app\ai\support_chain.py", line 2, in <module>
    from langchain.prompts import ChatPromptTemplate
ModuleNotFoundError: No module named 'langchain.prompts'

You still have OLD code in:

backend/app/ai/support_chain.py

It STILL says:

from langchain.prompts import ChatPromptTemplate

You must REPLACE it.

OPEN THIS FILE
backend/app/ai/support_chain.py
DELETE EVERYTHING

Replace entire file with this:

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

SYSTEM_PROMPT = """
You are an AI customer support agent.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}")
])

chain = prompt | llm

def support_agent(message: str):

    result = chain.invoke({
        "input": message
    })

    return result.content
IMPORTANT

The correct import is:

from langchain_core.prompts import ChatPromptTemplate

NOT:

from langchain.prompts import ChatPromptTemplate
THEN INSTALL

Inside backend terminal:

pip install langchain-core langchain-openai
THEN RUN
python -m uvicorn app.main:app --reload
QUICK CHECK

You can verify file saved correctly:

type app\ai\support_chain.py

If terminal still shows:

from langchain.prompts

then file was NOT saved correctly.

Real SaaS Upgrades code
Production SaaS Upgrades (Real Architecture + Code)

These upgrades turn your AI support chatbot into an actual SaaS product.

1. JWT Authentication
Install

Inside backend:

pip install python-jose passlib[bcrypt] python-multipart
Create Auth Utilities
backend/app/core/security.py
from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = "SUPER_SECRET_KEY"

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):

    return pwd_context.hash(password)

def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(days=7)

    to_encode.update({
        "exp": expire
    })

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
User Model
backend/app/models/user.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    email = Column(
        String,
        unique=True
    )

    password = Column(String)
Register/Login API
backend/app/api/auth.py
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(prefix="/auth")

fake_db = {}

class AuthRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(req: AuthRequest):

    fake_db[req.email] = hash_password(
        req.password
    )

    return {
        "message": "User created"
    }

@router.post("/login")
def login(req: AuthRequest):

    hashed = fake_db.get(req.email)

    if not hashed:
        return {
            "error": "User not found"
        }

    valid = verify_password(
        req.password,
        hashed
    )

    if not valid:
        return {
            "error": "Invalid password"
        }

    token = create_access_token({
        "sub": req.email
    })

    return {
        "access_token": token
    }
Add Router
backend/app/main.py
from app.api.auth import router as auth_router

app.include_router(auth_router)
2. Conversation Memory
Chat History Model
backend/app/models/chat.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.db.database import Base

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        Integer,
        primary_key=True
    )

    customer_id = Column(String)

    message = Column(Text)

    response = Column(Text)
Save Conversations
backend/app/services/chat_memory.py
memory_store = []

def save_chat(
    customer_id,
    message,
    response
):

    memory_store.append({
        "customer_id": customer_id,
        "message": message,
        "response": response
    })

def get_history(customer_id):

    history = []

    for item in memory_store:

        if item["customer_id"] == customer_id:
            history.append(item)

    return history
3. Stripe SaaS Billing
Install
pip install stripe
backend/app/services/stripe_service.py
import stripe

stripe.api_key = "YOUR_STRIPE_SECRET"

def create_checkout():

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],

        line_items=[
            {
                "price": "price_xxxxx",
                "quantity": 1
            }
        ],

        mode="subscription",

        success_url=
        "http://localhost:5173/success",

        cancel_url=
        "http://localhost:5173/cancel"
    )

    return session.url
Billing API
backend/app/api/billing.py
from fastapi import APIRouter

from app.services.stripe_service import (
    create_checkout
)

router = APIRouter(prefix="/billing")

@router.get("/checkout")
def checkout():

    url = create_checkout()

    return {
        "checkout_url": url
    }
4. Multi-Tenant SaaS

Each company gets isolated data.

Organization Model
backend/app/models/organization.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base

class Organization(Base):

    __tablename__ = "organizations"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    plan = Column(String)
Add organization_id Everywhere

Example:

organization_id = Column(Integer)

Tables:

users
chats
documents
tickets
5. AI Ticket Routing

Automatically route tickets.

backend/app/services/router.py
def route_ticket(category):

    if category == "refund":
        return "billing-team"

    if category == "technical":
        return "engineering"

    if category == "shipping":
        return "logistics"

    return "general-support"
6. AI Suggested Replies
backend/app/services/reply_generator.py
from openai import OpenAI

client = OpenAI()

def generate_reply(ticket):

    prompt = f"""
    Write a professional support reply.

    Ticket:
    {ticket}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
7. Admin Dashboard Metrics
backend/app/api/analytics.py
from fastapi import APIRouter

router = APIRouter(prefix="/analytics")

@router.get("/")
def analytics():

    return {

        "tickets_today": 152,

        "ai_resolved": 124,

        "human_escalations": 28,

        "avg_response_time": "12 sec"
    }
8. Usage Limits
backend/app/services/usage.py
usage = {}

LIMIT = 500

def check_limit(user_id):

    current = usage.get(user_id, 0)

    if current >= LIMIT:
        return False

    usage[user_id] = current + 1

    return True
9. Human Handoff System
backend/app/services/handoff.py
def handoff_to_human(ticket):

    return {
        "status": "queued",
        "assigned_to": "support-agent-1"
    }
10. Production Database Setup
backend/app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///./support.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
Create Tables
backend/create_db.py
from app.db.database import Base
from app.db.database import engine

from app.models.user import User
from app.models.chat import ChatHistory
from app.models.organization import Organization

Base.metadata.create_all(bind=engine)

print("Database created")

Run:

python create_db.py
11. Production Deployment
Backend

Deploy to:

Railway
Render
Frontend

Deploy to:

Vercel
12. SaaS Features That Increase Value
Add:
Team inbox
AI confidence score
AI auto-close tickets
AI voice support
WhatsApp integration
Gmail integration
Shopify app
CRM integration
Agent analytics
Customer sentiment tracking
AI workflow automation
Real SaaS Roadmap
Phase 1
Chatbot
RAG
PDF upload
Support AI
Phase 2
Billing
Auth
Teams
Dashboard
Phase 3
AI agents
Tool calling
Voice AI
Omnichannel support
High-Income Niches

Best industries:

Ecommerce
Clinics
Legal firms
SaaS startups
Agencies
Real estate
Education
Insurance
Add organization_id Everywhere

Example:

organization_id = Column(Integer)

Tables:

users
chats
documents
tickets                        HOW TO DO THAT?
Goal

Each company/account gets its own isolated data.

Example:

Company A cannot see Company B chats
Company A documents stay private
Company A tickets separated

This is called multi-tenant SaaS.

STEP 1 — Create Organization Model
backend/app/models/organization.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.database import Base

class Organization(Base):

    __tablename__ = "organizations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    plan = Column(String)
STEP 2 — Add organization_id To User Table
backend/app/models/user.py

Replace with:

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String,
        unique=True
    )

    password = Column(String)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )
STEP 3 — Add organization_id To Chat Table
backend/app/models/chat.py
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
STEP 4 — Create Document Model
backend/app/models/document.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base

class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(String)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )
STEP 5 — Create Ticket Model
backend/app/models/ticket.py
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
STEP 6 — Import Models In create_db.py
backend/create_db.py
from app.db.database import Base
from app.db.database import engine

from app.models.user import User
from app.models.chat import ChatHistory
from app.models.organization import Organization
from app.models.document import Document
from app.models.ticket import Ticket

Base.metadata.create_all(bind=engine)

print("Database created")
STEP 7 — Delete Old Database

If using SQLite:

Delete:

backend/support.db

because schema changed.

STEP 8 — Recreate Database

Inside backend:

python create_db.py

Expected:

Database created
STEP 9 — Confirm Tables

You should now have tables:

organizations
users
chat_history
documents
tickets
HOW MULTI-TENANT FILTERING WORKS

Example:

organization_id = 1

When querying chats:

db.query(ChatHistory).filter(
    ChatHistory.organization_id == 1
)

This ensures only that company's data appears.

Example Chat Save
new_chat = ChatHistory(
    customer_id="123",
    message="Hello",
    response="Hi there",
    organization_id=1
)
Real SaaS Flow
Organization
Nike
ID = 1
Users
admin@nike.com
support@nike.com

Both:

organization_id = 1
Why This Matters

Without organization_id:

❌ All customer data mixed together.

With organization_id:

✅ Secure SaaS isolation.

Critical for:

Stripe billing
Teams
Dashboards
Permissions
Enterprise SaaS
GDPR/security compliance
NEXT UPGRADE Production Deployment
Backend
Railway
Frontend
Vercel              CODE?
Production Deployment (Railway + Vercel)

Architecture:

Frontend (React/Vercel)
        ↓
Backend API (FastAPI/Railway)
        ↓
PostgreSQL/Supabase
PART 1 — Deploy Backend To Railway
STEP 1 — Create Procfile
backend/Procfile
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT

NO .txt

File name must be exactly:

Procfile
STEP 2 — Create runtime.txt
backend/runtime.txt
python-3.11.9
STEP 3 — Update requirements.txt

Inside backend:

pip freeze > requirements.txt
STEP 4 — Add CORS
backend/app/main.py

Replace with:

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "AI Support Agent Running"
    }
STEP 5 — Create GitHub Repo

Go to:

GitHub

Create repo:

ai-support-agent
STEP 6 — Push Code

Inside project root:

git init
git add .
git commit -m "initial commit"

Connect GitHub:

git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
STEP 7 — Deploy Railway

Go to:

Railway Dashboard

Create Project
New Project
→ Deploy from GitHub repo

Select:

ai-support-agent
IMPORTANT

Set Root Directory:

backend

Railway must deploy backend folder only.

STEP 8 — Add ENV Variables

Railway:

Project
→ Variables

Add:

OPENAI_API_KEY=

DATABASE_URL=

SUPABASE_URL=
SUPABASE_KEY=

SHOPIFY_STORE=
SHOPIFY_ACCESS_TOKEN=

SLACK_BOT_TOKEN=
SLACK_CHANNEL_ID=
STEP 9 — Deploy

Railway auto-builds.

Expected:

Deployment successful
STEP 10 — Get Backend URL

Example:

https://ai-support-agent-production.up.railway.app

Save this.

PART 2 — Deploy Frontend To Vercel
STEP 1 — Add Production API URL
frontend/.env
VITE_API_URL=https://YOUR-RAILWAY-URL.up.railway.app
STEP 2 — Update App.jsx

Replace fetch URL.

OLD:

http://localhost:8000/support/

NEW:

${import.meta.env.VITE_API_URL}/support/
Final Example
const res = await fetch(
  `${import.meta.env.VITE_API_URL}/support/`,
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message
    })
  }
)
STEP 3 — Push Changes
git add .
git commit -m "production deployment"
git push
STEP 4 — Deploy Vercel

Go to:

Vercel Dashboard

Import Project
Add New
→ Project
→ Import GitHub Repo

Select:

ai-support-agent
IMPORTANT

Set Root Directory:

frontend
STEP 5 — Add Frontend ENV Variable

Vercel:

Project Settings
→ Environment Variables

Add:

VITE_API_URL=https://YOUR-RAILWAY-URL.up.railway.app
STEP 6 — Deploy

Click:

Deploy
FINAL RESULT
Frontend
Example:
https://ai-support-agent.vercel.app
Backend
Example:
https://ai-support-agent-production.up.railway.app

TEST PRODUCTION
Production Improvements
Add Production Gunicorn
Install:
pip install gunicorn