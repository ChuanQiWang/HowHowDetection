#-*- coding: UTF-8 -*- 
import jieba
import jieba.analyse
import sys
import string

label = sys.argv[1]
name = sys.argv[2]

import codecs

fr = open('./list','r')
f = open('howhow', 'w') 
feature = codecs.open('howhow_feature', 'r',encoding='utf8') 
list = []
count = 0
while True:
    line = feature.readline()
    line = line.strip('\n')
    if (line.strip() == ''):
        break
    list.append(line)
    #print line  
#for i in range(len(list)):
#    print list[i]

gram = []
purify_log = []
sample =  codecs.open(name ,'r', encoding='utf8')
count = 0
while True:
    count += 1
    line2 = sample.readline()
    line2 = line2.strip('\n')
    if (line2.strip() == ''):
        break
    #print line2
    purify_log.append(line2)
words =  jieba.cut(purify_log[0], cut_all=False)

insample = []
for word in words:
     insample.append(word)#.encode('utf8'))
      
#for i in range(len(insample)):
    #print insample[i] 


for i in range(0,len(list)):
    gram.append(0)
#print type(insample[1])
#print insample[1]
#print type(list[-1])
#print list[-1]
#
#for i in range(0,len(insample)):
#s = "事產學".decode('utf-8')
#print s 
#print type(s)
#print list[-1].strip()==s
for i in range(0,len(insample)):
    for j in range(0,len(list)):
        #print list[j]
        if(list[j].strip() == insample[i].strip()):
            gram[j] += 1
	 #   print gram[j] 
#print gram
output = label + ' '
cnt = 1
for i in range(0,len(gram)):
    if gram[i]!=0:
        output = output + str(cnt) + ":" + str(float(gram[i])) + ' '
    cnt = cnt +1

if len(output)!=2:
    print output

sample.close()
feature.close()

