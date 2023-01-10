

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
# TODO RESTRUCTURE
    #TODO Class db connect
        # TODO Change where db insert,read called
    #TODO DASH MODULE
    #TODO SEPRATED MONGODB FUNCTION
    #
# TODO CHECK IS IT PARAREL RUN ? 
# TODO DUPLICATE COMMENT WHEN CLOSE AND FETCH AGAIN
# TODO STYLESHEET



class FetchYoutubeData():
    
    """All the things about youtube getting data
    """
    def __init__(self) -> None:
        pass
    
    def fetch_live_comment(self):
        return
    
    def fetch_vdo_comment(self):
        return
    
    

class DbConnect(): # MAYBE INHERIT FROM FETCHYOUTUBEDATA CLASS
    """Functions related to DB all processing in this class"""
    
    # Dict param to access database collection
    collection_params = { 

    }
    
    def __init__(self) -> None:
        return
    
    
    def read_sentiment():
        return
    
    def insert_comment():
        return
    
    
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
    
    
    
    
    
    

    
    
    