# NBA Player Statistics Web Application

A Flask-based web application that provides comprehensive NBA player statistics, comparisons, and interactive features for basketball enthusiasts.

## 🏀 Features

- **Player Search**: Real-time autocomplete search for NBA players
- **Player Statistics**: View detailed individual player stats with last 5 playoff games visualization
- **Player Comparison**: Side-by-side comparison of two players' recent performance
- **Interactive Charts**: Visual representation of player performance using Chart.js
- **User Authentication**: Secure user registration and login system
- **Responsive Design**: Mobile-friendly interface with Bootstrap
- **Featured Players**: Spotlight on 12 top NBA players with their photos

## 🎯 Featured Players

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

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Charts**: Chart.js for data visualization
- **NBA Data**: NBA API for real-time statistics
- **Authentication**: Flask sessions with password hashing

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
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
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📁 Project Structure

```
ITSC4155_Capstone/
├── app.py                 # Main Flask application
├── app_utils.py          # Utility functions
├── player_data.py        # Featured players data
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── instance/
│   └── users.db         # SQLite database
├── templates/           # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── search.html
│   ├── index.html
│   └── compare_players.html
├── static/              # Static files
│   ├── css/
│   │   └── home.css
│   ├── js/
│   │   ├── autocomplete.js
│   │   ├── carouselSlide.js
│   │   └── chat.js
│   └── images/          # Player photos
└── tests/               # Test files
```

## 🎮 Usage

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

## 🔧 Key Components

### Database Schema
```sql
User Table:
- id (Primary Key)
- username (Unique)
- password (Hashed)
```

### API Endpoints
- `/` - Home page with featured players
- `/signup` - User registration
- `/login` - User authentication
- `/logout` - Session termination
- `/search` - Player search and statistics
- `/compare` - Player comparison tool
- `/autocomplete` - AJAX endpoint for search suggestions

### Data Sources
- **NBA API**: Real-time player statistics and game logs
- **Local Database**: User authentication data
- **Static Data**: Featured player information and images

## 🎨 Frontend Features

### Interactive Elements
- **Autocomplete Search**: Real-time player name suggestions
- **Image Carousel**: Rotating display of featured players
- **Responsive Charts**: Dynamic visualization of player statistics
- **Mobile-Friendly**: Bootstrap-based responsive design

### JavaScript Modules
- `autocomplete.js`: Handles search suggestions
- `carouselSlide.js`: Manages image carousel functionality
- `chat.js`: Prepared for future chatbot integration

## 🔒 Security Features

- **Password Hashing**: Secure password storage using Werkzeug
- **Session Management**: Flask sessions for user authentication
- **Input Validation**: Form validation and sanitization
- **Environment Variables**: Sensitive data stored in .env file

## 📊 Statistics Features

### Player Individual Stats
- Points per game
- Assists per game
- Rebounds per game
- Steals per game
- Blocks per game
- Three-pointers made
- Last 5 playoff games visualization

### Player Comparison
- Side-by-side statistical comparison
- Recent performance metrics
- Visual chart comparisons

## 🧪 Testing

Run the test suite:
```bash
pytest
```

Test files are located in the `tests/` directory and cover:
- Player search functionality
- Autocomplete features
- Database operations
- Authentication systems

## 🚨 Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure the `instance/` directory exists
   - Check SQLALCHEMY_DATABASE_URI in .env file

2. **NBA API Timeout**
   - The app includes fallback data for featured players
   - Check internet connection for live data

3. **Environment Variables Not Loading**
   - Verify `.env` file exists in root directory
   - Check SECRET_KEY is properly set

4. **Port Already in Use**
   - Change the port in app.py: `app.run(debug=True, port=5001)`

### Development Mode
To run in development mode with debug enabled:
```bash
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development     # Windows
python app.py
```

## 🎯 Future Enhancements

- **ChatBot Integration**: OpenAI-powered basketball assistant
- **Real-time Updates**: Live game scores and updates
- **Advanced Analytics**: More detailed statistical analysis
- **Team Statistics**: Team-level performance metrics
- **Social Features**: User favorites and sharing

## 📝 License

This project is developed as part of ITSC 4155 Capstone course.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📞 Support

For questions or issues, please refer to the project documentation or contact the development team.

---

**Note**: This application is designed for educational purposes and uses the NBA API for statistical data. All player images and statistics are for demonstration purposes.