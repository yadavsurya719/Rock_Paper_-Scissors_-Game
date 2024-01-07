import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import random

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(id='background-animation'),
    html.Div([
        html.H1("Rock, Paper, Scissors Game", style={'text-align': 'center'}),
        html.Div([
            html.Button("Rock", id="rock-button", n_clicks=0),
            html.Button("Paper", id="paper-button", n_clicks=0),
            html.Button("Scissors", id="scissors-button", n_clicks=0),
        ], style={'display': 'flex', 'justify-content': 'center', 'margin-top': '20px'}),
        html.Div(id="output-message", style={'text-align': 'center', 'margin-top': '20px'}),
        html.Div(id="score", style={'text-align': 'center', 'margin-top': '20px'}),
        html.Div(html.Button("Play Again", id="play-again-button", n_clicks=0), style={'text-align': 'center', 'margin-top': '20px'}),
    ], style={'background-color': 'rgba(255, 255, 255, 0.9)', 'border-radius': '10px', 'padding': '20px'}),
])

user_score = 0
computer_score = 0

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

@app.callback(
    Output("output-message", "children"),
    Output("score", "children"),
    Input("rock-button", "n_clicks"),
    Input("paper-button", "n_clicks"),
    Input("scissors-button", "n_clicks"),
    State("play-again-button", "n_clicks"),
)
def update_output(rock_clicks, paper_clicks, scissors_clicks, play_again_clicks):
    global user_score, computer_score

    ctx = dash.callback_context
    button_id = ctx.triggered_id.split(".")[0] if ctx.triggered_id else None

    if button_id in ["rock-button", "paper-button", "scissors-button"]:
        user_choice = button_id.split("-")[0]
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = determine_winner(user_choice, computer_choice)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        score_message = f"Your score: {user_score} | Computer score: {computer_score}"
        return result, score_message

    elif button_id == "play-again-button":
        user_score = 0
        computer_score = 0
        return "", "Your score: 0 | Computer score: 0"

    return "", ""

if __name__ == "__main__":
    app.run_server(debug=True)
