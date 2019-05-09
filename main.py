import parsefile
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

files = {"pytorch":"data/PytorchQueryResults.csv", "MXnet":"data/MXnetQueryResults.csv",
         "keras":"data/KerasQueryResults.csv", "tensorflow":"data/TensorflowQueryResults.csv",
         "caffe":"data/CaffeQueryResults.csv", "DL4j":"data/DL4jQueryResults.csv",
         "DLib":"data/DLibQueryResults.csv", "theano": "data/TheanoQueryResults.csv"}

def convertData(data):
    try:
        newdata = [x.days for x in data]
        return newdata
    except:
        return data

def printstats(function, filename, title):
    times = function(open(filename))
    times = convertData(times)
    print("%-25s AVG: %10.2f  MAX: %10.2f  MIN: %5.2f" % (title, sum(times)/len(times), max(times), min(times)))

def getAvgTimes():
    for name, file in files.items():
        printstats(parsefile.getTimeInfo, file, "time open ("+name+"):")

def getAvgReps():
    for name, file in files.items():
        printstats(parsefile.getRepInfo, file, "reputation ("+name+"):")

def getAvgAnswers():
    for name, file in files.items():
        printstats(parsefile.getAnswersInfo, file, "num ans ("+name+"):")

def getAvgComments():
    for name, file in files.items():
        printstats(parsefile.getCommentsInfo, file, "num comments ("+name+"):")

def getAvgScore():
    for name, file in files.items():
        printstats(parsefile.getScoreInfo, file, "score ("+name+"):")

def getAvgUpVotes():
    for name, file in files.items():
        printstats(parsefile.UpVotesInfo, file, "UpVotes ("+name+"):")

def getAvgDownVotes():
    for name, file in files.items():
        printstats(parsefile.UpVotesInfo, file, "UpVotes ("+name+"):")

def prettyprintKeywords(keywords):
    return " ".join(["{:25}".format(str(x)) for x in keywords])

def getKeyWords():
    for name, file in files.items():
        print("Most common words used in (" + name + "):\t\t",
              prettyprintKeywords(parsefile.CountKeyWords(open(file))))

def graphStats(getfunction, title, ax):
    datatoplot = []

    for name, file in files.items():
        times = getfunction(open(file))
        datatoplot.append(convertData(times))

    ax.boxplot(datatoplot)
    # ax.set_xticklabels(["PyTorch", "Tensorflow", "MXnet", "Keras", "Caffe", "DL4j", "DLib", "Theano"], rotation=45)
    ax.set_xticklabels(files.keys(), rotation=45)
    ax.set_title(title)

def graphWords(text, ax, title):
    wordcloud = WordCloud(background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    ax.set_title("~"+title+"~", fontsize=50)
    # plt.show()

def plotfig1():
    plt.figure(1, figsize=(20, 10))

    ax = plt.subplot(2, 4, 1)
    graphStats(parsefile.getTimeInfo, "Amt Time Open", ax)
    print("Done *")

    ax = plt.subplot(2, 4, 2)
    graphStats(parsefile.getRepInfo, "User Reputation", ax)
    print("Done **")

    ax = plt.subplot(2, 4, 3)
    graphStats(parsefile.getAnswersInfo, "# Answers", ax)
    print("Done ***")

    ax = plt.subplot(2, 4, 4)
    graphStats(parsefile.getCommentsInfo, "# Comments", ax)
    print("Done ****")

    ax = plt.subplot(2, 4, 5)
    graphStats(parsefile.getCommentsInfo, "Score", ax)
    print("Done *****")

    ax = plt.subplot(2, 4, 6)
    graphStats(parsefile.UpVotesInfo, "UpVotes", ax)
    print("Done ******")

    ax = plt.subplot(2, 4, 7)
    graphStats(parsefile.DownVotesInfo, "DownVotes", ax)
    print("Done *******")

    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.show()

def concatallwords(words):
    sent = []
    for k,v in words:
        sent.extend([k] * v)
    random.shuffle(sent)
    return " ".join(sent)

def plotfig2():
    plt.figure(2, figsize=(20, 10))

    ax = plt.subplot(3, 3, 1)
    words = parsefile.CountKeyWords(open("data/MXnetQueryResults.csv"))
    graphWords(concatallwords(words), ax, "MXnet")
    print("Done *")

    ax = plt.subplot(3, 3, 2)
    words = parsefile.CountKeyWords(open("data/DL4jQueryResults.csv"))
    graphWords(concatallwords(words), ax, "DL4j")
    print("Done **")

    ax = plt.subplot(3, 3, 3)
    words = parsefile.CountKeyWords(open("data/DLibQueryResults.csv"))
    graphWords(concatallwords(words), ax, "DLib")
    print("Done ***")

    ax = plt.subplot(3, 3, 4)
    words = parsefile.CountKeyWords(open("data/PytorchQueryResults.csv"))
    graphWords(concatallwords(words), ax, "PyTorch")
    print("Done ****")

    ax = plt.subplot(3, 3, 5)
    words = parsefile.CountKeyWords(open("data/KerasQueryResults.csv"))
    graphWords(concatallwords(words), ax, "Keras")
    print("Done *****")

    ax = plt.subplot(3, 3, 6)
    words = parsefile.CountKeyWords(open("data/CaffeQueryResults.csv"))
    graphWords(concatallwords(words), ax, "Caffe")
    print("Done ******")

    ax = plt.subplot(3, 3, 7)
    words = parsefile.CountKeyWords(open("data/TensorflowQueryResults.csv"))
    graphWords(concatallwords(words), ax, "TensorFlow")
    print("Done *******")

    ax = plt.subplot(3, 3, 8)
    words = parsefile.CountKeyWords(open("data/TheanoQueryResults.csv"))
    graphWords(concatallwords(words), ax, "Theano")
    print("Done ********")

    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.show()

def main():
    # getAvgTimes()
    # getAvgReps()
    # getAvgAnswers()
    # getAvgComments()
    # getAvgScore()
    # getAvgUpVotes()
    # getKeyWords()

    plotfig1()
    # plotfig2()

    # getKeyWords()





if __name__=="__main__":
    main()

