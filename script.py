import pandas as pd
import zipfile
from datetime import datetime, timedelta, date

zf = zipfile.ZipFile('/dcs/14/u1404526/yr4/cs910/test/spotify/spotifys-worldwide-daily-song-ranking.zip')
df = pd.read_csv(zf.open('data.csv'))

#print df
'''
col names:
Position,Track Name,Artist,Streams,URL,Date,Region
'''

'''
Beginning of code to reduce dataset
'''

del df["URL"]

value_list = ["2017-08-01", "2017-08-02", "2017-08-03", "2017-08-04", "2017-08-05", "2017-08-06", "2017-08-07", "2017-08-08", "2017-08-09", "2017-08-10",
    "2017-08-11", "2017-08-12", "2017-08-13", "2017-08-14", "2017-08-15", "2017-08-16", "2017-08-17"]


'''
Keep any date that is not in August.
'''
# not is ~ symbol
df = df[~df.Date.isin(value_list)]#not in auguest as it isnt a full month in the dataset

#unique region values including global - 54
#print df.Region.unique(), len(df.Region.unique())

'''
Filter out positions that are not 1 to 50.
'''
df = df[df["Position"] <= 50]

'''
Only keep instances where Region == global
'''
df = df[df.Region.isin(["global"])]

'''
End of code to reduce dataset
'''

'''
Beginning of code to add relevant columns
'''

df['1dayago'],df['pos-1'],df['-1top10'] = "NA", "NA", "no"
df['2dayago'],df['pos-2'],df['-2top10'] = "NA", "NA", "no"
df['3dayago'],df['pos-3'],df['-3top10'] = "NA", "NA", "no"
df['4dayago'],df['pos-4'],df['-4top10'] = "NA", "NA", "no"
df['5dayago'],df['pos-5'],df['-5top10'] = "NA", "NA", "no"
df['6dayago'],df['pos-6'],df['-6top10'] = "NA", "NA", "no"
df['7dayago'],df['pos-7'],df['-7top10'] = "NA", "NA", "no"

df['currtop10'] = "no"
#df['all7']= "no"
#df['class2'] = "no"

day_diff = [1,2,3,4,5,6,7]


