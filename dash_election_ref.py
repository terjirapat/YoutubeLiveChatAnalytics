#Reference https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Deploy_App_to_Web/PythonAnyWhere
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from pathlib import Path
path = Path(__file__).parent.absolute()
fpath = str(path)+'\politics.csv'
df = pd.read_csv(fpath)
print(df.head())

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# สร้าง Radio button เตรียมไว้ และเอาเข้า list เพื่อนำไปใช้ต่อ ใน layout
radio_list = []
for s,v in zip(['AZ','FL','GA','IA','ME','MI','NC','NV','OH','PA','TX','WI'],
               [11,29,16,6,4,16,15,6,18,20,38,10]):
    radio_list.append(
        html.Div([
            html.Label(f'{s}-{v}: ', style={'display':'inline', 'fontSize':15}),
            dcc.RadioItems(
                id=f'radiolist-{s}',
                options=[
                    {"label": "Dem", "value": "democrat"},
                    {"label": "Rep", "value": "republican"},
                    {"label": "NA", "value": "unsure"},
                ],
                value='unsure',
                inputStyle={'margin-left': '10px'},
                labelStyle={'display': 'inline-block'},
                style={'display':'inline'}
            ),
        ], style={'textAlign':'end'})
    )

#print(radio_list)


# Input list for the callback
input_list = [] # append Input function with param เข้าไป แล้วเอา list ไปใช้่เป็น arg ใน callback ได้เลย
for x in ['AZ','FL','GA','IA','ME','MI','NC','NV','OH','PA','TX','WI']:
    input_list.append(
        Input(component_id=f'radiolist-{x}', component_property='value')
    )

# การจัด Layout นี่ ใช้ Div และจัดเป็น Row, Col ข้างใน Dif ซึ่งจะคล้ายๆ Grid
app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1("USA Elections 2020", style={'textAlign':'center'}), width=12)
    ]),
    dbc.Row([
        dbc.Col(radio_list, xs=4, sm=4, md=4, lg=2, xl=2), # เอา Radio button ที่ทำเป็น list เตรียมไว้ มาใช้ 
        dbc.Col(dcc.Graph(id='my-choropleth', figure={},
                          config={'displayModeBar':False}), xs=8, sm=8, md=8, lg=6, xl=6),
        dbc.Col(dcc.Graph(id='my-bar', figure={},
                          config={'displayModeBar': False}), xs=6, sm=6, md=6, lg=4, xl=4)

    ], className="g-0")
])


# must have Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='my-choropleth', component_property='figure'),
    Output(component_id='my-bar', component_property='figure'),
    input_list # list of Input function ที่เตรียมไว้มาใช้ได้ทันที
)
def update_graph(az, fl, ga, ia, me, mi, nc, nv, oh, pa, tx, wi):
    dff = df.copy()  # assign party to dataframe (long_code.py lines 55-57)
    for st,radio_value_chosen in zip(
            ['AZ','FL','GA','IA','ME','MI','NC','NV','OH','PA','TX','WI'],
            [az, fl, ga, ia, me, mi, nc, nv, oh, pa, tx, wi]):
        dff.loc[dff.state == st, 'party'] = radio_value_chosen

    # build map figure, use buildin function from plotly express
    fig_map = px.choropleth(
        dff, locations="state", hover_name='electoral votes',
        locationmode="USA-states", color="party", # color depen on "party"col
        scope="usa", color_discrete_map={'democrat': 'blue', # map the color
                                         'republican': 'red',
                                         'unsure': 'grey'})

    # build histogram figure
    dff = dff[dff.party != 'unsure']
    fig_bar = px.histogram(dff, x='party', y='electoral votes', color='party',
                           range_y=[0,350], color_discrete_map={'democrat': 'blue',
                                                                'republican': 'red'}
                           )
    # add horizontal line
    fig_bar.update_layout(showlegend=False, shapes=[
        dict(type='line', yref='paper',y0=0.77,y1=0.77, xref='x',x0=-0.5,x1=1.5)
    ])
    # add annotation text above line
    fig_bar.add_annotation(x=0.5, y=280, showarrow=False, text="270 votes to win")

    return fig_map, fig_bar


if __name__ == '__main__':
    app.run_server(debug=False)