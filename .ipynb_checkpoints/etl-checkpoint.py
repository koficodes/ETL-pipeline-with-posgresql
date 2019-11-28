import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from datetime import datetime


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id','title','artist_id','year','duration']]
    for i, row in song_data.iterrows():
        cur.execute(song_table_insert, list(row))
    
    # insert artist record
    artist_data = df[['artist_id','artist_name','artist_location','artist_latitude','artist_longitude']]
    for i, row in artist_data.iterrows():
        cur.execute(artist_table_insert, list(row))


def process_log_file(cur, filepath):
    # open log file
    df =  pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    df['ts'] = df['ts'].apply(lambda x: datetime.fromtimestamp(x/1000.0) ) #convert millisecond to seconds before transforming to datetinme
    df['start_time'] = df['ts'].apply(lambda x: x.strftime('%Y-%M-%d %H:%M:%S') )
    df['hour'] = df['ts'].apply(lambda x: x.hour )
    df['day'] = df['ts'].apply(lambda x: x.day )
    df['week'] = df['ts'].apply(lambda x: x.isocalendar()[1] )
    df['month'] = df['ts'].apply(lambda x: x.month )
    df['year'] = df['ts'].apply(lambda x: x.year )
    df['weekday'] = df['ts'].apply(lambda x: x.weekday() )

    # insert time data records
    #     time_data = 
    #     column_labels = 
    
    time_df =  df[['userId','start_time','hour','day','week','month','year','weekday']]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId','firstName','lastName','gender','level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        # insert songplay record
        songplay_data = (row.start_time,row.userId,row.level,songid,artistid,row.sessionId,row.location,row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()