import os
os.getcwd() 
os.chdir("Assignment")   # change the path to your data set located

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
