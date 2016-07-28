import csv
exampleFile = open('the_toifile_forapproval_19removed.csv')
# open the file and store it in a file object
# exampleFile = open('testdata.csv')
exampleReader = csv.reader(exampleFile)      # a reader object is created and the file object is passed to the fn
# exampleData = list(exampleReader)           # to create it and then the reader object is now laid out as a list
candidates = []
# there are a total of 11 candidates so 1st place gets 11 points, 2nd place = 10 points and so on
# every un-ranked candidate is given 1 point as though he came in last
for i in range(12):  # initialize all the vote counts to zero
    candidates.append(0)
# print exampleData
for row in exampleReader:
    for m in range(int(row[0])):
        candidates[0] += 1       #keep track of number of votes
        rowvoter = []
        for z in range(12):
            rowvoter.append(0)
        for x in range(1,len(row)):
            if row[x]:
                i = int(row[x])             # find which candidate is in x place ie at x position
                if i < 12:                  # keeping the range intact for the csv file
                    rowvoter[i] = 1         # only those who have votes get 1 all others are 0
                    candidates[i] += (11-x) # increase this candidates points
        for m in range(1,12):               # giving one point to every candidate that never got a vote
            if rowvoter[m] == 0:
                candidates[m] += 1


index = 1
for i in range(1, 11):
    if candidates[index] < candidates[i+1]:
        index = i+1

print "Winner by Borda Count Vote is candidate #" + str(index) + " with " + str(candidates[index]) + " points!!"
print candidates
# print exampleData[1][1]



