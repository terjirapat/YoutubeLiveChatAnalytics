import new_main # ! DONT FORGET TO RENAME
from dash import Dash, html, dcc, Input, Output, State
#from dash import dash_bootstrap_component as dbc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
# dev lib
import pandas as pd

"""
FIG1 MOST COMMENT
FIG2, SENTIMENT
FIG3, SENTIMENT PIE CHART
FIG4, SUBSCRIBER
"""


"""

MAIN APPICATION, start dash web app by excecute this module
ALL GRAPH FUNCTION WILL CODE BELOW
Ralative functions are imported from new_main.py,

When GET COMMENT FROM YOUTUBE are clicked, dash will call FetchYouTubeData function
THEN DB class

If user select listbox of existing VDO to plot then call DataProcessing class and their functions 
    which return a df ready for plot (maybe acess df by class property directly if it better)
    
"""
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
#import dash_bootstrap_components as dbc
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


import time
@app.callback(
    #Output(), # OUTPUT INSERT TO LIST OF VIDs or to GRAPHs
    Output(component_id= 'vdo_select', component_property= 'value'),
    Input(component_id= 'submit-button', component_property= 'n_clicks'),
    State(component_id= 'uri-input', component_property= 'value')
)
def fetch_button_clicked(n_clicks ,vid_id):
    print(n_clicks)
    if n_clicks <= 0:
        return
    else:
        a = call_fetch(vid_id)
        return a
        
def call_fetch(vid_id):
    
    #// TODO CALL FETCH DETAILS
    doc = obj.fetch_vdo_detail(vid_id)
    print('Fetch VDO COMPLETE :', doc)
    #// TODO CALL FETCH LIVE COMMENT
    print('##### FETCH LIVE COMMENT')
    comment_docs = obj.fetch_live_comment(vid_id)
    print('##### FETCH COMMENT COMPLETE')
    new_fetched_df = pd.DataFrame(comment_docs)
    print('############# FETCH NEW COMMENT COMPLETE ###########')
    print(new_fetched_df)
    # SHOW COMPLELTE
    # return new_fetched_df
    doc_name = comment_docs['vid_name']
    doc_channel = comment_docs['channel_name']
    doc_id = comment_docs['_id']
    
    return f'{doc_name}__{doc_channel}__{doc_id}'
    #return #obj.read_existing_vid()


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

    fig1 = px.bar(df_count_authername.head(10), x='author_name', y='message', title= 'Top 10 User by Number of Comments')

# def count_sentiment_time():
    df_time_sentiment = df_comment.groupby(['datetime', 'sentiment'])[
        ['message']].agg('count').reset_index()

    # fig2 = px.line(df_time_sentiment, x="datetime", y="message",
    #               color='sentiment', title='Sentiment by Time')
    fig2 = px.line(df_time_sentiment, x="datetime", y="message", color='sentiment', title='Sentiment by Time',
                    color_discrete_map={'neu':'burlywood',
                                    'pos':'green',
                                    'neg':'crimson'})

# def sentiment_pie(): # pie chart สัดส่วน sentiment
    df_sen = df_comment.groupby('sentiment')[['message']].count().reset_index()

    fig3 = px.pie(df_sen, values='message', names='sentiment', title='Sentiment', color='sentiment',
                color_discrete_map={'neu':'burlywood',
                                    'pos':'green',
                                    'neg':'crimson'})


# def new_subscriber(): # table new subscriber
    # subscriber = df_comment[df_comment['message'].str.contains('^Welcome to')][['author_name']].rename(columns={'author_name': 'New Subscriber'})

    # fig4 = go.Figure(data=[go.Table(
    #     header=dict(values=list(subscriber.columns),
    #                 fill_color='paleturquoise',
    #                 align='left'),
    #     cells=dict(values=subscriber.transpose().values.tolist(),
    #             fill_color='lavender',
    #             align='left'))
    # ])
    df_time_msg = df_comment.groupby('datetime')[['message']].agg('count').reset_index()

    fig4 = px.line(df_time_msg, x="datetime", y="message", title='Messages by Time')
    # return fig
    
    return fig1, fig2, fig3, fig4



if __name__ == '__main__':
    print('Call dash server')
    
    default_vid_id = 'RQ5A-6GKRds'
    
    obj = new_main.FetchYoutubeData()
    # df_comment = obj.read_comment(default_vid_id)
    fig1, fig2, fig3, fig4 = create_figs(default_vid_id)
    
    dash_main()

    app.run_server()#debug= True)#, dev_tools_silence_routes_logging= False)
    