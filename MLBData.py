def main():
  myFile = open("MLB_Pitching.csv", 'r')
  teamData = []
  for line in myFile:
    pitchingData = line.split(",")
    name = pitchingData[0]
    runs_allowed = pitchingData[3]
    wins = pitchingData[4]
    losses = pitchingData[5]
    era = pitchingData[7]
    teamData.append([name, "", runs_allowed, wins, losses, era])


  myFile.close()

  battingFile = open("MLB_Hitting.csv", 'r')

  teamCount = 0
  for line in battingFile:
    battingData = line.split(",")
    runs_scored = battingData[3]
    #print(runs_scored)
    teamData[teamCount][1] = runs_scored
    #print(teamData[teamCount])
    teamCount = teamCount + 1


  battingFile.close()
  
  outFile = open("mlboutput.csv", 'w')

  for line in teamData:
    output = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "\n"
    outFile.write(output)

  outFile.close()


if __name__ == '__main__':
  main()