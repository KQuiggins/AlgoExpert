const TEAM_WON = 1;
let competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]

let results = [0, 0, 1]


function tournamentWinner(competitions, results) {
    let currentBestTeam = "";
    let scores = {currentBestTeam: 0};

    for (let i = 0; i < competitions.length; i++) {
        const result = results[i];
        const [homeTeam, awayTeam] = competitions[i];
        //console.log(result, homeTeam, awayTeam);

        const winningTeam = result === TEAM_WON ? homeTeam : awayTeam;
        console.log(winningTeam);

        updateScores(winningTeam, 3, scores);

        if (scores[winningTeam] > scores[currentBestTeam]) {
            currentBestTeam = winningTeam;
        }

    }
    return currentBestTeam;

  }

function updateScores(team, points, scores) {
    if (!(team in scores)) scores[team] = 0;
    scores[team] += points;

    return scores;
}

console.log(tournamentWinner(competitions, results));

