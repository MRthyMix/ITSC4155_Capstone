# NBA Player Statistics Web Application

A Flask-based web application that provides comprehensive NBA player statistics, comparisons, and interactive features for basketball enthusiasts.

## 🏀 Features

- **Player Search**: Real-time autocomplete search for NBA players
- **Player Statistics**: View detailed individual player stats with last 5 playoff games visualization
- **Player Comparison**: Side-by-side comparison of two players' recent performance
- **Interactive Charts**: Visual representation of player performance using Chart.js
- **User Authentication**: Secure user registration and login system
- **Responsive Design**: Desktop-optimized interface with Bootstrap
- **Featured Players**: Spotlight on 12 top NBA players with their photos

## Featured Players

The application highlights these top NBA players:
- LeBron James (Lakers)
- Stephen Curry (Warriors) 
- Kevin Durant (Suns)
- Anthony Edwards (Timberwolves)
- Giannis Antetokounmpo (Bucks)
- Victor Wembanyama (Spurs)
- James Harden (Clippers)
- Ja Morant (Grizzlies)
- Kyrie Irving (Mavericks)
- Devin Booker (Suns)
- Klay Thompson (Mavericks)
- Paul George (76ers)

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Charts**: Chart.js for data visualization
- **NBA Data**: NBA API for real-time statistics
- **Authentication**: Flask sessions with password hashing

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/MRthyMix/ITSC4155_Capstone
cd ITSC4155_Capstone
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=sqlite:///users.db
```

### 5. Initialize the Database
The database will be automatically created when you first run the application.

### 6. Run the Application

**Windows:**
```bash
py app.py
# or
python app.py
```

**macOS:**
```bash
python3 app.py
```

The application will be available at `http://localhost:5000`


## Usage

### 1. User Registration
- Navigate to `/signup`
- Create a new account with username and password
- Login credentials are stored securely with password hashing

### 2. Player Search
- Use the search bar with autocomplete functionality
- Search supports partial name matching
- View detailed player statistics and recent playoff performance

### 3. Player Comparison
- Access the comparison feature from the navigation
- Select two players to compare their recent statistics
- View side-by-side performance metrics

### 4. Featured Players
- Browse the home page carousel showcasing top NBA players
- Click on any featured player to view their detailed stats


### Data Sources
- **NBA API**: Real-time player statistics and game logs
- **Local Database**: User authentication data
- **Static Data**: Featured player information and images

This project is developed as part of ITSC 4155 Capstone course.


---

**Note**: This application is designed for educational purposes and uses the NBA API for statistical data.
