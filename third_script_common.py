from second_script_sort import df_male, df_female
import re
from textblob import TextBlob
from collections import Counter
from pprint import pprint

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
    data = re.findall(r"((?<=She's).*)", data)    # remove He's, just leave useful character
    data = "".join(data)    # conver list into string
    female_des.append(data)

female_des = "".join(female_des)   # conver list into string
female_des 


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