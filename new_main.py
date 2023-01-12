

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

from pymongo.errors import DuplicateKeyError
########################################
#// TODO RESTRUCTURE
    #// TODO Class db connect
        #// TODO Change where db insert,read called
        #// TODO Fetch live comment
        #// TODO DB Insert live comment (maybe add more filed (vdo_type: live/clip)) to filter 2 kinds
        # TODO TEST FETCH LIVE VDO, OTHERS SITUATIONS
        # TODO DB READ FUNCTION ( from create_df_comment() )
            # TODO CAST TO DF
        # TODO DATA_Processing (main function to calling DB_READ())
        # TODO 
    #TODO DASH MODULE
    #// TODO SEPRATED MONGODB FUNCTION
    #
# TODO CHECK IS IT PARAREL RUN ? 
#// TODO DUPLICATE COMMENT WHEN CLOSE AND FETCH AGAIN
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
            print('MongoDB Connected')
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
    
    def insert_doc(self, collection):
        #doc = list(doc)
        try:
            # self.inserted_id = self.db_collection_dct[collection].insert_one(doc)
            if isinstance(self.doc_to_write, list):
                self.inserted_id = self.db_collection_dct[collection].insert_many(self.doc_to_write)
                self.inserted_id = self.inserted_id.inserted_ids
            else:
                self.inserted_id = self.db_collection_dct[collection].insert_one(self.doc_to_write)
                self.inserted_id = self.inserted_id.inserted_id
            
            print(self.inserted_id)
            #print(self.inserted_id.inserted_id)
        except DuplicateKeyError as e:
            print(type(e))
            print(e)
            self.inserted_id = self.vdo_id
        except Exception as e:
            print('Something erorr', e)
            self.inserted_id = None
            #raise RuntimeError('Insert VDO details to DB Error !!!')
        
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

    
    def fetch_live_comment(self, vid_id):
        self.doc_to_write = []
        self.vdo_id = FetchYoutubeData.url_spliter(vid_id)
        
        chats = pytchat.create(vid_id)
        while chats.is_alive():
            for chat in chats.get().sync_items():
                doc = {
                    'video_id': self.vdo_id,
                    'comment': {
                    'datetime': chat.datetime,
                    'author_name': chat.author.name,
                    'message': chat.message
                    }
                }
                print(doc)
                self.doc_to_write.append(doc)
                
            else: # when fetching are interrupted, raise this
                self.insert_doc(collection= 'Comment')
                return self.doc_to_write
        # ! IF IT TRY AGAIN IT WILL BE HUALT FUNCTION
        print('!!!!!!!! FETCHING WAS INTERUPTED !!!!!')
        raise RuntimeError('Fetching VDO was interrupted !!!! ')
            
        # getting chats successfully, then insert to db, to avoid duplicated docs
    
    def fetch_vdo_comment(self):
        """GET VDO CLIP COMMENT (comment below clip)  FROM YOUTUBE"""
        return
    
    def fetch_vdo_detail(self, vid_id, write_db= True):
        # MOVE TO FUNCTION url_spliter 
        # IF HTTPS:// in vid_id -> split .....
        #if 'https' or 'watch?v=' in vid_id:
            # splt1 = vid_id.split('watch?v=')[1]
            # vid_id = splt1.split('&ab_channel')[0]
            # self.vdo_id = FetchYoutubeData.url_spliter(vid_id)
            #print(self.vid_id)
        # else:
            # self.vdo_id = vid_id
        self.vdo_id = FetchYoutubeData.url_spliter(vid_id)
            
        try:
            request = self.yt_plug.videos().list(
                part= 'snippet,contentDetails',
                id= self.vdo_id
            )
            print('GET vdo details complete')
        except Exception as e:
            raise RuntimeError(e)
            
        try:
            response = request.execute()
            #self.vdo_id = vid_id
            self.vdo_name = response['items'][0]['snippet']['title']
            self.vdo_publish_date = FetchYoutubeData.adjust_datetime(
                response['items'][0]['snippet']['publishedAt']
                )
            self.vdo_channel_name = response['items'][0]['snippet']['channelTitle']
            self.doc_to_write = {
                '_id': self.vdo_id,
                'vid_name': self.vdo_name,
                'publish_date': self.vdo_publish_date,
                'channel_name': self.vdo_channel_name
            }
        except Exception as e:
            raise RuntimeError(e)
        
        if write_db == True:
            print('write here?')
            print(self.doc_to_write)
            self.insert_doc(collection= 'Video')
    
        return self.doc_to_write

    def adjust_datetime(dt):
        if 'Z' in dt:
            dt.replace('Z', '')
        if 'T' in dt:
            dt = ' '.join(dt.split('T'))
        return dt
            
    def url_spliter(vid_id):
        if 'https' or 'watch?v=' in vid_id:
            vid_id = vid_id.split('watch?v=')[1]
            vid_id = vid_id.split('&ab_channel')[0]
            print(vid_id)
            return vid_id
        else:
            return vid_id
        
    # @classmethod
    # def url_spliter(cls, url):
    #     url = url.split('watch?v=')[1]
    #     cls.url_splited = url.split('&ab_channel')[0]
    #     print(cls.url_splited)

         
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

    
    #DbConnect()
    obj = FetchYoutubeData()
    # obj.fetch_vdo_detail('arn6Wh6bLy0')
    obj.fetch_vdo_detail('https://www.youtube.com/watch?v=dyEeoHDw3IY&ab_channel=9arm')
    obj.fetch_live_comment('https://www.youtube.com/watch?v=dyEeoHDw3IY&ab_channel=9arm')
    # obj.fetch_vdo_detail('https://www.youtube.com/watch?)
    print(obj.vdo_id)
    #print(obj.vdo_details_doc)
    
    
    
    

    
    
    