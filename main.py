import parsefile
import random
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def getAvgTimes():
    print("time open (pytorch):\t", parsefile.getTimeInfo(open("data/PytorchQueryResults.csv")))
    print("time open (mxnet):\t\t", parsefile.getTimeInfo(open("data/MXnetQueryResults.csv")))
    print("time open (keras):\t\t", parsefile.getTimeInfo(open("data/KerasQueryResults.csv")))
    print("time open (tensorflow):\t", parsefile.getTimeInfo(open("data/TensorflowQueryResults.csv")))
    print("time open (caffe):\t\t", parsefile.getTimeInfo(open("data/CaffeQueryResults.csv")))
    print("time open (Dl4j):\t\t", parsefile.getTimeInfo(open("data/DL4jQueryResults.csv")))
    print("time open (dlib):\t\t", parsefile.getTimeInfo(open("data/DLibQueryResults.csv")))
    print("time open (theano):\t\t", parsefile.getTimeInfo(open("data/TheanoQueryResults.csv")))

def getAvgReps():
    print("user rep (tensorflow):\t", parsefile.getRepInfo(open("data/TensorflowQueryResults.csv")))
    print("user rep (keras):\t\t", parsefile.getRepInfo(open("data/KerasQueryResults.csv")))
    print("user rep (pytorch):\t\t", parsefile.getRepInfo(open("data/PytorchQueryResults.csv")))
    print("user rep (mxnet):\t\t", parsefile.getRepInfo(open("data/MXnetQueryResults.csv")))
    print("user rep (caffe):\t\t", parsefile.getRepInfo(open("data/CaffeQueryResults.csv")))
    print("user rep (theano):\t\t", parsefile.getRepInfo(open("data/TheanoQueryResults.csv")))
    print("user rep (Dl4j):\t\t", parsefile.getRepInfo(open("data/DL4jQueryResults.csv")))
    print("user rep (dlib):\t\t", parsefile.getRepInfo(open("data/DLibQueryResults.csv")))

def getAvgAnswers():
    print("num ans (keras):\t\t", parsefile.getAnswersInfo(open("data/KerasQueryResults.csv")))
    print("num ans (tensorflow):\t", parsefile.getAnswersInfo(open("data/TensorflowQueryResults.csv")))
    print("num ans (caffe):\t\t", parsefile.getAnswersInfo(open("data/CaffeQueryResults.csv")))
    print("num ans (pytorch):\t\t", parsefile.getAnswersInfo(open("data/PytorchQueryResults.csv")))
    print("num ans (theano):\t\t", parsefile.getAnswersInfo(open("data/TheanoQueryResults.csv")))
    print("num ans (Dl4j):\t\t\t", parsefile.getAnswersInfo(open("data/DL4jQueryResults.csv")))
    print("num ans (mxnet):\t\t", parsefile.getAnswersInfo(open("data/MXnetQueryResults.csv")))
    print("num ans (dlib):\t\t\t", parsefile.getAnswersInfo(open("data/DLibQueryResults.csv")))

def getAvgComments():
    print("num comments (mxnet):\t\t", parsefile.getCommentsInfo(open("data/MXnetQueryResults.csv")))
    print("num comments (Dl4j):\t\t\t", parsefile.getCommentsInfo(open("data/DL4jQueryResults.csv")))
    print("num comments (pytorch):\t\t", parsefile.getCommentsInfo(open("data/PytorchQueryResults.csv")))
    print("num comments (tensorflow):\t", parsefile.getCommentsInfo(open("data/TensorflowQueryResults.csv")))
    print("num comments (theano):\t\t", parsefile.getCommentsInfo(open("data/TheanoQueryResults.csv")))
    print("num comments (keras):\t\t", parsefile.getCommentsInfo(open("data/KerasQueryResults.csv")))
    print("num comments (caffe):\t\t", parsefile.getCommentsInfo(open("data/CaffeQueryResults.csv")))
    print("num comments (dlib):\t\t\t", parsefile.getCommentsInfo(open("data/DLibQueryResults.csv")))

