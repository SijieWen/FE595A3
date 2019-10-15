import pandas as pd
import re
from textblob import TextBlob
from pprint import pprint

## For all male characters
f = open("All_Male.txt",'r')
male_l = []
for l in f.readlines():
    l = re.findall(r"(He.*)", l)    # remove serial number in someone's file
    l = "".join(l)     # conver list into string
    blob = TextBlob(l)    
    male_l.append([blob.sentiment.polarity, l])   # use textblob's polarity score as my sentiment analysis
f.close()

df_male = pd.DataFrame(male_l, columns = ['Score', 'Sentence'])    # conver the list into a dataframe
df_male = df_male.sort_values(by="Score" , ascending=False)   # sort all of the characters based on sentiment score

top_male = df_male.head(10)   # top 10 male
top_male

bottom_male = df_male.tail(10)   # bottom 10 male
bottom_male


## For all female characters
f = open("All_Female.txt",'r')
female_l = []
for l in f.readlines():
    l = re.findall(r"(She.*)", l)    # remove serial number in someone's file
    l = "".join(l)     # conver list into string
    blob = TextBlob(l)    
    female_l.append([blob.sentiment.polarity, l])   # use textblob's polarity score as my sentiment analysis
f.close()

df_female = pd.DataFrame(female_l, columns = ['Score', 'Sentence'])    # conver the list into a dataframe
df_female = df_female.sort_values(by="Score" , ascending=False)   # sort all of the characters based on sentiment score

top_female = df_female.head(10)   # top 10 female
top_female

bottom_female = df_female.tail(10)   # bottom 10 female
bottom_female


## Output
def sort_list(df):
    sort_list = []
    for i in range(len(df)):
        sort_list.append(df.iloc[i,1])
    return sort_list

pprint(sort_list(top_male))
pprint(sort_list(bottom_male))
pprint(sort_list(top_female))
pprint(sort_list(bottom_female))



## Submit the output as text files
male_top10_file = open("male_top10.txt", 'a+')
for line in sort_list(top_male):
    male_top10_file.write(line + "\n")
male_top10_file.close()

female_top10_file = open("female_top10.txt", 'a+')
for line in sort_list(top_female):
    female_top10_file.write(line + "\n")
female_top10_file.close()

male_bottom10_file = open("male_bottom10.txt", 'a+')
for line in sort_list(bottom_male):
    male_bottom10_file.write(line + "\n")
male_bottom10_file.close()

female_bottom10_file = open("female_bottom10.txt", 'a+')
for line in sort_list(bottom_female):
    female_bottom10_file.write(line + "\n")
female_bottom10_file.close()



## Groups them together into the original format of the joke
def group(df1, df2):
    group_list = []
    for i in range(len(df1)):
        group_list.append(TextBlob(df1.iloc[i,1] + " " + df2.iloc[i,1] + " " + "They fight crime!"))
    return group_list

pprint(group(top_male, top_female))
pprint(group(bottom_male, bottom_female))
