import pandas as pd
import re
from textblob import TextBlob
from pprint import pprint
from collections import Counter

import os
os.getcwd() 
os.chdir("Assignment")

## Merge all male files
maledir = os.getcwd()+'/raw_result/raw_male'
malenames = []
for file in os.listdir(maledir):
    if file.endswith(".txt"):
        malenames.append(file)
malenames     # list all male files' names

all_male_file = open('All_Male.txt','a+') 
for name in malenames:  
    filepath = maledir + '/'
    filepath = filepath + name 
    for line in open(filepath,encoding='latin1'): 
        all_male_file.write(line)  
all_male_file.close()       # now we get a single file for all male characters


## Merge all female files
femaledir = os.getcwd()+'/raw_result/raw_female'
femalenames = []
for file in os.listdir(femaledir):
    if file.endswith(".txt"):
        femalenames.append(file)
femalenames      # list all female files' names

all_female_file = open('All_Female.txt','a+') 
for name in femalenames:  
    filepath = femaledir + '/'
    filepath = filepath + name 
    for line in open(filepath,encoding='latin1'): 
        all_female_file.write(line)  
all_female_file.close()     # now we get a single file for all female characters


## Sort all of the characters based on sentiment
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



## Find the 10 most common descriptors
## For all male characters
male_des = []
for i in range(len(df_male)):
    data = df_male.iloc[i,1]
    data = re.findall(r"((?<=He's).*)", data)    # remove He's, just leave useful character
    data = "".join(data)    # conver list into string
    male_des.append(data)

male_des = "".join(male_des)   # conver list into string
male_des     # all descriptions for male characters


## For all female characters
female_des = []
for i in range(len(df_female)):
    data = df_female.iloc[i,1]
    data = re.findall(r"((?<=She's).*)", data)    # remove She's, just leave useful character
    data = "".join(data)    # conver list into string
    female_des.append(data)

female_des = "".join(female_des)   # conver list into string
female_des    # all descriptions for female characters


## Get Wordlists
def find_wordlist(textblob, num):
    n_grams = textblob.ngrams(num)
    word_list = []
    for wlist in n_grams:
        word_list.append(" ".join(wlist))   # covert wordlist into list
    return word_list

male_blob = TextBlob(male_des)
female_blob = TextBlob(female_des)
male_wordlist = find_wordlist(male_blob, 3)
female_wordlist = find_wordlist(female_blob, 3)


## Count the frequencies of these wordlists
def find_most_common(wordlist):
    c = Counter(wordlist)
    most_common_phrases = c.most_common(10)
    common_list = []
    for k,v in most_common_phrases:
        common_list.append(str('{0: <5}'.format(v)) + k)
    return common_list

pprint(find_most_common(male_wordlist))    # the 10 most common descriptions of male along with the frequency
pprint(find_most_common(female_wordlist))  # the 10 most common descriptions of female along with the frequency



## Submit the most common descriptors as text files
male_common_file = open('male_most_commom.txt','a+') 
for line in find_most_common(male_wordlist):
    male_common_file.write(line + "\n")
male_common_file.close()

female_common_file = open('female_most_commom.txt','a+') 
for line in find_most_common(female_wordlist):
    female_common_file.write(line + "\n")
female_common_file.close()