def getAvgScore():
    print("score (mxnet):\t\t", parsefile.getScoreInfo(open("data/MXnetQueryResults.csv")))
    print("score (Dl4j):\t\t", parsefile.getScoreInfo(open("data/DL4jQueryResults.csv")))
    print("score (dlib):\t\t", parsefile.getScoreInfo(open("data/DLibQueryResults.csv")))
    print("score (pytorch):\t", parsefile.getScoreInfo(open("data/PytorchQueryResults.csv")))
    print("score (keras):\t\t", parsefile.getScoreInfo(open("data/KerasQueryResults.csv")))
    print("score (caffe):\t\t", parsefile.getScoreInfo(open("data/CaffeQueryResults.csv")))
    print("score (tensorflow):\t", parsefile.getScoreInfo(open("data/TensorflowQueryResults.csv")))
    print("score (theano):\t\t", parsefile.getScoreInfo(open("data/TheanoQueryResults.csv")))

def getAvgUpVotes():
    print("avg/max/min UpVotes (mxnet):\t\t", parsefile.UpVotesInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min UpVotes (Dl4j):\t\t", parsefile.UpVotesInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min UpVotes (dlib):\t\t", parsefile.UpVotesInfo(open("data/DLibQueryResults.csv")))
    print("avg/max/min UpVotes (pytorch):\t", parsefile.UpVotesInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min UpVotes (keras):\t\t", parsefile.UpVotesInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min UpVotes (caffe):\t\t", parsefile.UpVotesInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min UpVotes (tensorflow):\t", parsefile.UpVotesInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min UpVotes (theano):\t\t", parsefile.UpVotesInfo(open("data/TheanoQueryResults.csv")))


def getAvgDownVotes():
    print("avg/max/min UpVotes (mxnet):\t\t", parsefile.DownVotesInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min UpVotes (Dl4j):\t\t", parsefile.DownVotesInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min UpVotes (dlib):\t\t", parsefile.DownVotesInfo(open("data/DLibQueryResults.csv")))
    print("avg/max/min UpVotes (pytorch):\t", parsefile.DownVotesInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min UpVotes (keras):\t\t", parsefile.DownVotesInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min UpVotes (caffe):\t\t", parsefile.DownVotesInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min UpVotes (tensorflow):\t", parsefile.DownVotesInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min UpVotes (theano):\t\t", parsefile.DownVotesInfo(open("data/TheanoQueryResults.csv")))

def prettyprintKeywords(keywords):
    return " ".join(["{:25}".format(str(x)) for x in keywords])

def getKeyWords():
    print("Most common words used in (mxnet):\t\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/MXnetQueryResults.csv"))))
    print("Most common words used in (Dl4j):\t\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/DL4jQueryResults.csv"))))
    print("Most common words used in (dlib):\t\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/DLibQueryResults.csv"))))
    print("Most common words used in (pytorch):\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/PytorchQueryResults.csv"))))
    print("Most common words used in (keras):\t\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/KerasQueryResults.csv"))))
    print("Most common words used in (caffe):\t\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/CaffeQueryResults.csv"))))
    print("Most common words used in (tensorflow):\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/TensorflowQueryResults.csv"))))
    print("Most common words used in (theano):\t\t", prettyprintKeywords(parsefile.CountKeyWords(open("data/TheanoQueryResults.csv"))))

def convertData(data):
    try:
        newdata = [x.days for x in data]
        return newdata
    except:
        return data

def graphStats(getfunction, title, ax):
    datatoplot = []

    times = getfunction(open("data/PytorchQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/TensorflowQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/MXnetQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/KerasQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/CaffeQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/DL4jQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/DLibQueryResults.csv"))
    datatoplot.append(convertData(times))

    times = getfunction(open("data/TheanoQueryResults.csv"))
    datatoplot.append(convertData(times))

    ax.boxplot(datatoplot)
    ax.set_xticklabels(["PyTorch", "Tensorflow", "MXnet", "Keras", "Caffe", "DL4j", "DLib", "Theano"], rotation=45)
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

    ax = plt.subplot(2, 4, 2)
    graphStats(parsefile.getRepInfo, "User Reputation", ax)

    ax = plt.subplot(2, 4, 3)
    graphStats(parsefile.getAnswersInfo, "# Answers", ax)

    ax = plt.subplot(2, 4, 4)
    graphStats(parsefile.getCommentsInfo, "# Comments", ax)

    ax = plt.subplot(2, 4, 5)
    graphStats(parsefile.getCommentsInfo, "Score", ax)

    ax = plt.subplot(2, 4, 6)
    graphStats(parsefile.UpVotesInfo, "UpVotes", ax)

    ax = plt.subplot(2, 4, 7)
    graphStats(parsefile.DownVotesInfo, "DownVotes", ax)

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
    # plotfig1()
    plotfig2()

    # getKeyWords()





if __name__=="__main__":
    main()

