import csv
import dateutil.parser as dp

def getDateInfo(csvfile):
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

def main():
    filename = "data/QueryResults.csv"
    javafilename = "data/JavaQueryResults.csv"

    print("average time open (all):", getDateInfo(open(filename)))
    print("average time open (java):", getDateInfo(open(javafilename)))


if __name__=="__main__":
    main()