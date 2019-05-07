import parsefile

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

def main():
    print("AVERAGE TIME (closed - open):")
    getAvgTimes()

    print("\nAVERAGE USER REPUTATION:")
    getAvgReps()

if __name__=="__main__":
    main()