for index, row in df.iterrows():
    track_name = row['Track Name']
    if row['Date'] == "2017-01-01" or row['Date'] == "2017-01-02" or row['Date'] == "2017-01-03" or row['Date'] == "2017-01-04" or row['Date'] == "2017-01-05" or row['Date'] == "2017-01-06" or row['Date'] == "2017-01-07":
        #print "plshelp ", index, df.index.get_values(), df.loc[index,'test']#df.loc[0:15,'A'] = 16


        if row['Date'] == "2017-01-01":
            full_dates = ["2016-12-31", "2016-12-30", "2016-12-29", "2016-12-28", "2016-12-27", "2016-12-26", "2016-12-25"]

        else:
            if row['Date'] == "2017-01-02":
                full_dates = ["2017-01-01", "2016-12-31", "2016-12-30", "2016-12-29", "2016-12-28", "2016-12-27", "2016-12-26"]
            else:
                if row['Date'] == "2017-01-03":
                    full_dates = ["2017-01-02", "2017-01-01", "2016-12-31", "2016-12-30", "2016-12-29", "2016-12-28", "2016-12-27"]
                else:
                    if row['Date'] == "2017-01-04":
                        full_dates = ["2017-01-03", "2017-01-02", "2017-01-01", "2016-12-31", "2016-12-30", "2016-12-29", "2016-12-28"]
                    else:
                        if row['Date'] == "2017-01-05":
                            full_dates = ["2017-01-04", "2017-01-03", "2017-01-02", "2017-01-01", "2016-12-31", "2016-12-30", "2016-12-29"]
                        else:
                            if row['Date'] == "2017-01-06":
                                full_dates = ["2017-01-05", "2017-01-04", "2017-01-03", "2017-01-02", "2017-01-01", "2016-12-31", "2016-12-30"]
                            else:
                                if row['Date'] == "2017-01-07":
                                    full_dates = ["2017-01-06", "2017-01-05", "2017-01-04", "2017-01-03", "2017-01-02", "2017-01-01", "2016-12-31"]

                                #7
                                #print full_dates[6]
                                temp7 = df[(df["Date"] == full_dates[6]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
                                for index2, row2 in temp7.iterrows():
                                    df.loc[index,'7dayago'] = row2["Streams"]
                                    df.loc[index,'pos-7'] = row2["Position"]
                                    df.loc[index,'-7top10'] = "yes" if row2["Position"] <= 10 else "no"

                            #6
                            temp6 = df[(df["Date"] == full_dates[5]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
                            for index2, row2 in temp6.iterrows():
                                df.loc[index,'6dayago'] = row2["Streams"]
                                df.loc[index,'pos-6'] = row2["Position"]
                                df.loc[index,'-6top10'] = "yes" if row2["Position"] <= 10 else "no"

                        #5
                        temp5 = df[(df["Date"] == full_dates[4]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
                        for index2, row2 in temp5.iterrows():
                            df.loc[index,'5dayago'] = row2["Streams"]
                            df.loc[index,'pos-5'] = row2["Position"]
                            df.loc[index,'-5top10'] = "yes" if row2["Position"] <= 10 else "no"

                    #4
                    temp4 = df[(df["Date"] == full_dates[3]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
                    for index2, row2 in temp4.iterrows():
                        df.loc[index,'4dayago'] = row2["Streams"]
                        df.loc[index,'pos-4'] = row2["Position"]
                        df.loc[index,'-4top10'] = "yes" if row2["Position"] <= 10 else "no"

                #3
                temp3 = df[(df["Date"] == full_dates[2]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
                for index2, row2 in temp3.iterrows():
                    df.loc[index,'3dayago'] = row2["Streams"]
                    df.loc[index,'pos-3'] = row2["Position"]
                    df.loc[index,'-3top10'] = "yes" if row2["Position"] <= 10 else "no"

            #2
            temp2 = df[(df["Date"] == full_dates[1]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
            for index2, row2 in temp2.iterrows():
                df.loc[index,'2dayago'] = row2["Streams"]
                df.loc[index,'pos-2'] = row2["Position"]
                df.loc[index,'-2top10'] = "yes" if row2["Position"] <= 10 else "no"

        #1
        temp1 = df[(df["Date"] == full_dates[0]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp1.iterrows():
            df.loc[index,'1dayago'] = row2["Streams"]
            df.loc[index,'pos-1'] = row2["Position"]
            df.loc[index,'-1top10'] = "yes" if row2["Position"] <= 10 else "no"
        #print temp1, full_dates[0], track_name
        #print df[index]

    else:
        #replace value with new minus old in df
        date = row['Date'].split("-")
        #print date
        '''
        if after split day is 01-07, remember to go backward based on month
        '''
        daynum = int(date[2])
        #print daynum

        if daynum <= 7:
            #manually get month and then get value
            #does prev month have 31, 30 or 28 days
            '''
            month 2
            1 - 31, 30, 29, 28, 27, 26, 25
            2 - 31, 30, 29, 28, 27, 26
            3 - 31, 30, 29, 28, 27
            4 - 31, 30, 29, 28
            5 - 31, 30, 29
            6 - 31, 30
            7 - 31

            month 3
            1 - 28, 27, 26, 25, 24, 23, 22
            2 - 28, 27, 26, 25, 24, 23
            3 - 28, 27, 26, 25, 24
            4 - 28, 27, 26, 25
            5 - 28, 27, 26
            6 - 28, 27
            7 - 28

            month 4
            1 - 31, 30, 29, 28, 27, 26, 25
            2 - 31, 30, 29, 28, 27, 26
            3 - 31, 30, 29, 28, 27
            4 - 31, 30, 29, 28
            5 - 31, 30, 29
            6 - 31, 30
            7 - 31

            month 5
            1 - 30, 29, 28, 27, 26, 25, 24
            2 - 30, 29, 28, 27, 26, 25
            3 - 30, 29, 28, 27, 26
            4 - 30, 29, 28, 27
            5 - 30, 29, 28
            6 - 30, 29
            7 - 30

            month 6
            1 - 31, 30, 29, 28, 27, 26, 25
            2 - 31, 30, 29, 28, 27, 26
            3 - 31, 30, 29, 28, 27
            4 - 31, 30, 29, 28
            5 - 31, 30, 29
            6 - 31, 30
            7 - 31

            month 7
            1 - 30, 29, 28, 27, 26, 25, 24
            2 - 30, 29, 28, 27, 26, 25
            3 - 30, 29, 28, 27, 26
            4 - 30, 29, 28, 27
            5 - 30, 29, 28
            6 - 30, 29
            7 - 30


            need to include curr month e.g. when 7, dont forget 6 5 4 3 2....
            '''

            month_copy = date[1]
            date[1] = int(date[1])

            days = []
            months = []
            if int(date[1]) == 6 or int(date[1]) == 4 or int(date[1]) == 2:
                if daynum == 1:
                    days = [31, 30, 29, 28, 27, 26, 25]
                    months = [date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 2:
                    days = [1, 31, 30, 29, 28, 27, 26]
                    months = [date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 3:
                    days = [2, 1, 31, 30, 29, 28, 27]
                    months = [date[1], date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 4:
                    days = [3, 2, 1, 31, 30, 29, 28]
                    months = [date[1], date[1], date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 5:
                    days = [4, 3, 2, 1, 31, 30, 29]
                    months = [date[1], date[1], date[1], date[1], date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 6:
                    days = [5, 4, 3, 2, 1, 31, 30]
                    months = [date[1], date[1], date[1], date[1], date[1], date[1]-1, date[1]-1]
                elif daynum == 7:
                    days = [6, 5, 4, 3, 2, 1, 31]
                    months = [date[1], date[1], date[1], date[1], date[1], date[1], date[1]-1]
            elif int(date[1] == 7) or int(date[1]) == 5:
                if daynum == 1:
                    days = [30, 29, 28, 27, 26, 25, 24]
                    months = [date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 2:
                    days = [1, 30, 29, 28, 27, 26, 25]
                    months = [date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 3:
                    days = [2, 1, 30, 29, 28, 27, 26]
                    months = [date[1], date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 4:
                    days = [3, 2, 1, 30, 29, 28, 27]
                    months = [date[1], date[1], date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 5:
                    days = [4, 3, 2, 1, 30, 29, 28]
                    months = [date[1], date[1], date[1], date[1], date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 6:
                    days = [5, 4, 3, 2, 1, 30, 29]
                    months = [date[1], date[1], date[1], date[1], date[1], date[1]-1, date[1]-1]
                elif daynum == 7:
                    days = [6, 5, 4, 3, 2, 1, 30]
                    months = [date[1], date[1], date[1], date[1], date[1], date[1], date[1]-1]
            elif int(date[1]) == 3:
                if daynum == 1:
                    days = [28, 27, 26, 25, 24, 23, 22]
                    months = [date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 2:
                    days = [1, 28, 27, 26, 25, 24, 23]
                    months = [date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 3:
                    days = [2, 1, 28, 27, 26, 25, 24]
                    months = [date[1], date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 4:
                    days = [3, 2, 1, 28, 27, 26, 25]
                    months = [date[1], date[1], date[1], date[1]-1, date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 5:
                    days = [4, 3, 2, 1, 28, 27, 26]
                    months = [date[1], date[1], date[1], date[1], date[1]-1, date[1]-1, date[1]-1]
                elif daynum == 6:
                    days = [5, 4, 3, 2, 1, 28, 27]
                    months = [date[1], date[1], date[1], date[1], date[1], date[1]-1, date[1]-1]
                elif daynum == 7:
                    days = [6, 5, 4, 3, 2, 1, 28]
                    months = [date[1], date[1], date[1], date[1], date[1], date[1], date[1]-1]


            # can be put as 0 as no month is > 9 in this data set
            other_part_date = ["2017" + "-0" + str(months[0]) + "-", "2017" + "-0" + str(months[1]) + "-", "2017" + "-0" + str(months[2]) + "-",
            "2017" + "-0" + str(months[3]) + "-", "2017" + "-0" + str(months[4]) + "-", "2017" + "-0" + str(months[5]) + "-",
            "2017" + "-0" + str(months[6]) + "-"]

            if days[0] < 10:
                days[0] = "0"+str(days[0])
            if days[1] < 10:
                days[1] = "0"+str(days[1])
            if days[2] < 10:
                days[2] = "0"+str(days[2])
            if days[3] < 10:
                days[3] = "0"+str(days[3])
            if days[4] < 10:
                days[4] = "0"+str(days[4])
            if days[5] < 10:
                days[5] = "0"+str(days[5])
            if days[6] < 10:
                days[6] = "0"+str(days[6])
            #print days
            full_dates = [other_part_date[0] + str(days[0]), other_part_date[1] + str(days[1]), other_part_date[2] + str(days[2]), other_part_date[3] + str(days[3]),
            other_part_date[4] + str(days[4]), other_part_date[5] + str(days[5]), other_part_date[6] + str(days[6])]


        else:
            #do for 1 to 7
            dates_pre = [daynum - day_diff[0], daynum - day_diff[1], daynum - day_diff[2], daynum - day_diff[3], daynum - day_diff[4], daynum - day_diff[5], daynum - day_diff[6]]
            other_part_date = date[0] + "-" + date[1] + "-"


            if dates_pre[0] < 10:
                dates_pre[0] = "0"+str(dates_pre[0])
            if dates_pre[1] < 10:
                dates_pre[1] = "0"+str(dates_pre[1])
            if dates_pre[2] < 10:
                dates_pre[2] = "0"+str(dates_pre[2])
            if dates_pre[3] < 10:
                dates_pre[3] = "0"+str(dates_pre[3])
            if dates_pre[4] < 10:
                dates_pre[4] = "0"+str(dates_pre[4])
            if dates_pre[5] < 10:
                dates_pre[5] = "0"+str(dates_pre[5])
            if dates_pre[6] < 10:
                dates_pre[6] = "0"+str(dates_pre[6])

            #string conversion remains here for vals >= 10
            full_dates = [other_part_date + str(dates_pre[0]), other_part_date + str(dates_pre[1]), other_part_date + str(dates_pre[2]), other_part_date + str(dates_pre[3]), other_part_date + str(dates_pre[4]), other_part_date + str(dates_pre[5]), other_part_date + str(dates_pre[6])]

        #1
        temp1 = df[(df["Date"] == full_dates[0]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp1.iterrows():
            df.loc[index,'1dayago'] = row2["Streams"]
            df.loc[index,'pos-1'] = row2["Position"]
            #isApple = True if fruit == 'Apple' else False
            df.loc[index,'-1top10'] = "yes" if row2["Position"] <= 10 else "no"
        #print temp1, full_dates[0], track_name

        #2
        temp2 = df[(df["Date"] == full_dates[1]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp2.iterrows():
            df.loc[index,'2dayago'] = row2["Streams"]
            df.loc[index,'pos-2'] = row2["Position"]
            df.loc[index,'-2top10'] = "yes" if row2["Position"] <= 10 else "no"

        #3
        temp3 = df[(df["Date"] == full_dates[2]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp3.iterrows():
            df.loc[index,'3dayago'] = row2["Streams"]
            df.loc[index,'pos-3'] = row2["Position"]
            df.loc[index,'-3top10'] = "yes" if row2["Position"] <= 10 else "no"

        #4
        temp4 = df[(df["Date"] == full_dates[3]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp4.iterrows():
            df.loc[index,'4dayago'] = row2["Streams"]
            df.loc[index,'pos-4'] = row2["Position"]
            df.loc[index,'-4top10'] = "yes" if row2["Position"] <= 10 else "no"

        #5
        temp5 = df[(df["Date"] == full_dates[4]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp5.iterrows():
            df.loc[index,'5dayago'] = row2["Streams"]
            df.loc[index,'pos-5'] = row2["Position"]
            df.loc[index,'-5top10'] = "yes" if row2["Position"] <= 10 else "no"

        #6
        temp6 = df[(df["Date"] == full_dates[5]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp6.iterrows():
            df.loc[index,'6dayago'] = row2["Streams"]
            df.loc[index,'pos-6'] = row2["Position"]
            df.loc[index,'-6top10'] = "yes" if row2["Position"] <= 10 else "no"

        #7
        #print full_dates[6]
        temp7 = df[(df["Date"] == full_dates[6]) & (df["Track Name"] == track_name) & (df["Artist"] == row["Artist"])]
        for index2, row2 in temp7.iterrows():
            df.loc[index,'7dayago'] = row2["Streams"]
            df.loc[index,'pos-7'] = row2["Position"]
            df.loc[index,'-7top10'] = "yes" if row2["Position"] <= 10 else "no"

            #row['Track Name'] to check with whole df
            #streams to check with whole df
            #get df vals with new date and exact song if possible

            #print full_dates

        #df.loc[index,'test']

    #print row['c1'], row['c2']
    if row['Position'] <= 10:
        df.loc[index,'currtop10'] = "yes"

'''
End of code to remove relevant columns
'''

print df
#print df[df['class'] == "yes"].count()

#remove these are that means the song hasnt been top 50 for atleast 7 days in most cases


'''
10400 before this

Remove missing values
'''
df = df[df['pos-7'] != "NA"]
df = df[df['pos-6'] != "NA"]
df = df[df['pos-5'] != "NA"]
df = df[df['pos-4'] != "NA"]
df = df[df['pos-3'] != "NA"]
df = df[df['pos-2'] != "NA"]
df = df[df['pos-1'] != "NA"]
#print df[df['Position'] == 1].groupby('Track Name')['Position'].count()

#print df[(df["Position"] == 1) & (df["Date"] == "2017-01-01")]


print df
'''
DONT FORGET ME
'''
df.to_csv("cut1.csv", index=False)


#print df.Date.unique(), len(df.Date.unique())
#print df.Streams.unique(), len(df.Streams.unique()), sorted(df.Streams.unique())
#print df.Artist.unique(), len(df.Artist.unique())
#print df['Track Name'].unique(), len(df['Track Name'].unique())


'''

maybe add canada

how long do songs persist in the top 10? in the uk most streamed.

correlation between uk us and global charts

how often does the us and the most streamed songs dictate its place/ make it reach global charts

based on how many top tracks the us and uk share, can we recommend chart music form one another before it charts for the us?

when a song gets number 1, how long does it take for other countries to have it as number 1

when a song is top in the global charts, how many countires usually have the song as number 1? are there any consistent countries?

top5 as ed sheeran does a madness?

how long would a track be expected to remain number 1? global or uk -poisson regression - new col how long does it stay number 1 for.

for global
when something hits top 10, will it remain top 10 for a week? - classfication, have to make a new col does it stay in top 10 for 7 days,
need data from 11-50 because need to see pattern of days
cols to add:
day -1, ...-7
%increase for -1 to -7 = 6 by 7, 5 by 6
how many days consequtively in top 10,
is it bigger than 7(week)
class does it stay in top 10 for 7 days

other factros that can affect this are if in a week there are less streams for some reason, maybe song isnt available

maybe track position in chart as well



Links used to help

https://www.kaggle.com/edumucelli/spotifys-worldwide-daily-song-ranking

https://stackoverflow.com/questions/26942476/reading-csv-zipped-files-in-python

https://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe-using-python-del

https://chrisalbon.com/python/pandas_select_rows_when_column_has_certain_values.html

https://stackoverflow.com/questions/16923281/pandas-writing-dataframe-to-csv-file

https://stackoverflow.com/questions/29219011/selecting-rows-based-on-multiple-column-values-in-pandas-dataframe

https://stackoverflow.com/questions/40710811/count-items-greater-than-a-value-in-pandas-groupby

'''
