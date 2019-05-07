import csv
import dateutil.parser as dp

def getTimeInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    opendate = -1
    closedate = -1
    totaltime = 0
    totalposts = 0

    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            opendate = headers.index("CreationDate")
            closedate = headers.index("ClosedDate")
            firstLine = False
        else:
            closed = row[closedate]
            if closed != "":
                opened = dp.parse(row[opendate])
                closed = dp.parse(row[closedate])

                diff = closed - opened
                if totaltime == 0:
                    totaltime = diff
                # print(opened, "\t-\t", closed, "\t=\t", diff)

                totaltime += diff
                totalposts += 1

    return totaltime / totalposts



def getRepInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    userid = -1
    rep = -1

    users = {}

    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            # print(row)
            userid = headers.index("UserId")
            rep = headers.index("Reputation")
            firstLine = False
        else:
            users[row[userid]] = row[rep]

    # print(users)

    vals = [int(x) for x in users.values()]

    return sum(vals) / len(vals), max(vals), min(vals)