
from bs4 import BeautifulSoup
import os
import re
import csv


regex = re.compile('[A-Z]\w+')
names = []
names.append(['first name','last name','email 1', 'email 2'])
path = './files'
files = os.listdir(path)
#print(files)
for file in files:
    #print(file)
    if '.html' in file:
        #print('open this:', file)
        
        open_path = path+'/'+str(file)
        fh = open(open_path,'r').read()
        soup = BeautifulSoup( fh, 'html.parser')
        #beautiful_soup=soup.prettify(), this is just a string
        results = soup.find_all('span', attrs={'class':'department-leadership__name'})

        for result in results:
            content = result.contents[0]
            trimed = content[:len(content)-2]
            rx = regex.findall(trimed)
            fl = [rx[0],rx[-1]]
            slug = '.'.join(fl)
            email_1 =  slug+'@nyulangone.org'
            email_2 =  slug+'@nyumc.org'
            #print('raw',trimed,'fl',fl,'email 1:',email_1,'email 2:',email_2)
            fl.append(email_1)
            fl.append(email_2)
            #print(fl)
            names.append(fl)

output_file = open('results.csv','w',newline='')
output_writer = csv.writer(output_file)
for name in names:
    output_writer.writerow(name)
output_file.close()

# Target : <span class="department-leadership__name">Shengping Zou, </span>
# Download all web pages as full html into the folder

# Struct:
# create name list
# get list of all html files in folder

# Loop thru each html file
#   open file 
#   load file into bs4 
#   find name based on target
#       Target : <span class="department-leadership__name">Shengping Zou, </span>
#       save names into list
# export list to csv

# optional:
#   Regex parse to remove middle intitial
#   build final email strings
#       First.Last@{domain1, domain2}
#       FirstLast@{domain1, domain2}
