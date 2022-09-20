from app import db
import email
from app import mail_connect
from app import config
def commit_database(msg,i,ecom):
    body = ""
    for email_part in msg.get_payload():
        body += str(email_part)
    mail_connect.mail.copy(str(i),config.TRANSACTION_DIR)
    db.curr.execute(db.insert_email_id,(str(i),config.EMAIL,ecom[0],ecom,str(msg['subject']), body,"bcc","cc"))
    db.conn.commit()

def check_transaction(first_uid,last_uid):
    for i in range(first_uid,last_uid):
        try:
            type,data=mail_connect.mail.fetch(str(i),'(RFC822)') 
            for response_part in data:
                if isinstance(response_part,tuple):
                    msg=email.message_from_bytes(response_part[1])
                    email_from=email.utils.parseaddr(msg['from'])
                    transcational_sites = ["Amazon", "Flipkart"]
                    for name in transcational_sites:
                        if name in email_from:
                            commit_database(msg,i,email_from)  
                    db.curr.execute(db.update_last_id,(str(i)))
                    db.conn.commit()
        except Exception as e:
            print(e) 
