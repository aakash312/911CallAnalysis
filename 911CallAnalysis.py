import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class CallAnalyis_911:

    def __init__(self,df):
        '''
        Init function
        '''
        self.df =df


    def exploratoryAnalysis(self):
        '''
        This function is used for exploratory data analysis
        '''
        try:
            print(self.df.info())
            #Top 5 zipcodes
            print('Top 5 Zipcodes are : \n{}'.format(self.df['zip'].value_counts().head(5)))
            # Top 5 Townships
            print("Top 5 Townships are :\n{}".format(self.df['twp'].value_counts().head(5)))
            # No. of Unique Titles
            print("Number of unique Titles are :{}".format(self.df['title'].nunique()))

        except:
            print("exploratoryAnalysis function error")

    def featureCreation(self):
        '''
        This function is used to identify the top reasons why 911 calls are made
        '''
        try:
            self.df['Reason'] = self.df['title'].apply(lambda title: title.split(':')[0])
            print('The most common reasons for 911 calls is: \n{}'.format(self.df['Reason'].value_counts()))
            sns.countplot(x='Reason', data=self.df, palette='magma')
            plt.title("The most common reasons for 911 calls")
            plt.savefig('/Users/aakash/PycharmProjects/911CallAnalysis/reasonsForCalls.pdf')
            return self.df['Reason']

        except:
            print("featureCreation function error")

    def timeAnalysis(self):
        '''
        This function generates pdf with Time based Analysis
        '''
        try:
            #Since the timestamps are in string using pd.to_datetime to convert the string values into DateTime Objects
            print(type(self.df['timeStamp'].iloc[0]))
            self.df['timeStamp'] = pd.to_datetime(self.df['timeStamp'])
            # Set up the matplotlib figure
            f, axes = plt.subplots(3, 3, figsize=(25, 25))
            sns.despine(left=True)

            #Hourly Analysis
            self.df['Hour'] = self.df['timeStamp'].apply(lambda time: time.hour)
            sns.countplot(x='Hour', data=self.df, hue=self.df['Reason'], palette='magma',ax=axes[0, 0])

            #Monthly Analysis
            self.df['Month'] = self.df['timeStamp'].apply(lambda time: time.month)
            dmap = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
            self.df['Month'] = self.df['Month'].map(dmap)
            sns.countplot(x='Month', data=self.df, hue=self.df['Reason'], palette='magma',ax=axes[0, 1])

            #Weekly Analysis
            self.df['Day of Week'] = self.df['timeStamp'].apply(lambda time: time.dayofweek)
            dmap1 = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
            self.df['Day of Week'] = self.df['Day of Week'].map(dmap1)
            sns.countplot(x='Day of Week', data=self.df, hue=self.df['Reason'], palette='magma',ax=axes[0, 2])


            self.df['Date'] = self.df['timeStamp'].apply(lambda t: t.date())
            self.df.groupby('Date').count()['twp'].plot(ax=axes[1, 0])

            self.df[self.df['Reason'] == 'Traffic'].groupby('Date').count()['twp'].plot(ax=axes[1,1],color='#E89275')
            plt.title('Traffic')

            self.df[self.df['Reason'] == 'Fire'].groupby('Date').count()['twp'].plot(ax=axes[1,2], color='#A74779')
            plt.title('Fire')

            self.df[self.df['Reason'] == 'EMS'].groupby('Date').count()['twp'].plot(ax=axes[2,0],color='#4E1F6F')
            plt.title('EMS')
            plt.tight_layout()
            plt.show()
            # Generating pdf
            # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

            # plt.savefig('/Users/aakash/PycharmProjects/911CallAnalysis/TimeBasedAnalysis.pdf')
        except:
            print("timeRelated function error")



if __name__ == '__main__':
    __911__= CallAnalyis_911(df = pd.read_csv('911.csv'))
    # __911__.exploratoryAnalysis()
    __911__.featureCreation()
    __911__.timeAnalysis()

