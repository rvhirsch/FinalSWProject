import csv
import re
import dateutil.parser as dp
from collections import Counter

def getTimeInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    opendate = -1
    closedate = -1

    times = []

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
                times.append(diff)
    return times

def getRepInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    userid = -1
    rep = -1

    users = {}

    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            userid = headers.index("UserId")
            rep = headers.index("Reputation")
            firstLine = False
        else:
            users[row[userid]] = row[rep]
    return [int(x) for x in users.values()]

def getAnswersInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    answercount = -1

    answers = []

    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            answercount = headers.index("AnswerCount")
            firstLine = False
        else:
            count = int(row[answercount])
            answers.append(count)
    return answers

def getCommentsInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    commentcount = -1
    comments = []

    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            commentcount = headers.index("CommentCount")
            firstLine = False
        else:
            count = int(row[commentcount])
            comments.append(count)
    return comments

def getScoreInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    score = -1
    # minans = 100000000000
    # maxans = -1
    # totalans = 0
    # totalposts = 0

    scores = []

    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            score = headers.index("Score")
            firstLine = False
        else:
            count = int(row[score])
            scores.append(count)
            # if count > maxans:
            #     maxans = count
            # elif count < minans:
            #     minans = count
            # totalans += count
            # totalposts += 1

    # return totalans / totalposts, maxans, minans
    return scores


def UpVotesInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    UpVote = -1
    UpVotes = []
    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            UpVote = headers.index("UpVotes")
            firstLine = False
        else:
            countVote = int(row[UpVote])
            UpVotes.append(countVote)
            # if count > maxans:
            #     maxans = count
            # elif count < minans:
            #     minans = count
            # totalans += count
            # totalposts += 1

    # return totalans / totalposts, maxans, minans
    return UpVotes


def DownVotesInfo(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    DownVote = -1
    DownVotes = []
    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            DownVote = headers.index("DownVotes")
            firstLine = False
        else:
            countVote = int(row[DownVote])
            DownVotes.append(countVote)
            # if count > maxans:
            #     maxans = count
            # elif count < minans:
            #     minans = count
            # totalans += count
            # totalposts += 1

    # return totalans / totalposts, maxans, minans
    return DownVotes


def cleanhtml(row):
    currstr = str(row)
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', currstr)
    # rowstr = re.sub('\W+ ', '', cleantext)
    rowstr = "".join([x for x in cleantext if x.isalnum() or x == " "])
    return rowstr

def checkifsmall(x):
    # return x != "the" and x != "to" and x != "I" and x != "a" and x != "of" and x != "in" and x != "is" and x != "and" and x != "with" and x != "for" and x != "as" and x != "this" and x != "my" and x != "have"
    return len(x) > 5

def removesmallwords(allwords):
    return [x for x in allwords if checkifsmall(x)]


def CountKeyWords(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    body = -1
    # KeyWord = 1
    # KeyWords = ['python', 'java', 'c++', 'scala']
    allwords = []
    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            body = headers.index("Body")
            firstLine = False
        else:
            newwords = removesmallwords(cleanhtml(row[body].lower()).split())
            allwords.extend(newwords)

    CounterWords = Counter(allwords)
    Keywords = CounterWords.most_common(10)

    return Keywords



def main():
    print(getAnswersInfo(open("data/PytorchQueryResults.csv")))

if __name__ == '__main__':
    main()