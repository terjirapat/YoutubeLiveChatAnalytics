

import config  # import user, pwd for connect mongodb from config.py
import pandas as pd
from datetime import datetime
import plotly.express as px
import pymongo
import pytchat
import googleapiclient.discovery
from dash import Dash, html, dcc
from thai_sentiment import get_sentiment
from pythainlp import word_tokenize # ?
from pythainlp.corpus.common import thai_stopwords # ?

########################################
#// TODO RESTRUCTURE
    #// TODO Class db connect
        #// TODO Change where db insert,read called
        # TODO Fetch live comment
        # TODO DB Insert live comment (maybe add more filed (vdo_type: live/clip)) to filter 2 kinds
        
        # TODO DB READ FUNCTION ( from create_df_comment() )
            # TODO CAST TO DF
        # TODO DATA_Processing (main function to calling DB_READ())
        # TODO 
    #TODO DASH MODULE
    #TODO SEPRATED MONGODB FUNCTION
    #
# TODO CHECK IS IT PARAREL RUN ? 
# TODO DUPLICATE COMMENT WHEN CLOSE AND FETCH AGAIN
# TODO STYLESHEET


class DbConnect(): # MAYBE INHERIT FROM FETCHYOUTUBEDATA CLASS
    """Functions related to DB all processing in this class"""
    
    # Dict param to access database collection
    collection_params = { 

    }
    
    def __init__(self) -> None:
        self.__user = config.user
        self.__pwd = config.pwd
        
        try:
            self.myclient = pymongo.MongoClient(
                            f'mongodb+srv://{self.__user}:{self.__pwd}@cluster0.62kvg8y.mongodb.net/?retryWrites=true&w=majority'
                            )
            print('Connected')
        except Exception as e:
            print(e)
            print('connection failed')
            return
        
        self.mydb = self.myclient['YT_Project']
        self.db_collection_dct = {
            'Video': self.mydb['Video'],
            'Comment': self.mydb['Comment']
        }
        return
    
    def read_sentiment():
        
        return
    
    def insert_comment(self, doc):
        return
    
    def insert_vid_detail(self, doc: dict):
        try:
            self.inserted_id = self.db_collection_dct['Video'].insert_one(doc)
            print(self.inserted_id)
        except Exception as e:
            print(e)
            #self.inserted_id = None
        return self.inserted_id
    
    def read_existing_vid(self): # READ VDO FROM DB TO SHOW AT LISTBOX 
        return
    
    def check_duplicate_vdo(self, collection_obj, query):
        collection_obj.find_one(query) # ! ASK TER, does it checked by id? or anyfields else
        # check if none return true, else return false 
        return # BOOLs
    

class FetchYoutubeData(DbConnect):
    
    """All the things about youtube getting data
    """
    def __init__(self) -> None:
        super().__init__()
    #def __init__(self) -> None:
        self.__api = config.api
        self.yt_plug = googleapiclient.discovery.build(
            'youtube', 'v3', developerKey= self.__api
        )

    
    def fetch_live_comment(self):
        return
    
    def fetch_vdo_comment(self):
        return
    
    def fetch_vdo_detail(self, vid_id, write_db= True):
        # IF HTTPS:// in vid_id -> split .....
        try:
            request = self.yt_plug.videos().list(
                part= 'snippet,contentDetails',
                id= vid_id
            )
            print('GET vdo details complete')
        except Exception as e:
            raise RuntimeError(e)
            #return e
        
        response = request.execute()
        self.vdo_id = vid_id
        self.vdo_name = response['items'][0]['snippet']['title']
        self.vdo_publish_date = response['items'][0]['snippet']['publishedAt']
        self.vdo_channel_name = response['items'][0]['snippet']['channelTitle']
        self.vdo_details_doc = {
            '_id': self.vdo_id,
            'vid_name': self.vdo_name,
            'publish_date': self.vdo_publish_date,
            'channel_name': self.vdo_channel_name
        }
        
        if write_db == True:
            print('write here?')
            self.insert_vid_detail(self.vdo_details_doc)
            
            
        
        return self.vdo_details_doc
    
    

         
class DataProcessing(): # dont need constructor
    # ???? ทำยังไงให้สามารถใช้ DF ร่วมกันได้ บ่อยๆ ?????
    """
    NLP(sentiment analysis), 
    data processor to visualize, return df thats ready to plot
    """
    
    # ลองดูว่าถ้าเป็น self.df แล้วใช้ในกราฟด้วยการเข้าถึง self.df โดยตรง กราฟจะเปลี่ยนทันทีเลยไหม
    def get_sentiment(self, df= None):
        return df
    
    def count_user_comments(self, df= None):
        return df
    
    # FOR LINE PLOT SENTIMENT
    def count_sentiment_by_time(self, df= None):
        return
    
    def count_word():
        return
    
    def total_sentiment(): # return df of sentiment
        
        return # df where col = pos, neu, neg
    
    
    
if __name__ == '__main__':
    print('Start backed app')
    print('Init Mongo')
    #db_connnect = DbConnect()
    #print(db_connnect)
    # print(db_connnect.pwd)
    # print(db_connnect.user)
    
    obj = FetchYoutubeData()
    obj.fetch_vdo_detail('arn6Wh6bLy0')
    
    
    
    

    
    
    