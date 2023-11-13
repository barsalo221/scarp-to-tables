data = [{'teamId': 1610612737, 'abbreviation': 'ATL'}, {'teamId': 1610612738, 'abbreviation': 'BOS'}, {'teamId': 1610612751, 'abbreviation': 'BRK'}, {'teamId': 1610612766, 'abbreviation': 'CHO'}, {'teamId': 1610612741, 'abbreviation': 'CHI'}, {'teamId': 1610612739, 'abbreviation': 'CLE'}, {'teamId': 1610612742, 'abbreviation': 'DAL'}, {'teamId': 1610612743, 'abbreviation': 'DEN'}, {'teamId': 1610612765, 'abbreviation': 'DET'}, {'teamId': 1610612744, 'abbreviation': 'GSW'}, {'teamId': 1610612745, 'abbreviation': 'HOU'}, {'teamId': 1610612754, 'abbreviation': 'IND'}, {'teamId': 1610612746, 'abbreviation': 'LAC'}, {'teamId': 1610612747, 'abbreviation': 'LAL'}, {'teamId': 1610612763, 'abbreviation': 'MEM'}, {'teamId': 1610612748, 'abbreviation': 'MIA'}, {'teamId': 1610612749, 'abbreviation': 'MIL'}, {'teamId': 1610612750, 'abbreviation': 'MIN'}, {'teamId': 1610612740, 'abbreviation': 'NOP'}, {'teamId': 1610612752, 'abbreviation': 'NYK'}, {'teamId': 1610612760, 'abbreviation': 'OKC'}, {'teamId': 1610612753, 'abbreviation': 'ORL'}, {'teamId': 1610612755, 'abbreviation': 'PHI'}, {'teamId': 1610612756, 'abbreviation': 'PHO'}, {'teamId': 1610612757, 'abbreviation': 'POR'}, {'teamId': 1610612758, 'abbreviation': 'SAC'}, {'teamId': 1610612759, 'abbreviation': 'SAS'}, {'teamId': 1610612761, 'abbreviation': 'TOR'}, {'teamId': 1610612762, 'abbreviation': 'UTA'}, {'teamId': 1610612764, 'abbreviation': 'WAS'}]





team_id_abbreviation_list = [{"teamId": entry["teamId"], "abbreviation": entry["abbreviation"]} for entry in data]

# Print the new list
print(team_id_abbreviation_list)
