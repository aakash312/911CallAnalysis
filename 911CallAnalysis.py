import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class CallAnalyis_911:

    def __init__(self,df):
        self.df=df

    def infoCheck(self):
        print(self.df.info())

    def exploratoryAnalysis(self):
      try:
        #Top 5 zipcodes
        print('Top 5 Zipcodes are : \n{}'.format(self.df['zip'].value_counts().head(5)))
        # Top 5 Townships
        print("Top 5 Townships are :\n{}".format(self.df['twp'].value_counts().head(5)))
        # No. of Unique Titles
        print("Number of unique Titles are :{}".format(self.df['title'].nunique()))

      except:
        print("exploratoryAnalysis function error")

    def featurCreation(self):
        try:
            self.df['Reason'] = self.df['title'].apply(lambda title: title.split(':')[0])
            print('The most common reasons for 911 calls is: \n{}'.format(self.df['Reason'].value_counts()))
        except:
            print("featureCreation function error")



if __name__ == '__main__':
    __911__= CallAnalyis_911(df = pd.read_csv('911.csv'))
    # __911__.infoCheck()
    __911__.exploratoryAnalysis()
    __911__.featurCreation()

