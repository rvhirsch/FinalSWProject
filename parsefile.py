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

def getAvgTimes():
    print("average time open (pytorch):\t", getTimeInfo(open("data/PytorchQueryResults.csv")))
    print("average time open (mxnet):\t\t", getTimeInfo(open("data/MXnetQueryResults.csv")))
    print("average time open (keras):\t\t", getTimeInfo(open("data/KerasQueryResults.csv")))
    print("average time open (tensorflow):\t", getTimeInfo(open("data/TensorflowQueryResults.csv")))
    print("average time open (caffe):\t\t", getTimeInfo(open("data/CaffeQueryResults.csv")))
    print("average time open (Dl4j):\t\t", getTimeInfo(open("data/DL4jQueryResults.csv")))
    print("average time open (dlib):\t\t", getTimeInfo(open("data/DLibQueryResults.csv")))
    print("average time open (theano):\t\t", getTimeInfo(open("data/TheanoQueryResults.csv")))


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

def getAvgReps():
    print("avg/max/min user rep (tensorflow):\t", getRepInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min user rep (keras):\t\t", getRepInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min user rep (pytorch):\t\t", getRepInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min user rep (mxnet):\t\t", getRepInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min user rep (caffe):\t\t", getRepInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min user rep (theano):\t\t", getRepInfo(open("data/TheanoQueryResults.csv")))
    print("avg/max/min user rep (Dl4j):\t\t", getRepInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min user rep (dlib):\t\t", getRepInfo(open("data/DLibQueryResults.csv")))


def main():
    # getAvgTimes()

    getAvgReps()

if __name__=="__main__":
    main()