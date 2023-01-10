import new_main # ! DONT FORGET TO RENAME
from dash import Dash, html, dcc

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





if __name__ == '__main__':
    print('Call dash server')
    
    # css style sheet
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = Dash(__name__, external_stylesheets= external_stylesheets)
    app.run_server(debug= True)
    