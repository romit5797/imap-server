from app import app
import time
from app import db
from app import mail_connect
from app import transaction
from app import config

@app.route("/")
def initialSync():
    db.curr.execute(db.get_last_id)
    check_dir = db.curr.fetchone()
    if check_dir is None:
        mail_connect.mail.create(config.TRANSACTION_DIR)
        db.curr.execute(db.last_id_insert,str(1))
        db.conn.commit()
    while True:
        mail_connect.mail.select(config.MAIL_BOX, readonly=True)
        result, data = mail_connect.mail.uid('search', None, "ALL") # search and return uids instead
        ids = data[0] # data is a list.
        id_list = ids.split() # ids is a space separated string
        db.curr.execute(db.get_last_id)
        last_uid = db.curr.fetchone()[0]
        db.conn.commit()
        if id_list[-1] != last_uid:
            transaction.check_transaction(int(last_uid),  int(id_list[-1]))
        time.sleep(120) # poll for new email every 2 mins