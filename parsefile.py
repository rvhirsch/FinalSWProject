import csv
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
            score = headers.index("UpVotes")
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
            score = headers.index("DownVotes")
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


def CountKeyWords(csvfile):
    csvreader = csv.reader(csvfile, delimiter=",")

    KeyWord = 1
    KeyWords = ['python', 'java', 'c++', 'scala']
    firstLine = True
    for row in csvreader:
        if firstLine:
            headers = row
            score = headers.index("Body")
            firstLine = False
        else:
            comment = str(row[KeyWord])
            comment_split = comment.split()
            CounterWords = Counter(comment_split)
            Keywords = CounterWords.most_common(2)

    return Keywords



def main():
    print(getAnswersInfo(open("data/PytorchQueryResults.csv")))

if __name__ == '__main__':
    main()