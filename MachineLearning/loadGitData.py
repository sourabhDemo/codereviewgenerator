import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


class LoadDataML:

    def loadgitdata(self):
        # Load dataset
        url = "C:\\Work\\Projects\\SDC4-master\\code\\master\\test.csv"
        names = ['commit-id', 'committer-id', 'checkin-date', 'user-comments']
        dataset = pandas.read_csv(url, names=names)
        return dataset
