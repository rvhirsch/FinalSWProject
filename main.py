import parsefile
import matplotlib.pyplot as plt

def getAvgTimes():
    print("average time open (pytorch):\t", parsefile.getTimeInfo(open("data/PytorchQueryResults.csv")))
    print("average time open (mxnet):\t\t", parsefile.getTimeInfo(open("data/MXnetQueryResults.csv")))
    print("average time open (keras):\t\t", parsefile.getTimeInfo(open("data/KerasQueryResults.csv")))
    print("average time open (tensorflow):\t", parsefile.getTimeInfo(open("data/TensorflowQueryResults.csv")))
    print("average time open (caffe):\t\t", parsefile.getTimeInfo(open("data/CaffeQueryResults.csv")))
    print("average time open (Dl4j):\t\t", parsefile.getTimeInfo(open("data/DL4jQueryResults.csv")))
    print("average time open (dlib):\t\t", parsefile.getTimeInfo(open("data/DLibQueryResults.csv")))
    print("average time open (theano):\t\t", parsefile.getTimeInfo(open("data/TheanoQueryResults.csv")))

def getAvgReps():
    print("avg/max/min user rep (tensorflow):\t", parsefile.getRepInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min user rep (keras):\t\t", parsefile.getRepInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min user rep (pytorch):\t\t", parsefile.getRepInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min user rep (mxnet):\t\t", parsefile.getRepInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min user rep (caffe):\t\t", parsefile.getRepInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min user rep (theano):\t\t", parsefile.getRepInfo(open("data/TheanoQueryResults.csv")))
    print("avg/max/min user rep (Dl4j):\t\t", parsefile.getRepInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min user rep (dlib):\t\t", parsefile.getRepInfo(open("data/DLibQueryResults.csv")))

def getAvgAnswers():
    print("avg/max/min num ans (keras):\t\t", parsefile.getAnswersInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min num ans (tensorflow):\t", parsefile.getAnswersInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min num ans (caffe):\t\t", parsefile.getAnswersInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min num ans (pytorch):\t\t", parsefile.getAnswersInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min num ans (theano):\t\t", parsefile.getAnswersInfo(open("data/TheanoQueryResults.csv")))
    print("avg/max/min num ans (Dl4j):\t\t\t", parsefile.getAnswersInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min num ans (mxnet):\t\t", parsefile.getAnswersInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min num ans (dlib):\t\t\t", parsefile.getAnswersInfo(open("data/DLibQueryResults.csv")))

def getAvgComments():
    print("avg/max/min num comments (mxnet):\t\t", parsefile.getCommentsInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min num comments (Dl4j):\t\t\t", parsefile.getCommentsInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min num comments (pytorch):\t\t", parsefile.getCommentsInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min num comments (tensorflow):\t", parsefile.getCommentsInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min num comments (theano):\t\t", parsefile.getCommentsInfo(open("data/TheanoQueryResults.csv")))
    print("avg/max/min num comments (keras):\t\t", parsefile.getCommentsInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min num comments (caffe):\t\t", parsefile.getCommentsInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min num comments (dlib):\t\t\t", parsefile.getCommentsInfo(open("data/DLibQueryResults.csv")))

def getAvgScore():
    print("avg/max/min score (mxnet):\t\t", parsefile.getScoreInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min score (Dl4j):\t\t", parsefile.getScoreInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min score (dlib):\t\t", parsefile.getScoreInfo(open("data/DLibQueryResults.csv")))
    print("avg/max/min score (pytorch):\t", parsefile.getScoreInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min score (keras):\t\t", parsefile.getScoreInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min score (caffe):\t\t", parsefile.getScoreInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min score (tensorflow):\t", parsefile.getScoreInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min score (theano):\t\t", parsefile.getScoreInfo(open("data/TheanoQueryResults.csv")))

def getAvgUpVotes():
    print("avg/max/min UpVotes (mxnet):\t\t", parsefile.upVotesInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min UpVotes (Dl4j):\t\t", parsefile.upVotesInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min UpVotes (dlib):\t\t", parsefile.upVotesInfo(open("data/DLibQueryResults.csv")))
    print("avg/max/min UpVotes (pytorch):\t", parsefile.upVotesInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min UpVotes (keras):\t\t", parsefile.upVotesInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min UpVotes (caffe):\t\t", parsefile.upVotesInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min UpVotes (tensorflow):\t", parsefile.upVotesInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min UpVotes (theano):\t\t", parsefile.upVotesInfo(open("data/TheanoQueryResults.csv")))


def getAvgDownVotes():
    print("avg/max/min UpVotes (mxnet):\t\t", parsefile.DownVotesInfo(open("data/MXnetQueryResults.csv")))
    print("avg/max/min UpVotes (Dl4j):\t\t", parsefile.DownVotesInfo(open("data/DL4jQueryResults.csv")))
    print("avg/max/min UpVotes (dlib):\t\t", parsefile.DownVotesInfo(open("data/DLibQueryResults.csv")))
    print("avg/max/min UpVotes (pytorch):\t", parsefile.DownVotesInfo(open("data/PytorchQueryResults.csv")))
    print("avg/max/min UpVotes (keras):\t\t", parsefile.DownVotesInfo(open("data/KerasQueryResults.csv")))
    print("avg/max/min UpVotes (caffe):\t\t", parsefile.DownVotesInfo(open("data/CaffeQueryResults.csv")))
    print("avg/max/min UpVotes (tensorflow):\t", parsefile.DownVotesInfo(open("data/TensorflowQueryResults.csv")))
    print("avg/max/min UpVotes (theano):\t\t", parsefile.DownVotesInfo(open("data/TheanoQueryResults.csv")))


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

def main():
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
    graphStats(parsefile.upVotesInfo, "UpVotes", ax)

    ax = plt.subplot(2, 4, 7)
    graphStats(parsefile.DownVotesInfo, "DownVotes", ax)

    plt.show()

if __name__=="__main__":
    main()