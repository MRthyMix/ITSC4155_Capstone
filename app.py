from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo, playercareerstats, playergamelog
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from dotenv import load_dotenv
import os
# import openai
# from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI", 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)

ALL_PLAYERS = players.get_players()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

with app.app_context():
    db.create_all()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
        else:
            new_user = User(username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! You can now log in.", "success")
            return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user"] = username
            flash("Logged in successfully!", "success")
            return redirect(url_for("home_page"))
        else:
            flash("Invalid credentials", "danger")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home_page"))

@app.route('/autocomplete', methods=['GET'])
@login_required
def autocomplete():
    query = request.args.get('q', '').strip().lower()
    if not query:
        return jsonify([])

    filtered = [p for p in ALL_PLAYERS if query in p["full_name"].lower()]

    def match_rank(player_name: str, q: str) -> int:
        name_lower = player_name.lower()
        if name_lower.startswith(q):
            return 0
        return 1

    filtered.sort(key=lambda p: match_rank(p["full_name"], query))
    filtered = filtered[:5]

    return jsonify(filtered)

@app.route("/search", methods=["GET", "POST"])
@login_required
def search_page():
    if request.method == "POST":
        player_name = request.form.get("player_name", "").strip()
        if not player_name:
            return render_template("search.html", error="Please enter a player name.")
        return redirect(url_for("player_stats", name=player_name))

    return render_template("search.html")

@app.route("/player")
@login_required
def player_stats():
    player_name = request.args.get("name", "").strip()
    if not player_name:
        return redirect(url_for("home_page"))

    match = next((p for p in players.get_players()
                if player_name.lower() in p["full_name"].lower()), None)
    if not match:
        return render_template("index.html",
                            error=f"No NBA player found matching '{player_name}'")
    player_id = match["id"]

    # Fetch the last 5 games
    game_log = playergamelog.PlayerGameLog(
    player_id=player_id,
    season_type_all_star='Playoffs'
    ).get_data_frames()[0]
    last_5_games = game_log[['GAME_DATE', 'PTS', 'AST', 'REB', 'STL', 'BLK', 'FG3M']].dropna().head(5)

    # Process the stats
    labels = last_5_games['GAME_DATE'].tolist()
    points_per_game = last_5_games['PTS'].tolist()
    assists_per_game = last_5_games['AST'].tolist()
    rebounds_per_game = last_5_games['REB'].tolist()
    steals_per_game = last_5_games['STL'].tolist()
    blocks_per_game = last_5_games['BLK'].tolist()
    three_pointers_made = last_5_games['FG3M'].tolist()


    # Get player bio
    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    bio_df = info.get_data_frames()[0]          
    birth_str = bio_df.loc[0, "BIRTHDATE"]        
    birth_str = birth_str[:10]                    
    try:
        bdate = datetime.strptime(birth_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        computed_age = today.year - bdate.year - (
            (today.month, today.day) < (bdate.month, bdate.day)
        )
    except ValueError:
        computed_age = None

    team_id = bio_df.loc[0, "TEAM_ID"]
    team_logo_url = f"https://cdn.nba.com/logos/nba/{team_id}/primary/L/logo.svg" \
                    if team_id else "/static/images/fallback-team.png"

    return render_template(
    "index.html",
    error=None,
    player_data=bio_df.iloc[0].tolist(),
    computed_age=computed_age,
    team_logo_url=team_logo_url,
    chart_labels=labels,
    chart_points=points_per_game,
    chart_rebounds=rebounds_per_game,
    chart_assists=assists_per_game,
    chart_steals=steals_per_game,
    chart_blocks=blocks_per_game,
    chart_3pt=three_pointers_made,
)

@app.route('/compare', methods=['GET', 'POST'])
@login_required
def compare_players():
    if request.method == 'POST':
        player1 = request.form.get('player1')
        player2 = request.form.get('player2')

        if not player1 or not player2:
            flash("Please enter both player names.", "warning")
            return render_template('compare_players.html')

        return redirect(url_for('compare_results', player1=player1, player2=player2))

    return render_template('compare_players.html')

@app.route('/compare_results')
@login_required
def compare_results():
    player1_name = request.args.get('player1', '').strip()
    player2_name = request.args.get('player2', '').strip()

    def get_last_5_games(name):
        all_players = players.get_players()
        match = next((p for p in all_players if name.lower() in p['full_name'].lower()), None)
        if not match:
            return None, None
        pid = match['id']
        game_log = playergamelog.PlayerGameLog(player_id=pid, season_type_all_star="Playoffs").get_data_frames()[0]
        last_5 = game_log[['GAME_DATE', 'PTS', 'AST', 'REB']].head(5)
        return match['full_name'], last_5

    name1, stats1 = get_last_5_games(player1_name)
    name2, stats2 = get_last_5_games(player2_name)

    if stats1 is None or stats2 is None:
        flash("One or both players could not be found.", "danger")
        return redirect(url_for("compare_players"))

    return render_template('compare_player_results.html',
                    name1=name1, stats1=stats1,
                    name2=name2, stats2=stats2,
                    stats1_json=stats1.to_dict(orient='records'),
                    stats2_json=stats2.to_dict(orient='records'))

# Chatbot
# client = OpenAI()

# @app.route('/chat', methods=['POST'])
# def chatbot():
#     data = request.get_json()
#     messages = data.get("messages")

#     if not messages or not isinstance(messages, list):
#         return jsonify({'response': 'Invalid message format.'}), 400

#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=messages
#         )
#         reply = response.choices[0].message.content.strip()
#         return jsonify({'response': reply})
#     except Exception as e:
#         print(f"OpenAI API error: {e}")
#         return jsonify({'response': 'Sorry, something went wrong with the assistant.'}), 500



@app.route('/chat_page')
def chat_page():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True)

# For Vercel
app = app
