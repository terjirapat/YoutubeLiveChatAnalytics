import new_main # ! DONT FORGET TO RENAME
from dash import Dash, html, dcc

# Copy dash code here





if __name__ == '__main__':
    print('Call dash server')
    
    # css style sheet
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = Dash(__name__, external_stylesheets= external_stylesheets)
    app.run_server(debug= True)
    