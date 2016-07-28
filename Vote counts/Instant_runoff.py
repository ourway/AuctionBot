import csv
exampleFile = open('the_toifile_forapproval_19removed.csv')          # open the file and store it in a file object
exampleReader = csv.reader(exampleFile)     # a reader object is created and the file object is passed to the fn
# exampleData = list(exampleReader)           # to create it and then the reader object is now laid out as a list
candidates = []
newfile = 'untitled_new.csv'
newfile2 = 'untitled_new2.csv'
with open(newfile, 'wb') as fp:
    for row in exampleReader:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(row)
exampleFile.seek(0) # reset the row pointer of original file
with open(newfile2, 'wb') as xp:
    for row in exampleReader:
        wr = csv.writer(xp, dialect='excel')
        wr.writerow(row)
# now newfile and newfile2 have the same data and also reset the row pointer of original file
exampleFile.seek(0)

#print open(newfile).read()

for i in range(12):     #for 11 candidates make it range(12)
    candidates.append(0)
for row in exampleReader:
    #print row
    for m in range(int(row[0])):
        i = int(row[1])
        candidates[i] = candidates[i]+1
        candidates[0]=candidates[0]+1
indexmax = 1
#print candidates
for i in range(1, 11): #for 11 candidates make it range(1, 11)
    if candidates[indexmax] < candidates[i+1]:
        indexmax = i+1
        #else:
            #index.append()
        # print(row[0])
eliminated = []
print "The highest candidate is in the first round is #" + str(indexmax) + " with a voteshare of " + str(100.0*candidates[indexmax]/candidates[0])
iterationnumber=0
while(100.0*candidates[indexmax]/candidates[0])<=50.0:

    # eliminate the the last candidate
    #print "current votes stand at " + str(candidates)
    #print str(candidates)
    #print eliminated
    indexmin = 1
    i=1
    elim = set(eliminated)
    for i in range(1,11): #for 11 candidates make it i<11
        b=i+1
        if indexmin in eliminated:
            indexmin+=1
        if (i in elim):
            i+=1
            b=i+1
        while (b in elim):
            b = b+1
        if b<=11:
            if candidates[indexmin] > candidates[b]:
                indexmin = b
                i+=1


    #removecandidate = indexmin
    #print "we are going to eliminate " + str(indexmin)
    #print indexmin

    candidates[indexmin] = 0 # make this candidates vote 0
    eliminated.append(indexmin)
    iterationnumber+=1
    exampleFile.seek(0)
    open(newfile).seek(0)
    open(newfile2).seek(0)
    #exampleReader = csv.reader(open(newfile))
    with open(newfile, 'wb') as fp:
        for row in csv.reader(open(newfile2)):
            newrow = []
            newrow.append(row[0])
            for h in range(int(row[0])):
                #print len(row)
                #print row
                #if not (row[2]=='' ):
                if len(row)>2:
                    if not (row[1]==''):
                        if int(row[1]) == indexmin:
                            if not (row[2]=='' ):
                                candidates[int(row[2])]+=1  #transfer the votes
            for t in range(1,len(row)):

                if row[t] == '':
                    #print "this is the " + row
                    pass
                elif (int(row[t]) in eliminated):
                        pass
                else:
                    newrow.append(row[t])   #eliminate the candidate
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(newrow)
            #print newrow
    open(newfile).seek(0)
    open(newfile2).seek(0)
    #print "Post elimination current votes stand at " + str(candidates)
    with open(newfile2, 'wb') as xp:
        for row in csv.reader(open(newfile)):
            wr = csv.writer(xp, dialect='excel')
            wr.writerow(row)


indexmax = 1
#print candidates
for i in range(1, 11): #for 11 candidates make it range(1, 11)
    if candidates[indexmax] < candidates[i+1]:
        indexmax = i+1
        #else:
            #index.append()
        # print(row[0])


#print(open('untitled_new.csv').read())
#print "the candidate to eliminate is " + str(indexmin)
print "Total rounds of elimination = " + str(iterationnumber)
print "Winner by Instant Runoff Vote is candidate #" + str(indexmax) + " and hw wins by a majority of  " + str(float(100.0*candidates[indexmax]/candidates[0])) + "%"
#print candidates


