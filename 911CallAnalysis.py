import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class CallAnalyis_911:

    def __init__(self,df):
        self.df =df

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

    def featureCreation(self):
        try:
            self.df['Reason'] = self.df['title'].apply(lambda title: title.split(':')[0])
            print('The most common reasons for 911 calls is: \n{}'.format(self.df['Reason'].value_counts()))
            sns.countplot(x='Reason', data=self.df, palette='magma')
            plt.title("The most common reasons for 911 calls")
            plt.show()
            return self.df['Reason']
        except:
            print("featureCreation function error")

    def timeAnalysis(self):
        try:
            print(type(self.df['timeStamp'].iloc[0]))
            #Since the timestamps are in string using pd.to_datetime to convert the string values into DateTime Objects
            self.df['timeStamp'] = pd.to_datetime(self.df['timeStamp'])
            #Hourly Analysis
            self.df['Hour'] = self.df['timeStamp'].apply(lambda time: time.hour)
            sns.countplot(x='Hour', data=self.df, hue=self.df['Reason'], palette='magma')
            plt.title('Distribution of calls over Hours')
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            plt.show()
            #Monthly Analysis
            self.df['Month'] = self.df['timeStamp'].apply(lambda time: time.month)
            dmap = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
            self.df['Month'] = self.df['Month'].map(dmap)
            sns.countplot(x='Month', data=self.df, hue=self.df['Reason'], palette='magma')
            plt.title('Distribution of calls over Month')
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            plt.show()
            #Weekly Analysis
            self.df['Day of Week'] = self.df['timeStamp'].apply(lambda time: time.dayofweek)
            dmap1 = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
            self.df['Day of Week'] = self.df['Day of Week'].map(dmap1)
            sns.countplot(x='Day of Week', data=self.df, hue=self.df['Reason'], palette='magma')
            plt.title('Distribution of calls over over days of week by reason')
            plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            plt.show()
        except:
            print("timeRelated function error")


if __name__ == '__main__':
    __911__= CallAnalyis_911(df = pd.read_csv('911.csv'))
    # __911__.infoCheck()
    # __911__.exploratoryAnalysis()
    __911__.featureCreation()
    __911__.timeAnalysis()

