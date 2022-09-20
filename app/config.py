import os
from dotenv import load_dotenv
load_dotenv()

EMAIL=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")
HOST=os.environ.get("HOST")
DB_NAME=os.environ.get("DB_NAME")
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_USER=os.environ.get("DB_USER")
IMAP_SERVER=os.environ.get("IMAP_SERVER")
TRANSACTION_DIR=os.environ.get("TRANSACTION_DIR")
MAIL_BOX=os.environ.get("MAIL_BOX")
