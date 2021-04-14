import os
import random
from sentence_formats import draw_world, win_lose_world
import sentence_formats
import sys

def get_list(path):

    items = []
    f = open(path, 'r')
    for line in f.readlines():
        items.append(line.strip())

    return items

def get_player_names(path):

    items = []
    f = open(path, 'r')
    for line in f.readlines():
        items.append(line.strip().split(',')[0])

    return items

def main():
    sports = ['Cricket', 'Hockey', 'Tennis']

    get_world_cricket_sentences(200)

    # get_regional_cricket_sentences(25)

    get_world_tennis_sentences(200)

    get_world_hockey_sentences(300)

def get_world_cricket_sentences(count):

    output_path = "data.txt"
    output_gt_path = "data_gt.txt"

    teams = get_list('raw_data/cricket_teams_national.txt')
    tournaments = get_list('raw_data/cricket_matches.txt')

    specific = get_list('raw_data/cricket_matches_regional.txt')
    spl_tournaments = []
    spl_teams = []
    for s in specific:
        t, team1, team2 = s.strip().split(',')
        spl_tournaments.append(t)
        spl_teams.append((team1, team2))

    teams_done = set()
    tournaments_done = set()

    done = 0
    while done < count:
        team1, team2 = random.sample(teams, 2)
        while (team1 in teams_done or \
            team2 in teams_done) and \
                len(teams_done) < int(len(teams)/2)*2:
            team1, team2 = random.sample(teams, 2)

        teams_done.add(team1)
        teams_done.add(team2)

        if (team1, team2) in spl_teams:
            t = spl_tournaments[spl_teams.index((team1, team2))]
        
        elif (team2, team1) in spl_teams:
            t = spl_tournaments[spl_teams.index((team2, team1))]
        
        else:
            t = random.sample(tournaments, 1)[0]
            while t in tournaments_done and \
                len(tournaments_done) < len(tournaments):
                t = random.sample(tournaments, 1)[0]

            tournaments_done.add(t)

        margin_runs = f"by {random.sample(range(2, 78, 3),1)[0]} runs"
        margin_wickets = f"by {random.sample(range(2, 10), 1)[0]} wickets"
        margin = random.sample([margin_wickets, margin_runs], 1)[0]

        sentence, gt = win_lose_world('Cricket', team1, team2, margin, t, 'team')

        with open(output_path, "a") as f:
            f.write(sentence+'\n')

        with open(output_gt_path, "a") as f:
            f.write(gt+'\n')
        done += 1
    print(f"Added {count} world cricket sentences to {output_path} & {output_gt_path}")
    return

def get_regional_cricket_sentences(count):
    pass

def get_world_tennis_sentences(count):

    output_path = "data.txt"
    output_gt_path = "data_gt.txt"

    players = get_player_names('raw_data/tennis_players.txt')
    tournaments = get_list('raw_data/tennis_matches.txt')

    players_done = set()
    tournaments_done = set()

    done = 0
    while done < count:
        p1, p2 = random.sample(players, 2)
        while (p1 in players_done or \
            p2 in players_done) and \
                len(players_done) < int(len(players)/2)*2:
            p1, p2 = random.sample(players, 2)

        players_done.add(p1)
        players_done.add(p2)

        t = random.sample(tournaments, 1)[0]
        while t in tournaments_done and \
            len(tournaments_done) < len(tournaments):
            t = random.sample(tournaments, 1)[0]

        tournaments_done.add(t)

        score = random.sample(range(1,6), 1)[0]
        if score>2:
            lower_score = 5 - score
            higher_score = score
        else:
            lower_score = score
            higher_score = 5 - score

        margin = f"{higher_score} - {lower_score}"

        sentence, gt = win_lose_world('Tennis', p1, p2, margin, t, 'player')

        with open(output_path, "a") as f:
            f.write(sentence+'\n')

        with open(output_gt_path, "a") as f:
            f.write(gt+'\n')

        done += 1

    print(f"Added {count} world tennis sentences to {output_path} & {output_gt_path}")
    return

def get_world_hockey_sentences(count):

    output_path = "data.txt"
    output_gt_path = "data_gt.txt"

    teams = get_list('raw_data/hockey_teams.txt')
    tournaments = get_list('raw_data/hockey_matches.txt')
    # print(teams)
    # exit()
    teams_done = set()
    tournaments_done = set()

    done = 0
    while done < count:
        team1, team2 = random.sample(teams, 2)
        while (team1 in teams_done or \
            team2 in teams_done) and \
                len(teams_done) < int(len(teams)/2)*2:
            team1, team2 = random.sample(teams, 2)

        teams_done.add(team1)
        teams_done.add(team2)

        t = random.sample(tournaments, 1)[0]
        while t in tournaments_done and \
            len(tournaments_done) < len(tournaments):
            t = random.sample(tournaments, 1)[0]

        tournaments_done.add(t)

        higher_score = random.sample(range(2,7), 1)[0]
        lower_score = random.sample(range(1, higher_score), 1)[0]

        draw_score = random.sample([higher_score, lower_score], 1)[0]

        margin_win = f"{higher_score} - {lower_score}"
        margin_draw = f"{draw_score} - {draw_score}"

        margin = random.sample([margin_win, margin_draw], 1)[0]
        if margin==margin_draw:
            sentence, gt = draw_world('Hockey', team1, team2, margin, t, 'team')
        else:
            sentence, gt = win_lose_world('Cricket', team1, team2, margin, t, 'team')

        with open(output_path, "a") as f:
            f.write(sentence+'\n')

        with open(output_gt_path, "a") as f:
            f.write(gt+'\n')

        done += 1
    print(f"Added {count} world hockey sentences to {output_path} & {output_gt_path}")
    pass

if __name__=='__main__':
    main()
