import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class CallAnalyis_911:

    def __init__(self,df):
        self.df=df

    def infoCheck(self):
        print(self.df.info())
        print('Hello world')

    def exploratoryAnalysis(self):
      try:
        #Top 5 zipcodes
        print('Top 5 Zipcodes are : ')
        print(self.df['zip'].value_counts().head(5))
        # Top 5 Townships
        print("Top 5 Townships are :{}".format(self.df['twp'].value_counts().head(5)))
        print("Number of unique Titles are :{}".format(self.df['title'].nunique()))

      except:
        print("exploratoryAnalysis function error")


if __name__ == '__main__':
    __911__= CallAnalyis_911(df = pd.read_csv('911.csv'))
    # __911__.infoCheck()
    __911__.exploratoryAnalysis()

