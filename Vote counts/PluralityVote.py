import csv
exampleFile = open('the_toifile_forapproval_19_firstlines_removed_.csv')          # open the file and store it in a file object
# exampleFile = open('testdata.csv')
exampleReader = csv.reader(exampleFile)     # a reader object is created and the file object is passed to the fn
# exampleData = list(exampleReader)           # to create it and then the reader object is now laid out as a list
candidates = []
for i in range(12):
    candidates.append(0)
# print exampleData
for row in exampleReader:
    for m in range(int(row[0])):
        i = int(row[1])
        candidates[i] = candidates[i]+1
        candidates[0]=candidates[0]+1
indexmax = 1
for i in range(1, 11):
    if candidates[indexmax] < candidates[i+1]:
        indexmax = i+1
        #else:
            #index.append()
        # print(row[0])


print "Winner by Plurality Vote is candidate #" + str(indexmax) + " and his vote share is " + str(float(100.0*candidates[indexmax]/candidates[0])) + "%"
print candidates


