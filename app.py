import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load merged dataset
df = pd.read_csv("Merged_NFL_Data.csv")

# Convert key columns to numeric
df["PF"] = pd.to_numeric(df["PF"], errors='coerce')
df["Yds_x"] = pd.to_numeric(df["Yds_x"], errors='coerce')
df["W"] = pd.to_numeric(df["W"], errors='coerce')
df["Cmp_y"] = pd.to_numeric(df["Cmp_y"], errors='coerce')
df["Att_y"] = pd.to_numeric(df["Att_y"], errors='coerce')
df["Yds"] = pd.to_numeric(df["Yds"], errors='coerce')
df["Sk"] = pd.to_numeric(df["Sk"], errors='coerce')
df["Int_y"] = pd.to_numeric(df["Int_y"], errors='coerce')  # Rename for clarity

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Rob Pastori's NFL 2024 Team Performance Dashboard"

# Layout
app.layout = html.Div([
    html.H1(
        [
            "Rob Pastori's ",
            html.Strong("NFL 2024 Team Performance Dashboard")
        ],
        style={
            'textAlign': 'center',
            'fontSize': '3.5em',
            'fontFamily': 'Montserrat, sans-serif',
            'color': '#2c3e50',
            'textShadow': '2px 2px 4px rgba(0,0,0,0.2)',
            'padding': '20px 0',
            'background': 'linear-gradient(to right, #e0f2f7, #bbdefb)',
            'borderRadius': '10px',
            'margin': '20px auto',
            'maxWidth': '90%',
        }),

    html.Div([
        html.Label("Select Team:"),
        dcc.Dropdown(
            id='team-dropdown',
            options=[{'label': team, 'value': team} for team in sorted(df['Team'].dropna().unique())],
            value=None,
            placeholder="All Teams"
        )
    ], style={'width': '50%', 'margin': 'auto'}),

    dcc.Graph(id='points-vs-yards'),
    dcc.Graph(id='wins-bar'),
    dcc.Graph(id='passing-vs-yards'),
    dcc.Graph(id='sacks-bar'),
    dcc.Graph(id='interceptions-bar')
]),    html.Div(
        [
            html.A(
                "Data courtesy of Sports Reference",
                href="https://www.pro-football-reference.com/years/2024/#site_menu_link",
                target="_blank",
                style={
                    'fontSize': '0.8em',
                    'color': '#666',
                    'textDecoration': 'none',
                    'textAlign': 'center',
                    'display': 'block',
                    'marginTop': '30px',
                    'marginBottom': '10px'
                }
            )
        ]
    )

@app.callback(
    Output('points-vs-yards', 'figure'),
    Output('wins-bar', 'figure'),
    Output('passing-vs-yards', 'figure'),
    Output('sacks-bar', 'figure'),
    Output('interceptions-bar', 'figure'),
    Input('team-dropdown', 'value')
)
def update_graphs(selected_team):
    filtered_df = df if not selected_team else df[df['Team'] == selected_team]
    sacks_df = filtered_df.sort_values('Sk', ascending=False)
    ints_df = filtered_df.sort_values('Int_y', ascending=False)

    fig1 = px.scatter(filtered_df, x="Yds_x", y="PF", text="Team",
                      title="Total Yards vs Points For",
                      labels={"Yds_x": "Total Yards", "PF": "Points For"},
                      color="Team")

    fig2 = px.bar(filtered_df, x="Team", y="W",
                  title="Wins per Team",
                  labels={"W": "Wins"})

    fig3 = px.scatter(filtered_df, x="Cmp_y", y="Yds", size="Att_y", color="Team", text="Team",
                      title="Passing Completions vs Passing Yards",
                      labels={"Cmp_y": "Completions", "Yds": "Passing Yards", "Att_y": "Attempts"})

    fig4 = px.bar(sacks_df, x="Team", y="Sk",
                  title="Sacks per Team (Highest to Lowest)",
                  labels={"Sk": "Sacks"})

    fig5 = px.bar(ints_df, x="Team", y="Int_y",
                  title="Interceptions per Team (Highest to Lowest)",
                  labels={"Int_y": "Interceptions"})

    return fig1, fig2, fig3, fig4, fig5

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
