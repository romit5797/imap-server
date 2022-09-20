import imaplib
from app import config

mail=imaplib.IMAP4_SSL(config.IMAP_SERVER)
mail.login(config.EMAIL, config.PASSWORD)
mail.select(config.MAIL_BOX)
type,data=mail.search(None,'ALL')
mail_ids=data[0]
