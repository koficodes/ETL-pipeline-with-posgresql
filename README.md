## ETL PIPELINE WITH POSTGRESQL
#### INTRODUCTION
The purpose of this project is to create an ETL pipeline for the analysis of user activity of a music streaming app called sparkify.
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.
This project creates an ETL pipeline to fetch the data and then creates a database with a star schema in which the data is organized and saved for analysis.

#### DATABASE SCHEMA
The *star schema* is used for the database with `songplays` as the **fact table** and `users, songs, artists and time` as **dimension tables**

### HOW TO RUN THIS PROJECT

#### Required Python Packages

 - *pandas*
 - *psycopg2*

> NOTE: Consider using a virtual envronment.

#### FILES

 - `create_tables.py :` contains code for dropping and creating database tables.
 - `etl.ipnyb` notebook for trying out the ETL process.
 - `etl.py` contains code to run the entire ETL process
 - `test.ipynb` test the ETL process to make sure the tables are populated
 - `sql_queries.py`  contains the SQL queries need for this ETL project

#### STARTUP
Make sure you have PostgreSQL and all the required packages installed on your machine. Edit the `create_tables.py` file to enter your database details.
From the project directory run the following command:

    $ python3 create_tables.py
    $ python3 etl.py
