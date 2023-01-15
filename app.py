import new_main # ! DONT FORGET TO RENAME
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
# dev lib
import pandas as pd

# Copy dash code paste here
"""
FIG1 MOST COMMENT
FIG2, SENTIMENT
FIG3, SENTIMENT PIE CHART
FIG4, SUBSCRIBER
"""

# ! ถ้าดึงเข้าาแล้วจะเพิ่มลำบาก ให้ทำ util function ขึ้นมาเพื่อ convert เป็น str format for dropdwn
# ! BUG READ VDO WITHOUT COMMENT BUG -> FUNCTION HANDLE OR REMOVE IT FROM LIST
    # ! เขียน function ไล่เช็ค ให้ดึงจกา vdo ID แล้วถ้าไม่มี comment ในอีก collection ให้ลบ
#// TODO, เขียน function plot (return tuple (fig1,fig2,fig3))
    #// TODO ใน function จะดึงข้อมูลจาก DB
    #// TODO เรียกละ function มาเป็น fig1, fig2, fig3 และ plot ปกติก่อน
    #// TODO CALLBACK หลักสำรหับเปลี่ยนทุกกราฟ มี input มาจากช่องที่เลือก list of video
# TODO สร้าง HTML (DASH) ELEMENT FOR INPUT
    # TODO SHOW LIST OF VIDEO
        # TODO CHANGE FONT SIZE
    # TODO VIDEO ID input
    # TODO FETCH BUTTON 
        # TODO CREATE FUNCTION TO CALL FETCH LIVE AND COMMENT
            # ! HOW TO APPEND TO LIST OF EXISTING VDO
# TODO สร้าง callback

# TODO DASH HOVER
# TODO DASH จัดรูปร่าง
# TODO DASH PLOT ลูกเล่น 

"""

MAIN APPICATION, start dash web app by excecute this module
ALL GRAPH FUNCTION WILL CODE BELOW
Ralative functions are imported from new_main.py,

When GET COMMENT FROM YOUTUBE are clicked, dash will call FetchYouTubeData function
THEN DB class

If user select listbox of existing VDO to plot then call DataProcessing class and their functions 
    which return a df ready for plot (maybe acess df by class property directly if it better)
    
"""
import dash_bootstrap_components as dbc
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = [dbc.themes.DARKLY]
# app = Dash(__name__, external_stylesheets= external_stylesheets)
app = Dash(__name__)
server = app.server


# def dash_main():

#     app.layout = html.Div(
#         [   
#             html.Div(children= [
#                 html.H1(
#                     children= 'Existing VDO name to plot'
#                     # children= 'Enter youtube video uri to fetch live stream comment'
#                 ),
#                 dcc.Dropdown(id= 'vdo_select', value= obj.read_existing_vid()[0],
#                              options= obj.read_existing_vid())
                
#             ], style={'padding': 10, 'flex': 1})
            
#             ,   html.H1("Enter youtube video URI"),
                #     html.Div([
                #         html.Div([
                #             html.Label("URI"),
                #             dcc.Input(id="uri-input", type="text", placeholder="Enter video URI"),
                #         ]),
                #     html.Button("Submit", id="submit-button", n_clicks=0),
                # ]),

#             html.Div(children=[
#                 html.H1(children='Scatter plot'),

#                 html.Div(children='''
#                     description 1.
#                 '''),

#                 dcc.Graph(
#                     id='id1',
#                     figure=fig1
#                 )


#             ], style={'padding': 10, 'flex': 1}),

#             html.Div(children=[
#                 html.H1(children='Histogram plot'),

#                 html.Div(children='''
#                     description 2.
#                 '''),

#                 dcc.Graph(
#                     id='id2',
#                     figure=fig2
#                 )
#             ], style={'padding': 10, 'flex': 1}),


#             html.Div(children=[
#                 html.H1(children='Histogram plot 3'),

#                 html.Div(children='''
#                     description 3.
#                 '''),

#                 dcc.Graph(
#                     id='id3',
#                     figure=fig3
#                 )
#             ], style={'padding': 10, 'flex': 0.5}),


#             html.Div(children=[
#                 html.H1(children='Histogram plot 3'),

#                 html.Div(children='''
#                     description 3.
#                 '''),

#                 dcc.Graph(
#                     id='id4',
#                     figure=fig4
#                 )
#             ], style={'padding': 10, 'flex': 0.5}),

