def main():
  myFile = open("Covid-19", 'r')

  for line in myFile:
    info = line.split(",")
    td = info[12]
    name = info[0]
    rating = info[1]
    print (name, "had a rating of", rating, "and threw", td, "touchdowns.")

  myFile.close()


if __name__ == '__main__':
  main()
