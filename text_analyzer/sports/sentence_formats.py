import random

# team_sport win/lose
def win_lose_world(sport: str, team1: str, team2: str, margin: str, match: str, cat: str):
    
    ranking1, ranking2 = random.sample(['1', '2', '3', '4', '5'], 2)
    team1 = random.sample([team1, f"World no . {ranking1} {team1}"], 1)[0]
    team2 = random.sample([team2 ,f"world no . {ranking2} {team2}"], 1)[0]
    if cat=='team':
        beat_word = random.sample(['beat', 'thrash', 'pip'], 1)[0]
    elif cat=='player':
        beat_word = random.sample(['beats', 'thrashes', 'pips'], 1)[0]
    match_word = random.sample([' to clinch', ' to win'], 1)[0]
    sport_addition = random.sample([f'{sport} : ', ''],1)[0]
    margin_addition = random.sample([margin, ''], 1)[0]
    match_addition = random.sample([match, ''], 1)[0]
    while match_addition=='' and margin_addition=='':
        margin_addition = random.sample([margin, ''], 1)[0]
        match_addition = random.sample([match, ''], 1)[0]
    gt = ''
    
    len_sport_addition = len(sport_addition.strip().split(" "))
    
    if len(sport_addition)>0: 
        gt += 'B-S '
        len_sport_addition -= 1
        while len_sport_addition>1:
            gt += 'I-S '
            len_sport_addition -= 1
        gt += 'O '  # :

    len_team1 = len(team1.strip().split(' '))
    if team1.lower().startswith('world'):
        gt += 'O O O '
        len_team1 -= 3

    gt += 'B-WT '
    len_team1 -= 1
    while len_team1>0:
        gt += 'I-WT '
        len_team1 -= 1
    
    
    gt += 'O '      # {beat_word}

    len_team2 = len(team2.strip().split(' '))
    if team2.lower().startswith('world'):
        gt += 'O O O '
        len_team2 -= 3

    gt += 'B-LT '
    len_team2 -= 1
    while len_team2>0:
        gt += 'I-LT '
        len_team2 -= 1

    if len(margin_addition)>0:
        len_margin = len(margin.strip().split(' '))
   
        # margin or (G)ap
        gt += 'B-G '
        len_margin -= 1
        while len_margin>0:
            gt += 'I-G '
            len_margin -= 1

        margin_addition = ' ' + margin
    
    if len(match_addition)>0:
        gt += 'O O '    # to {match_word}

        len_match = len(match.strip().split(' '))
        gt += 'B-M '
        len_match -= 1
        while len_match>0:
            gt += 'I-M '
            len_match -= 1
        match_addition = match_word + ' ' + match

    gt += 'O'       # .

    output = f"{sport_addition}{team1} {beat_word} {team2}{margin_addition}{match_addition} ."

    return output, gt


# team sport draw
def draw_world(sport: str, team1: str, team2: str, margin: str, match: str, cat: str):
    sport_addition = random.sample([f'{sport} : ', ''],1)[0]
    ranking = random.sample(['1', '2', '3', '4', '5'], 1)[0]
    adj1 = random.sample(['A resilient ', 'A buoyant ', '', f"World no . {ranking} "], 1)[0]
    adj2 = ''
    if len(adj1)==0:
        adj2 = random.sample(['a resilient ', 'a buoyant ', '', f"world no . {ranking} "], 1)[0]
    
    margin_addition = random.sample([margin + ' ',''], 1)[0]
    match_addition = random.sample([f'in {match} ' ,''], 1)[0]
    
    gt = ''
    
    if len(sport_addition)>0: 
        len_sport = len(sport.strip().split(" "))
        gt += 'B-S '
        len_sport -= 1
        while len_sport>0:
            gt += 'I-S '
            len_sport -= 1
        gt += 'O '          # :
    
    if len(adj1)>0:
        len_adj1 = len(adj1.strip().split(' '))
        while len_adj1>0:
            gt += 'O '      # a resilient / world no. 3
            len_adj1 -= 1
    
    len_team1 = len(team1.strip().split(' '))
    gt += 'B-WT '
    len_team1 -= 1
    while len_team1>0:
        gt += 'I-WT '
        len_team1 -= 1
    
    gt += 'O O O '      # play out a 

    if len(margin_addition)>0:
        len_margin = len(margin.strip().split(' '))
   
        # margin or (G)ap
        gt += 'B-G '
        len_margin -= 1
        while len_margin>0:
            gt += 'I-G '
            len_margin -= 1

    gt += 'O O '            # draw against

    if len(adj2)>0:
        len_adj2 = len(adj2.strip().split(' '))
        while len_adj2>0:
            gt += 'O '      # a resilient / world no. 3
            len_adj2 -= 1
    
    len_team2 = len(team2.strip().split(' '))
    gt += 'B-WT '
    len_team2 -= 1
    while len_team2>0:
        gt += 'I-WT '
        len_team2 -= 1
    
    if len(match_addition)>0:
        gt += 'O '      # in
        
        len_match = len(match.strip().split(' '))
   
        # margin or (G)ap
        gt += 'B-G '
        len_match -= 1
        while len_match>0:
            gt += 'I-G '
            len_match -= 1

    gt += 'O '      # .
    if cat=='team':
        output = f"{sport_addition}{adj1}{team1} play out a {margin_addition}draw against {adj2}{team2} {match_addition}."
    
    elif cat=='player':
        output = f"{sport_addition}{adj1}{team1} plays out a {margin_addition}draw against {adj2}{team2} {match_addition}."
    
    return output, gt

