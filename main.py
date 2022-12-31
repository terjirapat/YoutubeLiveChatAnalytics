import config  # import user, pwd for connect mongodb from config.py
import pandas as pd
from datetime import datetime
import plotly.express as px
import pymongo
import pytchat
import googleapiclient.discovery
from dash import Dash, html, dcc
from thai_sentiment import get_sentiment
from pythainlp import word_tokenize
from pythainlp.corpus.common import thai_stopwords

########################################

# connect mongodb


def connect_db():
    global mycol_video, mycol_comment

    # user, pwd from config.py
    user = config.user
    pwd = config.pwd

    myclient = pymongo.MongoClient(
        f'mongodb+srv://{user}:{pwd}@cluster0.62kvg8y.mongodb.net/?retryWrites=true&w=majority')
    mydb = myclient['YT_Project']
    mycol_video = mydb['Video']
    mycol_comment = mydb['Comment']

########################################

# Dash


def dash_main():
    app = Dash(__name__)

    create_df_comment('fS5h1PFtDJQ')

    app.logger.info(df_comment)

    fig1 = most_comment_user()

    fig2 = count_sentiment_time()

    app.layout = html.Div(
        [

            html.Div(children=[
                html.H1(children='Scatter plot'),

                html.Div(children='''
                    description 1.
                '''),

                dcc.Graph(
                    id='id1',
                    figure=fig1
                )


            ], style={'padding': 10, 'flex': 1}),

            html.Div(children=[
                html.H1(children='Histogram plot'),

                html.Div(children='''
                    description 2.
                '''),

                dcc.Graph(
                    id='id2',
                    figure=fig2
                )
            ], style={'padding': 10, 'flex': 1}),


            html.Div(children=[
                html.H1(children='Histogram plot 3'),

                html.Div(children='''
                    description 3.
                '''),

                dcc.Graph(
                    id='id3',
                    figure=fig2
                )
            ], style={'padding': 10, 'flex': 0.5}),

        ], style={'display': 'flex', 'flexDirection': 'row', 'flex-wrap': 'wrap'})

    if __name__ == '__main__':
        app.run_server(debug=True, dev_tools_silence_routes_logging=False)

########################################

# Insert data to mongodb


def vid_detail(video_id):  # Input video ID to extract video detail as document to Video collection
    api_key = config.api  # api from config.py

    # Set up the YouTube API client
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    # Make a request to the YouTube API to get information about the video
    request = youtube.videos().list(
        part="snippet,contentDetails",
        id=video_id
    )
    response = request.execute()

    # Extract the name, public date, and YouTube channel of the video
    video_name = response["items"][0]["snippet"]["title"]
    video_public_date = response["items"][0]["snippet"]["publishedAt"]
    video_channel_name = response["items"][0]["snippet"]["channelTitle"]

    document = {'_id': video_id, 'vid_name': video_name,
                'public_date': video_public_date, 'channel_name': video_channel_name}

    x = mycol_video.insert_one(document)


def vid_comment(video_id):  # Input video ID to extract comment as document to Comment collection
    chat = pytchat.create(video_id)

    while chat.is_alive():
        for c in chat.get().sync_items():
            # print(f"{c.datetime} [{c.author.name}]- {c.message}")

            document = {
                'video_id': video_id,
                'comment': {
                    'datetime': c.datetime,
                    'author_name': c.author.name,
                    'message': c.message
                }
            }
            x = mycol_comment.insert_one(document)

########################################

# Query from mongodb


def create_df_comment(video_id):  # query video comment form mongodb by video id
    global df_comment

    ls_datetime = []
    ls_author_name = []
    ls_message = []

    result = mycol_comment.find({
        'video_id': {'$eq': video_id}
    },
        {
        'comment'
    })

    for i in result:
        datetime = i['comment']['datetime']
        author_name = i['comment']['author_name']
        message = i['comment']['message']

        ls_datetime.append(datetime)
        ls_author_name.append(author_name)
        ls_message.append(message)

    dict = {'datetime': ls_datetime,
            'author_name': ls_author_name, 'message': ls_message}

    df_comment = pd.DataFrame(dict)

    # sentiment
    def sentiment(text):
        sen = get_sentiment(text)
        return sen[0]

    df_comment['sentiment'] = df_comment['message'].apply(sentiment)

########################################

# plot


def most_comment_user():
    df_count_authername = df_comment.groupby('author_name')[['message']].apply(
        'count').sort_values(by='message', ascending=False).reset_index()

    fig = px.bar(df_count_authername.head(10), x='author_name', y='message')
    return fig


def count_sentiment_time():
    df_time_sentiment = df_comment.groupby(['datetime', 'sentiment'])[
        ['message']].apply('count').reset_index()

    fig = px.line(df_time_sentiment, x="datetime", y="message",
                  color='sentiment', title='Sentiment by Time')
    return fig

########################################


connect_db()

dash_main()

# x = input('Input number: ')
# if x == '1':
#     video_id = input('Input Video ID: ')
#     vid_detail(video_id)
#     vid_comment(video_id)
#     print('Import Data Success!!')