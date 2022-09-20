<!-- ABOUT THE PROJECT -->
## About The Project

This is a basic Flask based IMAP-Server.

### Built With

* [Python](https://www.python.org)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [MySQL](https://www.mysql.com)

### Prerequisites

* [Python](https://www.python.org/downloads/)

### Setup

1. Clone the github repo
   ```sh
   git clone https://github.com/romit5797/imap-server.git
   ```
2. Install Python packages
   ```sh
   cd imap-server &&  pip install -r requirements.txt
   ```
3. Set your config env file to store the application secrets
   ```sh
   touch .env
   ```
4. Create Schema in MySQLfor Linux/Unix/MacOS
   ```sh
   mysql -u root < ./app/sql/testdb.sql
   ```
5. Run the server
   ```sh
   export FLASK_APP=run.py && flask run
    ```
6. Access the api
   ```sh
   http://localhost:5000/

## Features

- Scrap the transactional emails from Amazon and Flipkart from your mailbox using IMAP.
- Store the scraped emails in a SQL database with an easily queryable schema.
- Also, scrape any transactional new emails from Amazon and Flipkart instantaneously and store them in the SQL database.
- Move all the Amazon and Flipkart transactional emails to a different label called
Ecom-Receipt in your mailbox
- Handle server restart or IMAP connection broken.

## Project structure

```bash
< PROJECT ROOT >
   |
   |-- app/
   |    |
   |    | -- config.py                     # App Configuration
   |    | -- db.py                         # Manage Database
   |    | -- mail_connect.py               # Connect to email service
   |    | -- transcation.py                # Find transcational emails  
   |    | -- views.py                      # App Routing
   |    | -- __init__.py                   # Bundle all above sections and expose the Flask APP 
   |    |
   |    |-- sql/
   |    |    |-- testdb.sql                # Create SQL schema
   |    |
   |    |-- static/                        # CSS files, Javascripts files, images
   |    |
   |    |-- templates/                     # HTML Pages
   |
   |-- requirements.txt                    # Application Dependencies
   |
   |-- run.py                              # Start the app in development and production
   |
   |-- ************************************************************************
```
