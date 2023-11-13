import mysql.connector

# Your MySQL database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "CRcr240403",
    "database": "predsport"
}

data = [
  { "teamId": 1610612737, 
  "abbreviation": "ATL", 
  "value": "Atlanta Hawks", 
  "label": "Atlanta Hawks", 
  "simpleName": "Hawks",
   "location": "Atlanta"
},
{
  "teamId": 1610612738,
  "abbreviation": "BOS",
  "value": "Boston Celtics", 
  "label": "Boston Celtics",
  "simpleName": "Celtics",
  "location": "Boston"
},
{
  "teamId": 1610612751,
  "abbreviation": "BRK",
  "teamName": "Brooklyn Nets",
  "value": "Brooklyn Nets", 
  "label": "Brooklyn Nets",
  "simpleName": "Nets",
  "location": "Brooklyn"
},
{
  "teamId": 1610612766,
  "abbreviation": "CHO",
  "value": "Charlotte Hornets", 
  "label": "Charlotte Hornets",
  "simpleName": "Hornets",
  "location": "Charlotte"
},
{
  "teamId": 1610612741,
  "abbreviation": "CHI",
  "value": "Chicago Bulls", 
  "label": "Chicago Bulls",
  "simpleName": "Bulls",
  "location": "Chicago"
},
{
  "teamId": 1610612739,
  "abbreviation": "CLE",
  "value": "Cleveland Cavaliers", 
  "label": "Cleveland Cavaliers",
  "simpleName": "Cavaliers",
  "location": "Cleveland"
},
{
  "teamId": 1610612742,
  "abbreviation": "DAL",
  "value": "Dallas Mavericks", 
  "label": "Dallas Mavericks",
  "simpleName": "Mavericks",
  "location": "Dallas"
},
{
  "teamId": 1610612743,
  "abbreviation": "DEN",
  "value": "Denver Nuggets", 
  "label": "Denver Nuggets",
  "simpleName": "Nuggets",
  "location": "Denver"
},
{
  "teamId": 1610612765,
  "abbreviation": "DET",
  "value": "Detroit Pistons", 
  "label": "Detroit Pistons",
  "simpleName": "Pistons",
  "location": "Detroit"
},
{
  "teamId": 1610612744,
  "abbreviation": "GSW",
  "value": "Golden State Warriors", 
  "label": "Golden State Warriors",
  "simpleName": "Warriors",
  "location": "Golden State"
},
{
  "teamId": 1610612745,
  "abbreviation": "HOU",
  "value": "Houston Rockets", 
  "label": "Houston Rockets",
  "simpleName": "Rockets",
  "location": "Houston"
},
{
  "teamId": 1610612754,
  "abbreviation": "IND",
  "value": "Indiana Pacers", 
  "label": "Indiana Pacers",
  "simpleName": "Pacers",
  "location": "Indiana"
},
{
  "teamId": 1610612746,
  "abbreviation": "LAC",
  "value": "Los Angeles Clippers", 
  "label": "Los Angeles Clippers",
  "simpleName": "Clippers",
  "location": "Los Angeles"
},
{
  "teamId": 1610612747,
  "abbreviation": "LAL",
  "value": "Los Angeles Lakers", 
  "label": "Los Angeles Lakers",
  "simpleName": "Lakers",
  "location": "Los Angeles"
},
{
  "teamId": 1610612763,
  "abbreviation": "MEM",
  "value": "Memphis Grizzlies", 
  "label": "Memphis Grizzlies",
  "simpleName": "Grizzlies",
  "location": "Memphis"
},
{
  "teamId": 1610612748,
  "abbreviation": "MIA",
  "value": "Miami Heat", 
  "label": "Miami Heat",
  "simpleName": "Heat",
  "location": "Miami"
},
{
  "teamId": 1610612749,
  "abbreviation": "MIL",
  "value": "Milwaukee Bucks", 
  "label": "Milwaukee Bucks",
  "simpleName": "Bucks",
  "location": "Milwaukee"
},
{
  "teamId": 1610612750,
  "abbreviation": "MIN",
  "value": "Minnesota Timberwolves", 
  "label": "Minnesota Timberwolves",
  "simpleName": "Timberwolves",
  "location": "Minnesota"
},
{
  "teamId": 1610612740, 
  "abbreviation": "NOP",
  "value": "New Orleans Pelicans", 
  "label": "New Orleans Pelicans",
  "simpleName": "Pelicans",
  "location": "New Orleans"
},
{
  "teamId": 1610612752,
  "abbreviation": "NYK",
  "value": "New York Knicks", 
  "label": "New York Knicks",
  "simpleName": "Knicks",
  "location": "New York"
},
{
  "teamId": 1610612760,
  "abbreviation": "OKC",
  "value": "Oklahoma City Thunder", 
  "label": "Oklahoma City Thunder",
  "simpleName": "Thunder",
  "location": "Oklahoma City"
},
{
  "teamId": 1610612753,
  "abbreviation": "ORL",
  "value": "Orlando Magic", 
  "label": "Orlando Magic",
  "simpleName": "Magic",
  "location": "Orlando"
},
{
  "teamId": 1610612755,
  "abbreviation": "PHI",
  "value": "Philadelphia 76ers", 
  "label": "Philadelphia 76ers",
  "simpleName": "76ers",
  "location": "Philadelphia"
},
{
  "teamId": 1610612756,
  "abbreviation": "PHO",
  "value": "Phoenix Suns", 
  "label": "Phoenix Suns",
  "simpleName": "Suns",
  "location": "Phoenix"
},
{
  "teamId": 1610612757,
  "abbreviation": "POR",
  "value": "Portland Trail Blazers", 
  "label": "Portland Trail Blazers",
  "simpleName": "Trail Blazers",
  "location": "Portland"
},
{
  "teamId": 1610612758,
  "abbreviation": "SAC",
  "value": "Sacramento Kings", 
  "label": "Sacramento Kings",
  "simpleName": "Kings",
  "location": "Sacramento"
},
{
  "teamId": 1610612759,
  "abbreviation": "SAS",
  "value": "San Antonio Spurs", 
  "label": "San Antonio Spurs",
  "simpleName": "Spurs",
  "location": "San Antonio"
},
{
  "teamId": 1610612761,
  "abbreviation": "TOR",
  "value": "Toronto Raptors", 
  "label": "Toronto Raptors",
  "simpleName": "Raptors",
  "location": "Toronto"
},
{
  "teamId": 1610612762,
  "abbreviation": "UTA",
  "value": "Utah Jazz", 
  "label": "Utah Jazz",
  "simpleName": "Jazz",
  "location": "Utah"
},
{
  "teamId": 1610612764,
  "abbreviation": "WAS",
  "value": "Washington Wizards", 
  "label": "Washington Wizards",
  "simpleName": "Wizards",
  "location": "Washington"
}
]

# Connect to the MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Loop through the JSON data and update the "teamId" based on "abbreviation"
for entry in data:
    team_id = entry["teamId"]
    abbreviation = entry["abbreviation"]

    # SQL query to update the "teamId" based on "abbreviation"
    update_query = "UPDATE predsport.stats2024 SET TeamId = %s WHERE TM = %s"

    # Execute the query
    cursor.execute(update_query, (team_id, abbreviation))
    conn.commit()

# Close the database connection
cursor.close()
conn.close()