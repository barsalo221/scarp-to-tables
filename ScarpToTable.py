import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="CRcr240403",database="predsport")
url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", {"id": "per_game_stats"})
headers = [th.text.strip() for th in table.find_all("th")]
rows = []
for tr in table.tbody.find_all("tr"):
    row = [td.text.strip() for td in tr.find_all("td")]
    rows.append(row)
mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE predsport.stats2024")
i=0
for row in rows:
    if rows[i] != [] :
        print("next row is: ")
        # print(row)
        sql = "INSERT INTO predsport.stats2024(Player, Pos, Age, TM, G, GS, MP, FG, FGA, FGP, threeP, threePA, threePP, twoP, twoPA, twoPP, EFGP, FT, FTA, FTP, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS) VALUES" \
              " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = tuple(rows[i])
        mycursor.execute(sql, values)
        mydb.commit()
        i=i+1
    else:
        i=i+1

data = [{'teamId': 1610612737, 'abbreviation': 'ATL'}, {'teamId': 1610612738, 'abbreviation': 'BOS'}, {'teamId': 1610612751, 'abbreviation': 'BRK'}, {'teamId': 1610612766, 'abbreviation': 'CHO'}, {'teamId': 1610612741, 'abbreviation': 'CHI'}, {'teamId': 1610612739, 'abbreviation': 'CLE'}, {'teamId': 1610612742, 'abbreviation': 'DAL'}, {'teamId': 1610612743, 'abbreviation': 'DEN'}, {'teamId': 1610612765, 'abbreviation': 'DET'}, {'teamId': 1610612744, 'abbreviation': 'GSW'}, {'teamId': 1610612745, 'abbreviation': 'HOU'}, {'teamId': 1610612754, 'abbreviation': 'IND'}, {'teamId': 1610612746, 'abbreviation': 'LAC'}, {'teamId': 1610612747, 'abbreviation': 'LAL'}, {'teamId': 1610612763, 'abbreviation': 'MEM'}, {'teamId': 1610612748, 'abbreviation': 'MIA'}, {'teamId': 1610612749, 'abbreviation': 'MIL'}, {'teamId': 1610612750, 'abbreviation': 'MIN'}, {'teamId': 1610612740, 'abbreviation': 'NOP'}, {'teamId': 1610612752, 'abbreviation': 'NYK'}, {'teamId': 1610612760, 'abbreviation': 'OKC'}, {'teamId': 1610612753, 'abbreviation': 'ORL'}, {'teamId': 1610612755, 'abbreviation': 'PHI'}, {'teamId': 1610612756, 'abbreviation': 'PHO'}, {'teamId': 1610612757, 'abbreviation': 'POR'}, {'teamId': 1610612758, 'abbreviation': 'SAC'}, {'teamId': 1610612759, 'abbreviation': 'SAS'}, {'teamId': 1610612761, 'abbreviation': 'TOR'}, {'teamId': 1610612762, 'abbreviation': 'UTA'}, {'teamId': 1610612764, 'abbreviation': 'WAS'}]
# Loop through the JSON data and update the "teamId" based on "abbreviation"
for entry in data:
    team_id = entry["teamId"]
    abbreviation = entry["abbreviation"]

    # SQL query to update the "teamId" based on "abbreviation"
    update_query = "UPDATE predsport.stats2024 SET TeamId = %s WHERE TM = %s"

    # Execute the query
    mycursor.execute(update_query, (team_id, abbreviation))
    mydb.commit()

mydb.commit()
mycursor.close()
mydb.close()