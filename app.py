import new_main # ! DONT FORGET TO RENAME
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
# dev lib
import pandas as pd

# Copy dash code paste here
"""

MAIN APPICATION, start dash web app by excecute this module
ALL GRAPH FUNCTION WILL CODE BELOW
Ralative functions are imported from new_main.py,

When GET COMMENT FROM YOUTUBE are clicked, dash will call FetchYouTubeData function
THEN DB class

If user select listbox of existing VDO to plot then call DataProcessing class and their functions 
    which return a df ready for plot (maybe acess df by class property directly if it better)
    
"""

df = pd.read_csv('https://github.com/chris1610/pbpython/blob/master/data/cereal_data.csv?raw=True')
print(df)
fig2 = px.histogram(df, x='sugars', title='Rating distribution')
print(fig2)

def dash_main():
    #app = Dash(__name__)

    # Get url input
    #create_df_comment('fS5h1PFtDJQ')

    #app.logger.info(df_comment)

    #fig1 = most_comment_user()

    #fig2 = count_sentiment_time()

    app.layout = html.Div(
        [

            html.Div(children=[
                html.H1(children='Scatter plot'),

                html.Div(children='''
                    description 1.
                '''),

                dcc.Graph(
                    id='id1',
                    # figure=fig1
                    figure=fig2
                )


            ], style={'padding': 10, 'flex': 1}),

            html.Div(children=[
                html.H1(children='Histogram plot'),

                html.Div(children='''
                    description 2.
                '''),

                dcc.Graph(
                    id='id2',
                    # figure=fig2
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
                    # figure=fig2
                    figure=fig2
                )
            ], style={'padding': 10, 'flex': 0.5}),

        ], style={'display': 'flex', 'flexDirection': 'row', 'flex-wrap': 'wrap'})

    # if __name__ == '__main__':
    #     app.run_server(debug=True, dev_tools_silence_routes_logging=False)




if __name__ == '__main__':
    print('Call dash server')
    
    # css style sheet
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = Dash(__name__, external_stylesheets= external_stylesheets)
    server = app.server
    dash_main()
    app.run_server()#debug= True)
    