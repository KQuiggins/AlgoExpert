CONST_TEAM_WON = 1

def tournamentWinner(competitions, results):


    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        print(idx, competition)
        result = results[idx]
        print(result)
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == CONST_TEAM_WON else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
              currentBestTeam = winningTeam

    return currentBestTeam

def updateScores(team, points, scores):
     if team not in scores:
          scores[team] = 0

     scores[team] += points
     return scores

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]

results = [0, 0, 1]

print(tournamentWinner(competitions, results))

