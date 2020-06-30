import abc

class AbstractModel(metaclass=abc.ABCMeta):


    def getType(self):
        print('\nI AM A MODEL')

    @abc.abstractmethod
    def fit(self):
        pass


class KNN(AbstractModel):

    def fit(self):
        #doSomething()
        pass


class ANN(AbstractModel):

    def fit(self):
        #doSomethingElse()
        pass


#AutoML

#AbstractModel.load
#AbstractModel.preprocess
#AbstractModel.process