#         ], style={'display': 'flex', 'flexDirection': 'row', 'flex-wrap': 'wrap'})


#import dash_html_components as html
import dash_bootstrap_components as dbc
def dash_main():
    app.layout = html.Div([
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.H1(
                        children= 'Existing VDO name to plot'
                    ),
                    dcc.Dropdown(id= 'vdo_select', value= obj.read_existing_vid()[0],
                                 options= obj.read_existing_vid())
                ], style={'padding': 10}),
                width={"size": 4, "offset": 4},
            ),
        ]),
        
         #html.Div([
    html.H1("Enter youtube video URI"),
    html.Div([
        html.Div([
            html.Label("URI"),
            dcc.Input(id="uri-input", type="text", placeholder="Enter video URI"),
        ]),
        html.Button("Submit", id="submit-button", n_clicks=0),
    ]),
    
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='id1',
                    figure=fig1
                ),
                width={"size": 6, "offset": 3},
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='id2',
                    figure=fig2
                ),
                width={"size": 6, "offset": 3},
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='id3',
                    figure=fig3
                ),
                width={"size": 6, "offset": 3},
            ),
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='id4',
                    figure=fig4
                ),
                width={"size": 6, "offset": 3},
            ),
        ])
    ], style={'display': 'flex', 'flexDirection': 'column'})
        # if __name__ == '__main__':
        #     app.run_server(debug=True, dev_tools_silence_routes_logging=False)


    #// TODO ทำให้เป็น function เดียว return 4 กราฟ หรือจะทำยังไง ถ้าแยก function แล้วจะดึง DF รอบเดียว
# TODO CALLBACK 
# TODO VIDEO DETAILS จะทำยังไงให้เมื่อดึงเสร็จ แล้วมันเพิ่มรายชื่อเข้ามา (append ยังไง)


@app.callback(
    # output TO EACH FIC
    Output(component_id= 'id1', component_property= 'figure'),
    Output(component_id= 'id2', component_property= 'figure'),
    Output(component_id= 'id3', component_property= 'figure'),
    Output(component_id= 'id4', component_property= 'figure'),
    # INPUT VDO ID FROM DROPDOWN LIST
    Input(component_id= 'vdo_select', component_property= 'value')
)
def create_figs(video_id):
    
    if '__' in video_id:
        video_id = video_id.split('__')[2]
    #video_id = video_id.split
    print('############################')
    print('create figs calll')
    df_comment = obj.read_comment(video_id)
    print(df_comment)

    df_count_authername = df_comment.groupby('author_name')[['message']].agg( # ! BUG, STR OBJECT NOT CALLABLE Y
        'count').sort_values(by='message', ascending=False).reset_index()

    fig1 = px.bar(df_count_authername.head(10), x='author_name', y='message')

# def count_sentiment_time():
    df_time_sentiment = df_comment.groupby(['datetime', 'sentiment'])[
        ['message']].agg('count').reset_index()

    fig2 = px.line(df_time_sentiment, x="datetime", y="message",
                  color='sentiment', title='Sentiment by Time')


# def sentiment_pie(): # pie chart สัดส่วน sentiment
    df_sen = df_comment.groupby('sentiment')[['message']].count().reset_index()

    fig3 = px.pie(df_sen, values='message', names='sentiment', title='Sentiment', color='sentiment',
                color_discrete_map={'neu':'burlywood',
                                    'pos':'green',
                                    'neg':'crimson'})


# def new_subscriber(): # table new subscriber
    subscriber = df_comment[df_comment['message'].str.contains('^Welcome to')][['author_name']].rename(columns={'author_name': 'New Subscriber'})

    fig4 = go.Figure(data=[go.Table(
        header=dict(values=list(subscriber.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=subscriber.transpose().values.tolist(),
                fill_color='lavender',
                align='left'))
    ])

    
    return fig1, fig2, fig3, fig4



if __name__ == '__main__':
    print('Call dash server')
    
    default_vid_id = 'RQ5A-6GKRds'
    
    obj = new_main.FetchYoutubeData()
    # df_comment = obj.read_comment(default_vid_id)
    fig1, fig2, fig3, fig4 = create_figs(default_vid_id)
    
    # css style sheet
    # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    # app = Dash(__name__, external_stylesheets= external_stylesheets)
    # server = app.server
    dash_main()
    app.run_server(debug= True, dev_tools_silence_routes_logging= False)
    