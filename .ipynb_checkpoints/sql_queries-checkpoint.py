# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE  IF NOT EXISTS songplays(
    songplay_id serial PRIMARY KEY,
    start_time VARCHAR(100) NOT NULL,
    user_id INTEGER NOT NULL,
    level VARCHAR (50) NOT NULL,
    song_id VARCHAR(100),
    artist_id VARCHAR(100),
    session_id INTEGER NOT NULL,
    location VARCHAR(50),
    user_agent VARCHAR(255) NOT NULL
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER NOT NULL, 
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(1) NOT NULL,
    level VARCHAR(5) NOT NULL
);""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    artist_id VARCHAR(100) NOT NULL,
    year INTEGER NOT NULL,
    duration NUMERIC NOT NULL
);""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(50) NOT NULL,
    latitude VARCHAR(50) NOT NULL,
    longitude VARCHAR(50) NOT NULL
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time VARCHAR(100) NOT NULL ,
    hour INTEGER NOT NULL,
    day INTEGER NOT NULL,
    week INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    weekday INTEGER NOT NULL,
    user_id INTEGER NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
INSERT INTO users(user_id,first_name, last_name, gender, level)
VALUES (%s,%s,%s,%s,%s)
""")

song_table_insert = ("""
INSERT INTO songs(song_id,title,artist_id,year,duration)
VALUES (%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id,name, location, latitude, longitude)
VALUES(%s,%s,%s,%s,%s)
""")


time_table_insert = ("""
INSERT INTO time(user_id,start_time, hour, day, week, month, year, weekday)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = ("""SELECT song_id,artist_id FROM  songs WHERE title=%s AND duration=%s""")
# SELECT A.song_id,B.artist_id FROM (SELECT song_id FROM  songs WHERE title='%s' AND duration='%s') AS A ,(SELECT artist_id FROM  artists WHERE name='%s') AS B;
# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
