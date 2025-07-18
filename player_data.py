# Featured players list - only these players will be available
# This limits the NBA API data to just these key players

FEATURED_PLAYERS = [
    {
        'id': 2544,
        'full_name': 'LeBron James',
        'first_name': 'LeBron',
        'last_name': 'James',
        'is_active': True,
        'team_id': 1610612747,
        'team_name': 'Los Angeles Lakers',
        'position': 'F',
        'height': '6-9',
        'weight': '250',
        'birthdate': '1984-12-30',
        'years_experience': 21
    },
    {
        'id': 201939,
        'full_name': 'Stephen Curry',
        'first_name': 'Stephen',
        'last_name': 'Curry',
        'is_active': True,
        'team_id': 1610612744,
        'team_name': 'Golden State Warriors',
        'position': 'G',
        'height': '6-2',
        'weight': '185',
        'birthdate': '1988-03-14',
        'years_experience': 15
    },
    {
        'id': 201142,
        'full_name': 'Kevin Durant',
        'first_name': 'Kevin',
        'last_name': 'Durant',
        'is_active': True,
        'team_id': 1610612756,
        'team_name': 'Phoenix Suns',
        'position': 'F',
        'height': '6-10',
        'weight': '240',
        'birthdate': '1988-09-29',
        'years_experience': 17
    },
    {
        'id': 1630162,
        'full_name': 'Anthony Edwards',
        'first_name': 'Anthony',
        'last_name': 'Edwards',
        'is_active': True,
        'team_id': 1610612750,
        'team_name': 'Minnesota Timberwolves',
        'position': 'G',
        'height': '6-4',
        'weight': '225',
        'birthdate': '2001-08-05',
        'years_experience': 4
    },
    {
        'id': 203507,
        'full_name': 'Giannis Antetokounmpo',
        'first_name': 'Giannis',
        'last_name': 'Antetokounmpo',
        'is_active': True,
        'team_id': 1610612749,
        'team_name': 'Milwaukee Bucks',
        'position': 'F',
        'height': '6-11',
        'weight': '243',
        'birthdate': '1994-12-06',
        'years_experience': 11
    },
    {
        'id': 1641705,
        'full_name': 'Victor Wembanyama',
        'first_name': 'Victor',
        'last_name': 'Wembanyama',
        'is_active': True,
        'team_id': 1610612759,
        'team_name': 'San Antonio Spurs',
        'position': 'C',
        'height': '7-4',
        'weight': '210',
        'birthdate': '2004-01-04',
        'years_experience': 1
    },
    {
        'id': 201935,
        'full_name': 'James Harden',
        'first_name': 'James',
        'last_name': 'Harden',
        'is_active': True,
        'team_id': 1610612746,
        'team_name': 'LA Clippers',
        'position': 'G',
        'height': '6-5',
        'weight': '220',
        'birthdate': '1989-08-26',
        'years_experience': 15
    },
    {
        'id': 1629630,
        'full_name': 'Ja Morant',
        'first_name': 'Ja',
        'last_name': 'Morant',
        'is_active': True,
        'team_id': 1610612763,
        'team_name': 'Memphis Grizzlies',
        'position': 'G',
        'height': '6-3',
        'weight': '174',
        'birthdate': '1999-08-10',
        'years_experience': 5
    },
    {
        'id': 202681,
        'full_name': 'Kyrie Irving',
        'first_name': 'Kyrie',
        'last_name': 'Irving',
        'is_active': True,
        'team_id': 1610612742,
        'team_name': 'Dallas Mavericks',
        'position': 'G',
        'height': '6-2',
        'weight': '195',
        'birthdate': '1992-03-23',
        'years_experience': 13
    },
    {
        'id': 1626164,
        'full_name': 'Devin Booker',
        'first_name': 'Devin',
        'last_name': 'Booker',
        'is_active': True,
        'team_id': 1610612756,
        'team_name': 'Phoenix Suns',
        'position': 'G',
        'height': '6-5',
        'weight': '206',
        'birthdate': '1996-10-30',
        'years_experience': 9
    },
    {
        'id': 202691,
        'full_name': 'Klay Thompson',
        'first_name': 'Klay',
        'last_name': 'Thompson',
        'is_active': True,
        'team_id': 1610612742,
        'team_name': 'Dallas Mavericks',
        'position': 'G',
        'height': '6-6',
        'weight': '215',
        'birthdate': '1990-02-08',
        'years_experience': 13
    },
    {
        'id': 202331,
        'full_name': 'Paul George',
        'first_name': 'Paul',
        'last_name': 'George',
        'is_active': True,
        'team_id': 1610612755,
        'team_name': 'Philadelphia 76ers',
        'position': 'F',
        'height': '6-8',
        'weight': '220',
        'birthdate': '1990-05-02',
        'years_experience': 14
    }
]

# Mock stats data for demonstration
MOCK_STATS = {
    'pts': 25.7,
    'reb': 7.3,
    'ast': 7.3,
    'fg_pct': 0.540,
    'ft_pct': 0.741,
    'fg3_pct': 0.410
}

def get_featured_players():
    """Returns list of featured players only"""
    return FEATURED_PLAYERS

def is_featured_player(player_name):
    """Check if player is in featured list"""
    return any(player_name.lower() in p['full_name'].lower() for p in FEATURED_PLAYERS)