def win_lose_regional(sport: str, team1: str, team2: str, margin: str, match: str, cat: str):

    team1 = random.sample([team1, team1], 1)[0]
    team2 = random.sample([team2 ,team2], 1)[0]
    if cat=='team':
        beat_word = random.sample(['beat', 'thrash', 'pip'], 1)[0]
    elif cat=='player':
        beat_word = random.sample(['beats', 'thrashes', 'pips'], 1)[0]
    match_word = random.sample([' to clinch', ' to win'], 1)[0]
    sport_addition = random.sample([f'{sport} : ', ''],1)[0]
    margin_addition = random.sample([margin, ''], 1)[0]
    match_addition = random.sample([match, ''], 1)[0]

    gt = ''
    
    len_sport_addition = len(sport_addition.strip().split(" "))
    
    if len(sport_addition)>0: 
        gt += 'B-S '
        len_sport_addition -= 1
        while len_sport_addition>1:
            gt += 'I-S '
            len_sport_addition -= 1
        gt += 'O '  # :

    len_team1 = len(team1.strip().split(' '))
    gt += 'B-WT '
    len_team1 -= 1
    while len_team1>0:
        gt += 'I-WT '
        len_team1 -= 1
    
    
    gt += 'O '      # {beat_word}

    len_team2 = len(team2.strip().split(' '))
    gt += 'B-LT '
    len_team2 -= 1
    while len_team2>0:
        gt += 'I-LT '
        len_team2 -= 1

    if len(margin_addition)>0:
        len_margin = len(margin.strip().split(' '))

        # margin or (G)ap
        gt += 'B-G '
        len_margin -= 1
        while len_margin>0:
            gt += 'I-G '
            len_margin -= 1

        margin_addition = ' ' + margin
    
    if len(match_addition)>0:
        gt += 'O O '        # to {match_word}

        len_match = len(match.strip().split(' '))
        gt += 'B-M '
        len_match -= 1
        while len_match>0:
            gt += 'I-M '
            len_match -= 1
        match_addition = match_word + ' ' + match

    gt += 'O'       # .

    output = f"{sport_addition}{team1} {beat_word} {team2}{margin_addition}{match_addition} ."

    return output, gt


def draw_regional(sport: str, team1: str, team2: str, margin: str, match: str, cat: str):
    
    sport_addition = random.sample([f'{sport} : ', ''],1)[0]
    adj1 = random.sample(['A resilient ', 'A buoyant ', ''], 1)[0]
    adj2 = ''
    if len(adj1)==0:
        adj2 = random.sample(['a resilient ', 'a buoyant ', ''], 1)[0]
    
    margin_addition = random.sample([margin + ' ',''], 1)[0]
    match_addition = random.sample([f'in {match} ' ,''], 1)[0]
    
    gt = ''
    
    
    if len(sport_addition)>0: 
        len_sport = len(sport.strip().split(" "))
        gt += 'B-S '
        len_sport -= 1
        while len_sport>0:
            gt += 'I-S '
            len_sport -= 1
        gt += 'O '          # :
    
    if len(adj1)>0:
        len_adj1 = adj1.strip().split(' ')
        while len_adj1>0:
            gt += 'O '      # a resilient
            len_adj1 -= 1
    
    len_team1 = len(team1.strip().split(' '))
    gt += 'B-WT '
    len_team1 -= 1
    while len_team1>0:
        gt += 'I-WT '
        len_team1 -= 1
    
    gt += 'O O O '      # play out a 

    if len(margin_addition>0):
        len_margin = len(margin.strip().split(' '))
   
        # margin or (G)ap
        gt += 'B-G '
        len_margin -= 1
        while len_margin>0:
            gt += 'I-G '
            len_margin -= 1

    gt += 'O O '            # draw against

    if len(adj2)>0:
        len_adj2 = adj2.strip().split(' ')
        while len_adj2>0:
            gt += 'O '      # a resilient
            len_adj2 -= 1
    
    len_team2 = len(team2.strip().split(' '))
    gt += 'B-WT '
    len_team2 -= 1
    while len_team2>0:
        gt += 'I-WT '
        len_team2 -= 1
    
    if len(match_addition>0):
        gt += 'O '      # in
        
        len_match = len(match.strip().split(' '))
   
        # margin or (G)ap
        gt += 'B-G '
        len_match -= 1
        while len_match>0:
            gt += 'I-G '
            len_match -= 1

    if cat=='team':
        output = f"{adj1}{team1} play out a {margin_addition}draw against {adj2}{team2} {match_addition}."
    
    elif cat=='player':
        output = f"{adj1}{team1} plays out a {margin_addition}draw against {adj2}{team2} {match_addition}."
    
    return output, gt