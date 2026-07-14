# pgAdmin Guide

## What it does
pgAdmin provides a graphical interface for PostgreSQL.

## How to connect to the PostgreSQL server

1. Open pgAdmin in your browser.
2. In the left panel, right-click Servers and choose Register -> Server.
3. In the General tab, give the server a name such as Local ETL Postgres.
4. In the Connection tab, enter these values:
   - Host name/address: localhost
   - Port: 55432
   - Maintenance database: sales_db
   - Username: postgres
   - Password: mysecretpassword
5. Click Save.
6. The server will appear in the left panel, and you can expand it to view the database and tables.

## Connection details summary
- Host: localhost
- Port: 55432
- Database: sales_db
- User: postgres
- Password: mysecretpassword
