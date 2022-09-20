import pymysql
from app import config

conn = pymysql.connect(host=config.HOST,db=config.DB_NAME,user=config.DB_USER,password=config.DB_PASSWORD)
curr = conn.cursor()
last_id_insert = """insert into last_id (uuid) values (%s) """
get_last_id="""select * from last_id limit 1"""
insert_email_id = """insert into `email_store` (uuid,email,site,sender,subject,
            body, bcc, cc)
            values (%s, %s, %s, %s, %s, %s,%s,%s) 
         """
update_last_id = """update`last_id` set uuid = %s"""